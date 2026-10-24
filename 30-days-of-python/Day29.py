from flask import Flask,  Response
import json
import os

app = Flask(__name__)

student_list = [
    {
        'name':'Asabeneh',
        'country':'Finland',
        'city':'Helsinki',
        'skills':['HTML', 'CSS','JavaScript','Python']
    },
    {
        'name':'David',
        'country':'UK',
        'city':'London',
        'skills':['Python','MongoDB']
    },
    {
        'name':'John',
        'country':'Sweden',
        'city':'Stockholm',
        'skills':['Java','C#']
    }
]


@app.route('/api/v1.0/students', methods = ['GET'])
def students ():
    return Response(json.dumps(student_list), mimetype='application/json')

@app.route('/api/v1.0/students/<id>', methods = ['GET'])
def single_student (id):
    print(id)
    print()
    if [student for student in student_list if student["name"] == id]:
        return Response(json.dumps([student for student in student_list if student["name"] == id]), mimetype='application/json')
    else: 
        return Response(json.dumps(student_list), mimetype='application/json')
 
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8000))
    app.run(debug=True, host='0.0.0.0', port=port)