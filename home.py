from __future__ import division
from flask import Flask, render_template, request, url_for, jsonify, abort
import urllib2;
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import *
import mysql.connector 
from decimal import Decimal
import simplejson as json

# sudo apt-get install python3-lxml
# sudo apt-get install python-lxml
# apt-get install python-dev libxml2 libxml2-dev libxslt-dev
app=Flask(__name__)
SQLALCHEMY_DATABASE_URI = 'mysql://TravelSafeAdmin:TravelSafeAdmin@ts601.ccxemqbq5sy5.us-west-2.rds.amazonaws.com:3306/TravelSafe_Earthquake'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/query')
def query():
	query = "SELECT * from TravelSafe_Earthquake.Earthquake_7"
	data = getdata(query)
	return json.dumps(data)


def getdata(query):
	conn = mysql.connector.connect(user='TravelSafeAdmin', password='TravelSafeAdmin', database='', host ='ts601.ccxemqbq5sy5.us-west-2.rds.amazonaws.com', use_unicode=True)
	cursor = conn.cursor()
	data = cursor.execute(query)
	data = cursor.fetchall()
	#data = [str(s) for s in data]
	#cursor.close()
	#conn.close()
	return data 

@app.route('/data', methods=['POST'])
def postdata():
	if not request.json:
		abort(400)
	lat = request.json['lat']
	lng = request.jsonify['lng']
	print lat,lng
	return json.dumps(lat)

if __name__ == "__main__":
    app.run()


