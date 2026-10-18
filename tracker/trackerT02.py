from datetime import datetime, timedelta
from pathlib import Path
import argparse
import json
import copy

def mittelwert(werte):
    if len(werte) >= 1:
        sum = 0
        for i in werte:
            sum += i
        return round(sum/len(werte), 2)
    else: return None

def median(werte):
    if len(werte) >= 1:
        werte.sort()
        n = len(werte)
        mitte = n // 2

        if n % 2 == 0:return (werte[mitte - 1] + werte[mitte]) / 2
        else: return werte[mitte]
    else: return None

def spannweite(werte):
    if len(werte) >= 1:
        werte.sort()
        return werte[int(len(werte))-1] - werte[0]
    else: return None


p = argparse.ArgumentParser(description="Tracker auswerten")
p.add_argument("feld", choices=["stimmung", "ruecken"])
p.add_argument("--tage", type=int, default=7)
args = p.parse_args()

folder = Path(__file__).parent
path = folder / "eintraege.jsonl"

data = []
werte = []
pro_tag_stimmung = {}
pro_tag_ruecken = {}

with open(path, "r", encoding="utf-8") as file:
    for line in file:
        if line.strip():
            data.append(json.loads(line))

    for eintrag in data:    
        tag = eintrag["zeit"][:10]
        stimmung = eintrag.get("stimmung")
        ruecken = eintrag.get("ruecken")

        if stimmung is not None:
            if tag not in pro_tag_stimmung:
                pro_tag_stimmung[tag] = []
            pro_tag_stimmung[tag].append(stimmung)

        if ruecken is not None:
            if tag not in pro_tag_ruecken:
                pro_tag_ruecken[tag] = []
            pro_tag_ruecken[tag].append(ruecken)

    heute = datetime.today().date()

    pro_tag = {"stimmung": copy.deepcopy(pro_tag_stimmung), "ruecken": copy.deepcopy(pro_tag_ruecken)} 

    for key, value in pro_tag[args.feld].items():
        day = datetime.strptime(key, "%Y-%m-%d").date() 
        if len(value) >= 1 and heute - day <= timedelta(days=args.tage):
            for i in value:
                werte.append(i)

mw = None
md = None
sp = None

if len(werte) >= 1:
    mw = mittelwert(werte)
    md = median(werte)
    sp = spannweite(werte)

print(f"{args.feld} der letzten {args.tage} Tage:\nWerte: {len(werte)}\nMittelwert: {mw}\nMedian: {md}\nSpannweite: {sp} ")