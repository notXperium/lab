

def token(text):
    if type(text) is not str: raise TypeError("Muss String sein")

    zeichen = "+-/*()"
    ziffer = "0123456789."
    ergebniss = []
    zahl = ""

    for i in text.replace(" ", ""):
        if i not in zeichen and i in ziffer:
            zahl+=i
        elif i in zeichen:
            if len(zahl)>=1: ergebniss.append(float(zahl)); zahl = ""
            ergebniss.append(i)
        else: raise ValueError("Falsche Eingabe")
    if len(zahl)>=1: ergebniss.append(float(zahl)); zahl = ""
    return ergebniss

print(token("1+os"))
