from datetime import datetime, timedelta

zeit = "2026-10-05 15:59"

p = datetime.strptime(zeit, "%Y-%m-%d %H:%M")
print(p.date())

heute = datetime.strptime("2026-10-12", "%Y-%m-%d").date()
eintraegestr = ["2026-10-08 10:00", "2026-10-01 10:00"]
eintraege = []
for eintrag in eintraegestr:
    eintraege.append(datetime.strptime(eintrag, "%Y-%m-%d %H:%M").date())

print(eintraege)

for eintrag in eintraege:
    print(heute - eintrag <= timedelta(days=7)) 