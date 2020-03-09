import requests

url = "http://10.68.34.87:8086/query?db=mdt_db&q=SELECT * FROM \"Cisco-IOS-XE-wireless-awips-oper:awips-oper-data/awips-alarm\""

payload  = {}
headers = {

}

response = requests.request("GET", url, headers=headers, data = payload)

print(response.text.encode('utf8'))
