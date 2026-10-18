i = 0

while i < 10:
    i+=1
    if i==3:
        print(i)
        continue
else: 
    print("los")

numbers = (0, 1, 2, 3, 4, 5)

for n in numbers:
    print(n)

language = 'Python'
for l in language:
    print(l)

person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
}

for key, value in person.items():
     print(key, value)


print(list(range(0,11,2)))
print(set(range(0,7,3)))

# for k in person:
#     if k == 'skills':
#         for s in person["skills"]:
#             print(s)

for k in person["skills"]:
    print(k)
else:
    print("end")

for i in range(11):
    print(i, "x", i, "=", i**2)