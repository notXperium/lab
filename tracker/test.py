data = [6,7,5,8,7,6,9]           


def mittelwert(werte):
    sum = 0
    for i in werte:
        sum += i
    return round(sum/len(werte), 2)

def median(werte):
    werte.sort()
    median = 0

    if len(werte) % 2 == 0:
        median1= werte[int(len(werte)/2)]
        median2= werte[int((len(werte)/2)+1)]
        median= (median1 + median2) /2
    else:
        median = werte[int((len(werte) +1) / 2)]

    return median

def spannweite(werte):
    werte.sort()
    return werte[int(len(werte))-1] - werte[0]

print(mittelwert(data))
print(median(data))
print(spannweite(data))

