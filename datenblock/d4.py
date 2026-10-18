import json
from pathlib import Path


def mittelwert(werte):
        sum = 0
        if werte:
            for i in werte:
                sum += i
            return round(sum/len(werte), 2)
        else:
            return sum

with open(Path(__file__).parent / "d4.jsonl", "a+") as f:
    f.seek(0)
    i = 0
    eintraege = []
    for line in f.read().splitlines():
        if line.strip():
            eintraege.append(json.loads(line))
            i +=1

     
    #print(f"{i} Einträge")
    #print(eintraege[0])

    datum = []

    for l in eintraege:
        datum.append(l["zeit"])

   # print(sorted(set(datum[:10])))

    # for date in sorted(set(datum)):
    #     data = eintraege.get(date)
    #     print(data) 


    days = {}
    for eintrag in eintraege:

        try:
            if eintrag["stimmung"]:
                days[eintrag["zeit"][:10]] = days.get(eintrag["zeit"][:10], [])
                days[eintrag["zeit"][:10]].append(eintrag["stimmung"])
        except KeyError:
            pass

    for day, stimmung in sorted(days.items()):

        print(day, mittelwert(stimmung))