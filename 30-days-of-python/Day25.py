import pandas as pd
import numpy as np

s = pd.Series(["A","B","C"], index = [1,2,3])

print(s)

dct = {'name':'Asabeneh','country':'Finland','city':'Helsinki'}

print(pd.Series(dct))

print(pd.Series(np.linspace(10,50,5)))

data = [
    ['Asabeneh', 'Finland', 'Helsink'],
    ['David', 'UK', 'London'],
    ['John', 'Sweden', 'Stockholm']
]

print(pd.DataFrame(data, columns=["Name", "Country", "City"]))

data = [
    {'Name': 'Asabeneh', 'Country': 'Finland', 'City': 'Helsinki'},
    {'Name': 'David', 'Country': 'UK', 'City': 'London'},
    {'Name': 'John', 'Country': 'Sweden', 'City': 'Stockholm'}]

d = pd.DataFrame(data)

df = pd.read_csv("/Users/lennox/Documents/lab/30-days-of-python/weight-height.csv")

print(df.tail(10))
print(df.columns)
print(df["Gender"].head(10))

print(df["Height"].describe())

d["Weight"] = [74, 83, 117]

print(d)

d["Height"] = [173, 180, 193]

d['Height'] *= 0.01

print(d)

def bmicalc(dataset):
    weight = dataset['Weight']
    height = dataset['Height']

    bmi = []

    for w,h in zip(weight,height):
        bmi.append(round(w/(h**2), 2))
    return bmi

d["BMI"] = bmicalc(d)


d["Birth Year"] = ['1769', '1985', '1990']
print(d)


def age(yearArray):
    from datetime import datetime

    today = datetime.today().year
    age = []
    for year in yearArray:
        age.append(today-int(year))
    return age

d["Age"] = age(d["Birth Year"])
d["Alive"] = d['Age'] < 100
print(d)







