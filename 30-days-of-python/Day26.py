from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/') 
def home ():
    return '<h1>Welcome</h1>'

@app.route('/about')
def about():
    return "<h1>About</h1>"

@app.route('/post', methods= ['GET','POST'])
def post():
    name = 'Text Analyzer'
    if request.method == 'GET':
         return "<h1>GET</h1>"
    if request.method =='POST':
        content = request.form['content']
        print(content)
        return "<h1>Recieved</h1>"



if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8000))
    app.run(debug=True, host='0.0.0.0', port=port)