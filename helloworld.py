'''docstring for the file overall
by: Troy Center, troycenter1@gmail.com, Coding Dojo Python fundamentals, June 2017
'''
#pylint: disable=C0103
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')

def hello_world():
    return render_template("index.html")

app.run(debug=True)
