tage = 5

for i in range(1, tage+1):
    print(f"Tag {i}")

nummer = {}
werte = [6,7,5]
print("\n")

for i in range(len(werte)):
    nummer[i+1] = werte[i]

for key, value in nummer.items():
    print(f"{key}: {value}")

print("\n")
for key, value in enumerate(werte, start=1):
    print(f"{key}: {value}") 


print("\n")

n = 4
for i in range(n, 0, -1):
    print(i)
print("Los")

print("\n")

konten = {"ING": 500, "N26": 120, "Revolut": 80}

summe = 0
for key in konten.keys():
    summe += konten[key]
print(summe)

print("\n")

zaheler = {}
habits = ["Gym", "Physio", "Gym", "Lernen", "Gym"]

for h in habits:
    zaheler[h] = zaheler.get(h, 0) +1

print(zaheler)

maxKey = None
maxValue = None

for key, value in zaheler.items():
    if maxValue is None or value > maxValue:
        maxKey = key
        maxValue = value
print(f"{maxKey}: {maxValue}")