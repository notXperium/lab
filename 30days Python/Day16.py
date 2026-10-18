from datetime import datetime, date, timedelta

now = datetime.now()

day = now.day
month = now.month
year = now.year
hour = now.hour
minute = now.minute
second = now.second
timestamp = now.timestamp()

#print('timestamp', timestamp)
#print(f'{day}/{month}/{year}, {hour}:{minute}')

newYear = datetime(2020, 1, 1)
#print(newYear)

time_two = now.strftime("%d/%m/%Y, %H:%M:%S")
#print("time two:", time_two)  

date_string = "5 December, 2019"
date_object = datetime.strptime(date_string, "%d %B, %Y")
#print(date_object)

d = date(2020, 1, 1)
print(d.today())

print(date.today() - d)

t1 = timedelta(weeks=12, days=10, hours=4, seconds=20)
t2 = timedelta(days=7, hours=5, minutes=3, seconds=30)

print(t1-t2)