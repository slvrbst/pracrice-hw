import os
import subprocess
import codecs
from flask import Flask, render_template, request, flash, redirect

app = Flask(__name__)

@app.route("/index")
@app.route("/")
def index():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/extraction")
def extraction():
    txt0 = request.form['txt']
    with codecs.open('./test.txt', 'w', 'utf-8') as f:
        f.write(str(txt0))
    command = ['./tomitaparser', 'config.proto']
    output = subprocess.check_output(command)
    return render_template('pretty.html')




if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port = 5000)