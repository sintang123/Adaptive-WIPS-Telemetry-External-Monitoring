from flask import Flask, escape, request, render_template
from dateutil import parser
from datetime import datetime
import time
import requests
import json

app = Flask(__name__)

@app.route('/')
def home():
    #name = request.args.get("name", "World")

    value = getDataFromDB()
    
    return render_template('template.html', posts=value)

def getDataFromDB():
	#url = "http://10.68.34.87:8086/query?db=mdt_db&q=SELECT * FROM \"Cisco-IOS-XE-wireless-awips-oper:awips-oper-data/awips-alarm\""
	url = "http://<IP_ADDRESS_HERE>:8086/query?db=mdt_db&q=SELECT * FROM \"Cisco-IOS-XE-wireless-awips-oper:awips-oper-data/awips-alarm\""
	
	payload = {}
	headers = {}

	response = requests.request("GET", url, headers=headers, data = payload)
	jsondata = json.loads(response.text)

	alarmList = []

	for dataArray in jsondata["results"][0]["series"][0]["values"]:

		rawTime = dataArray[0]
		time = datetime_from_utc_to_local(rawTime)
		dataArray[0] = time

		rawAlarmTimestamp = dataArray[5]
		alarmTimestamp = datetime_from_utc_to_local(rawAlarmTimestamp)
		dataArray[5] = alarmTimestamp

		#alarm = alarmTimestamp + "---" + dataArray[2] + "---" + dataArray[3] + "---" + dataArray[4] + "---" + dataArray[6]  + "---" + dataArray[7] + "---" + str(dataArray[9])   
	
		#alarmList.append(alarm)

	#return alarmList
	return jsondata["results"][0]["series"][0]["values"]

#Convert UTC to Singapore Time
def datetime_from_utc_to_local(utc_datetime_string):
	utc_datetime = parser.parse(utc_datetime_string)
	now_timestamp = time.time()
	offset = datetime.fromtimestamp(now_timestamp) - datetime.utcfromtimestamp(now_timestamp)

	localTime = utc_datetime + offset

	year = localTime.strftime("%Y")
	month = localTime.strftime("%b")
	day = localTime.strftime("%d")
	hour = localTime.strftime("%H")
	minute = localTime.strftime("%M")
	second = localTime.strftime("%S")

	localTimeString = day + "-" + month + "-" + year + " " + hour + ":" + minute + ":" + second

	return localTimeString

app.run(debug=True)