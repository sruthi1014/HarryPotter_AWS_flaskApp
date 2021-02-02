from flask import Flask,render_template, request
import pickle
import numpy as np

data=pickle.load(open('harry.pkl','rb'))

app=Flask(__name__)

@app.route('/')
def intro():
    return render_template('html_harry.html')

@app.route('/submit',methods=['POST'])
def fetch():
    input=request.form['a']
    input1=request.form['b']
    print(input,input1)
    return render_template('after.html',data=list(input,input1))