from flask import Flask, render_template

#export FLASK_APP=main.py
#q for exiting git commands in terminal

app = Flask(__name__)

@app.route('/')
def hello_world():
  return render_template("index.html")

@app.route('/test')
def hi():
  return render_template("test.html")

app.run(host='0.0.0.0', port=8080)

