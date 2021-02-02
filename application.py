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
    print(input)
    details=csvdata.loc[[input]]
    print(details.House)

    return render_template('after.html',data=details)
if __name__== "__main__":
    application.run(debug=True)