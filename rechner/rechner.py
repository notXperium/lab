
def token(text):
    if type(text) is not str: raise TypeError("Muss String sein")

    zeichen = "+-/*()"
    ziffer = "0123456789."
    ergebniss = []
    zahl = ""

    for i in text.replace(" ", "").replace("−", "-"):
        if i not in zeichen and i in ziffer:
            zahl+=i  
        elif i == "-" and zahl == "" and len(ergebniss) >= 1 and ergebniss[-1] in ("*", "/"):
            zahl = "-"
        elif i in zeichen:
            if len(zahl)>=1: ergebniss.append(float(zahl)); zahl = ""
            ergebniss.append(i)
        else: raise ValueError("Falsche Eingabe")
    if len(zahl)>=1: ergebniss.append(float(zahl)); zahl = ""
    return ergebniss

def sort(text):

    temp = []
    geklammert = []
    Klammer = 0

    for i in text:
        if str(i) == "(": Klammer += 1
        elif str(i) == ")": Klammer -= 1

        if Klammer > 0 :
            if Klammer == 1:
                if str(i) != "(":
                 temp.append(i)
            else:
                temp.append(i)
        elif Klammer == 0 and len(temp)>=1: geklammert.append(sort(temp)); temp = []

        else: geklammert.append(i)

    out = []
    for i in geklammert:
            if str(i) in "+-":
                if len(temp)>=1: out.append(temp); temp = []
                out.append(i)
            else: temp.append(i)
    if len(temp) >=1: out.append(temp); temp = []

    return out

def calc(shelf):

    out = []
    result = 0
    sum_operator = "+"

    for i in shelf:

        if type(i) is list:
            PROD = 1
            prod_operator = "*"
            for w in i:
                if type(w) is list: w = calc(w)
                if str(w) in "*/": prod_operator = w
                if type(w) is float:
                    if prod_operator == "*": PROD *= w
                    else: 
                        if w != 0: PROD /= w
                        else: raise ZeroDivisionError("Kann nicht durch 0 teilen!")
            out.append(PROD)
        else:
            out.append(i)

    for i in out:
        if str(i) in "+-": sum_operator = i
        if type(i) is float:
            if sum_operator == "+": result +=i
            else: result -=i
    
    return result


                    





