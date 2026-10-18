person = [ {
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
    },
    {
    'first_name':'Benjamin',
    'last_name':'Yetayeh',
    'age':12,
    'country':'Germany',
    'is_marred':False,
    'skills':['nothing', "even less"],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
    }
]

print(len(person))

print(person[0].get("is_marred"))
person[0]["job_tite"] = "Entwickler"
person[0]["skills"].append("Docker")
person[0]["last_name"] = "Smith"

person[0].pop("job_tite")
person[0].popitem()
del person[0]['skills']

for item in person:
    # for key, value in item.items():
    #     print(key, value, "\n")
    # print("\n")
    for i in item.keys():
        print(i, item[i])
    print("\n")