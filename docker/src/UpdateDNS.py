from requests import get, Session
from datetime import datetime
from os import environ

ip = get('https://api.ipify.org').content.decode('utf8')
apiURL = 'api.domeneshop.no'
apiUser = environ['APIUSER']
apiKey = environ['APIKEY']
domainid = environ['DOMAINID']
dnsID = environ['DNSID']
dnsHost = environ['DNSHOST']
dnsrecord = {'host': dnsHost, 'ttl': 300, 'type': 'A', 'data': ip}
dt = datetime.now()
time = dt.strftime("%H:%M:%S %Y-%m-%d")

session = Session()
session.auth = (apiUser, apiKey)
auth = session.post('https://' + apiURL)
response = session.put('https://' + apiURL + '/v0/domains/' + domainid + '/dns/' + dnsID, json=dnsrecord)
print(time + " " + response.url + " " + str(response.status_code))