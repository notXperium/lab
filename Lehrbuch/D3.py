eintraege = [
    {"tag": "Mo", "habit": "Gym", "stimmung": 7},
    {"tag": "Mo", "habit": "Physio", "stimmung": 8},
    {"tag": "Di", "habit": "Gym", "stimmung": 8}
]

lst1 = []
lst2 = []

for i in eintraege:
        lst1.append(i["habit"])

print(lst1)

for i in eintraege:
    if i["habit"] == "Gym":
        lst2.append(i["stimmung"])

print(lst2)

days = {}

for i in eintraege:
    print(i["stimmung"])
    days[i["tag"]] = days.get(i["tag"], [])
    days[i["tag"]].append(i["stimmung"])

        

        

print(days)