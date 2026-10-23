a = "Thirty"
b = "Days"
c = "Of"
d = "Python" 

st1 = "{} {} {} {} ".format(a, b, c, d)

print(st1)

e = "Coding"
f = "For"
g = "All"

st2 = "{} {} {}".format(e,f,g)
print(st2.upper()) 
print(st2.lower())
print(st2[7:])
print(st2.find("Coding"))
print(st2.replace("Coding", "python"))
company = st2
print(len(company))

print("Name\tAge")
print("Ali\t17")