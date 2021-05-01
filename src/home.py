from flask import Flask, render_template, url_for, request, session, redirect  
import requests
import pymongo
import os, time
import json 
from json import loads
from time import sleep
from json import dumps
import threading
jsval=[]
app = Flask(__name__)
app.secret_key = 'any random string'
countres=0
users = 0

@app.route("/search",methods=["GET","POST"])
def search():
	return render_template("search.html")

@app.route("/search_check",methods=["GET","POST"])
def show_results():
	req=request.form
	req=dict(req)
	val = str(req['uid'])
	query="https://swapi.dev/api/people/?search="+val
	print("query is:",query)
	response = requests.get(query)
	jsval=response.json()
	# print("response :",response.json())
	# colours = ['Red', 'Blue', 'Black', 'Orange']
	namelis=[]
	vall=val.lower()
	print(len(jsval),":",jsval['count'])
	for i in range(min(len(jsval),jsval['count'])):
		curname=jsval['results'][i]['name'].lower()
		curname2=curname.replace(vall, vall.upper())
		namelis.append(curname2)

	return render_template("search.html", countval=min(len(jsval),jsval['count']),colours=namelis)

@app.route('/submit-form', methods = ['POST'])
def submitForm():
    selectValue = request.form.get('select1')
    # return '<h1>You selcted : (str(selectValue))</h1>'
    return '<h1>You selected:: {}!</h1>'.format(selectValue)



if __name__ == "__main__":
    app.run(debug=True, threaded=True)