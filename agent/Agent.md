# Agent

## Was ist das?
Mein erster in Python geschriebener AI Agent, basierend auf der Google Gemini API. Gemini entscheidet selbst, welches Werkzeug es für eine Frage braucht, ruft es auf und antwortet mit dem Ergebnis.

## Werkzeuge
| Funktion | Was? |
| --- | --- |
| [Rechne](./agent.py#L20-L24) | Rechnet mathematische Ausdrücke mit den Funktionen aus dem [Rechner](/rechner/Rechner.md) aus |
| [Wetter](./agent.py#L27-L44) | Holt Wetterdaten über die [Open-Meteo](https://open-meteo.com/) API |
| [Lies Notizen](./agent.py#L46-L53) | Liest die Notiz zu einem Datum, Dateien außerhalb des Notiz-Ordners sind gesperrt |
| [Liste Notizen](./agent.py#L55-L68) | Listet alle Notizen der letzten Tage auf, ohne Angabe alle |