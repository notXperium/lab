konten = {"ING": 500, "N26": 120, "Revolut": 80}
summe = 0
for i in konten.keys():
    summe += konten[i]

print(summe)

habits = ["Gym", "Physio", "Gym", "Lernen", "Gym"]  
tst = []
for i in habits:
    tst.append(habits.count(i))

print(tst)

werte = dict(zip(habits, tst))

print(werte)
max_key = None
max_value = None
for key, value in werte.items():
    if max_value is None or value > max_value:
        max_key = key
        max_value = value

print(f"\n{max_key} {max_value} \n\n")

zaehler = {}
for h in habits:
    zaehler[h] = zaehler.get(h, 0) + 1
print(zaehler)

