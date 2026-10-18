# lab

Mein Lernweg in Code: Python, Mathe und KI, ein Lerntag nach dem anderen.

<!-- Hier kommt bei T07 rein, in meinen Worten: wer ich bin, warum ich das mache, was als Nächstes kommt. -->

## Projekte

| Ordner | Was drin ist | Lerntage |
|---|---|---|
| [`tracker/`](tracker/) | Auswertung meiner Habit-Tracker-Daten: Mittelwert, Median, Spannweite, Zeitraum per Kommandozeile | T01, T02 |
| [`gleichungen/`](gleichungen/) | Löser für `ax + b = cx + d`, druckt die Schritte wie auf Papier, erkennt keine und unendlich viele Lösungen | T03 |
| [`datenblock/`](datenblock/) | Daten verarbeiten: Zählen mit `range`, Zähler mit Dictionaries, Gruppieren, JSONL lesen, Datum rechnen | D1–D5 |
| [`30-days-of-python/`](30-days-of-python/) | Übungen aus [30 Days of Python](https://github.com/Asabeneh/30-Days-Of-Python) | Tag 8–21 |

## Ausführen

```
python tracker/auswertung.py stimmung --tage 7
python gleichungen/loeser.py 7 -4 3 12
```

`tracker/eintraege.jsonl` enthält Beispieldaten, nicht meine echten.

## Aufbau

- Ein Ordner pro Projekt. Projekte wachsen über mehrere Lerntage, welcher Lerntag in welchen Ordner gehört, steht im Lehrbuch oben auf jeder Seite.
- Dateien heißen nach dem, was sie tun (`loeser.py`), nicht nach dem Lerntag. Den Verlauf zeigt Git.
- Daten liegen neben dem Script, das sie liest.
