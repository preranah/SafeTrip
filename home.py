from __future__ import division
from flask import Flask, render_template, request, url_for, jsonify, abort, redirect
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

@app.route('/data/', methods=['POST','GET'])
def postdata():
	#lat = request.json['lat']
	#lng = request.json['lng']
	data = request.args.to_dict()
	print data
	lat = float(data['lat']) 
	lng = float(data['lng'])
	query = "SELECT * from TravelSafe_Earthquake.Earthquake_7 where latitude > " + str(lat-5) + " AND latitude < " + str(lat+5) + " AND longitude > " + str(lng-5) + " AND longitude < " + str(lng+5)
	data = getdata(query) 
	return json.dumps(data)

if __name__ == "__main__":
    app.run()


