from flask import Flask
import pymongo 
import os 
MONGODB_URI = 'MongoURI'
client = pymongo.MongoClient(MONGODB_URI)

db = client.test

students = [
        {'name':'David','country':'UK','city':'London','age':34},
        {'name':'John','country':'Sweden','city':'Stockholm','age':28},
        {'name':'Sami','country':'Finland','city':'Helsinki','age':25},
    ]
for student in students:
    db.students.insert_one(student)

for i in client["test"].students.find({}, {"_id":0,  "name": 1, "country":1}):
    print(i)


app = Flask(__name__)
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)