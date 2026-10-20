# Nachbau von Mike (20.10.) nach dem Stand vom 12.10.: das Original liegt auf dem PC
# in Documents/Lab/Agent. Gleiche Teile: nackte HTTP-Requests an Gemini,
# Tools rechne und wetter, Schleife mit functionCall / functionResponse.
import os
import requests
from dotenv import load_dotenv

load_dotenv()
KEY = os.environ["GEMINI_API_KEY"]
MODELL = "gemini-flash-lite-latest"
URL = f"https://generativelanguage.googleapis.com/v1beta/models/{MODELL}:generateContent"


def rechne(ausdruck):
    return eval(ausdruck)  # T05/T06 ersetzen das durch einen sicheren Rechner


def wetter(ort):
    geo = requests.get(
        "https://geocoding-api.open-meteo.com/v1/search",
        params={"name": ort, "count": 1, "language": "de"},
        timeout=10,
    ).json()
    if not geo.get("results"):
        return f"Ort '{ort}' nicht gefunden"
    treffer = geo["results"][0]
    daten = requests.get(
        "https://api.open-meteo.com/v1/forecast",
        params={"latitude": treffer["latitude"], "longitude": treffer["longitude"], "current": "temperature_2m,wind_speed_10m"},
        timeout=10,
    ).json()
    if daten.get("error"):
        return f"Wetterdienst-Fehler: {daten.get('reason')}"
    jetzt = daten["current"]
    return f"{treffer['name']}: {jetzt['temperature_2m']} °C, Wind {jetzt['wind_speed_10m']} km/h"


TOOLS = [{
    "functionDeclarations": [
        {
            "name": "rechne",
            "description": "Rechnet einen mathematischen Ausdruck aus, z. B. '3 * (4 + 2)'. Für jede Rechnung benutzen, nicht im Kopf rechnen.",
            "parameters": {
                "type": "object",
                "properties": {"ausdruck": {"type": "string", "description": "Der Ausdruck in Python-Schreibweise"}},
                "required": ["ausdruck"],
            },
        },
        {
            "name": "wetter",
            "description": "Holt das aktuelle Wetter (Temperatur in °C, Wind) für einen Ort.",
            "parameters": {
                "type": "object",
                "properties": {"ort": {"type": "string", "description": "Stadt, z. B. 'Perth'"}},
                "required": ["ort"],
            },
        },
    ]
}]

FUNKTIONEN = {"rechne": rechne, "wetter": wetter}


def frage_modell(verlauf):
    antwort = requests.post(URL, params={"key": KEY}, json={"contents": verlauf, "tools": TOOLS}, timeout=30)
    antwort.raise_for_status()
    return antwort.json()["candidates"][0]["content"]


verlauf = []  # das Modell hat kein Gedächtnis, deshalb schicken wir jedes Mal alles mit
frage = input("Du: ")
verlauf.append({"role": "user", "parts": [{"text": frage}]})

while True:
    inhalt = frage_modell(verlauf)
    verlauf.append(inhalt)

    aufrufe = [teil["functionCall"] for teil in inhalt["parts"] if "functionCall" in teil]
    if not aufrufe:
        print("Agent:", "".join(teil.get("text", "") for teil in inhalt["parts"]))
        break

    antworten = []
    for aufruf in aufrufe:
        name, args = aufruf["name"], aufruf.get("args", {})
        print(f"  [Tool] {name}({args})")
        try:
            ergebnis = FUNKTIONEN[name](**args)
        except Exception as fehler:
            ergebnis = f"Fehler: {fehler}"  # Fehler gehen ans Modell zurück, kein Absturz
        antworten.append({"functionResponse": {"name": name, "response": {"ergebnis": str(ergebnis)}}})
    verlauf.append({"role": "user", "parts": antworten})
