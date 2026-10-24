# Rechner

## Was ist das?
3 Funktionen, die einen Ausdruck als `str` in ein mathematisch korrektes Ergebnis verwandeln, ohne `eval()`. Punkt vor Strich, verschachtelte Klammern und Vorzeichen wie in `2*-3` klappen, Divison durch `0` wirft einen sauberen Fehler. Der [Agent](/agent/Agent.md) nutzt den Rechner als Werkzeug.


## Inhalt
| Funktion | Was? |
| --- | --- |
| [Token](./rechner.py#L2-L21) | Zerlegt die Eingabe in Zahlen und Rechenzeichen und gibt sie als Liste aus, ungültige Zeichen werden abgelehnt |
| [Sort](./rechner.py#L22-L51) | Rekursive Funktion, die Klammern auflöst und jede Klammer als eigene Liste in der Liste ausgibt |
| [Calc](./rechner.py#L52-L82) | Rekursive Funktion, die diese Listen ausrechnet, Punkt vor Strich |