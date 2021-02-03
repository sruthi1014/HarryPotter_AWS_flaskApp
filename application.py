from flask import Flask, render_template,request
import pickle
import pandas as pd
application= Flask(__name__)

@application.route('/')
def intro():
    return render_template('html_harry.html')

@application.route('/submit',methods=['POST'])
def fetch():
    csvdata=pickle.load(open('harry.pkl','rb'))
    input=request.form['a']
    if input == 'other':
        input=request.form['b']

    try:
        details = csvdata.loc[[input]]
        return render_template('after.html', data=details)
    except KeyError:
        return "<center><h1>Insert a name from the list</h1><a href='/'> Go back to home page</a></center>"


if __name__== "__main__":
    application.run(debug=True)