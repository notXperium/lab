from datetime import datetime,timedelta
from dotenv import load_dotenv
from pathlib import Path
import requests
import os

load_dotenv()
KEY = os.environ["GEMINI_API_KEY"]
MODELL = "gemini-flash-lite-latest"
URL = f"https://generativelanguage.googleapis.com/v1beta/models/{MODELL}:generateContent"

NOTIZEN = Path(__file__).parent / "notizen"


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

def lies_notizen(datum):
    datum = Path(datum).name
    try:
        with open(f"{NOTIZEN}/{datum}.txt", "r", encoding="utf-8") as notiz:
            notiz.seek(0)
            return notiz.read()

    except: return "File not found"

def liste_notizen(days=None):
    files = sorted([file.stem for file in NOTIZEN.iterdir() if file.suffix == ".txt"])
    out = []
    if days:
        today = datetime.today().date()
        tm = timedelta(days=days)

        for f in files:
            day = datetime.strptime(f, "%Y-%m-%d").date()
            if today - day <= tm:
                out.append(f)
        return out

    return files


    
        


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
        {
            "name": "lies_notizen",
            "description": "Liest Notizen des Datums (Format: YYYY-MM-DD) !Ohne File Endung!",
            "parameters": {
                "type": "object",
                "properties": {"datum": {"type": "string", "description": "Datum z.B. 2026-10-17"}},
                "required": ["datum"],
            },
        },
        {
            "name": "liste_notizen",
            "description": "Erhalte eine Liste aller Notizen (optional von den letzten x Tagen), sortiert (älteste zuerst)",
            "parameters": {
                "type": "object",
                "properties": {"days": {"type": "integer", "description": "Alle Notizen aus den letzten z.B 7 Tagen"}},
            },
        },
    ]
}]

FUNKTIONEN = {"rechne": rechne, "wetter": wetter, "lies_notizen": lies_notizen, "liste_notizen": liste_notizen}


def frage_modell(verlauf):
    antwort = requests.post(URL, params={"key": KEY}, json={"contents": verlauf, "tools": TOOLS}, timeout=30)
    antwort.raise_for_status()
    return antwort.json()["candidates"][0]["content"]


verlauf = []  
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
            ergebnis = f"Fehler: {fehler}"  
        antworten.append({"functionResponse": {"name": name, "response": {"ergebnis": str(ergebnis)}}})
    verlauf.append({"role": "user", "parts": antworten})
