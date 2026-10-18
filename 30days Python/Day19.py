#File Handling
#with open() as x closes file itself
with open("/Users/lennox/Documents/lab/30days Python/jsonday19.txt", "a+") as f:
    f.write("test")
    f.truncate(0)
    f.seek(0)
    for i in range(15):
         f.write(f"{i}\n")
    f.seek(0)
    print(f.read())

import json
person_json = '''{
    "name":"Asabeneh",
    "country":"Finland",
    "city":"Helsinki",
    "skills":["JavaScrip", "React","Python"]
}'''

dct = json.loads(person_json)

print(dct["name"])

person = {
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScrip", "React", "Python"]
}
with open("/Users/lennox/Documents/lab/30days Python/jsonday19.txt", "a+") as f:

    js = json.dump(person, f, ensure_ascii=False, indent=4)

    f.seek(0)
    print(f.read().splitlines())