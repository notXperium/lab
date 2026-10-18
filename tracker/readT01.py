import json
from pathlib import Path

folder = Path(__file__).parent
print("Habits berechnen")

path = folder / "eintraege.jsonl"

data = []
with open(path, "r", encoding="utf-8") as file:
    for line in file:
        if line.strip():
            data.append(json.loads(line))

print(len(data), "Actions logged")

pro_tag = {}
pro_tag_ruecken = {}

for eintrag in data:    
    tag = eintrag["zeit"][:10]
    stimmung = eintrag.get("stimmung")
    ruecken = eintrag.get("ruecken")

    if stimmung:
        if tag not in pro_tag:
            pro_tag[tag] = []

        pro_tag[tag].append(stimmung)

    if ruecken:
        if tag not in pro_tag_ruecken:
            pro_tag_ruecken[tag] = []

        pro_tag_ruecken[tag].append(ruecken)

def mittelwert(werte):
    sum = 0
    for i in werte:
        sum += i
    return round(sum/len(werte), 2)

def median(werte):
    werte.sort()
    n = len(werte)
    mitte = n // 2

    if n % 2 == 0:
        return (werte[mitte - 1] + werte[mitte]) / 2
    else:
        return werte[mitte]

def spannweite(werte):
    werte.sort()
    return werte[int(len(werte))-1] - werte[0]

#print("Stimmung:")
for tag, stimmungen in pro_tag.items():
    print(tag, "\nMittelwert:", mittelwert(stimmungen), "\nMedian:", median(stimmungen), "\nSpannweite:", spannweite(stimmungen))
print("\nRuecken:")
for tag, ruecken in pro_tag_ruecken.items():
    print(tag, "\nMittelwert:", mittelwert(ruecken), "\nMedian:", median(ruecken), "\nSpannweite:", spannweite(ruecken))

