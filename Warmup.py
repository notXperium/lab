#T04
werte = ["2026-10-12", "2026-10-17", "2026-10-20", "2026-10-23"]

from datetime import datetime, timedelta

last7 = []
today = datetime.today().date()
for i in werte:
    day = datetime.strptime(i, "%Y-%m-%d").date()
    if today - day <= timedelta(days=7) and today - day >= timedelta(days=0):
        last7.append(i)

print(last7)
