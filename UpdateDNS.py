from requests import get, Session
from datetime import datetime
from os import environ

ip = get('https://api.ipify.org').content.decode('utf8')
hostname = 'api.domeneshop.no'
user = environ['API_USER']
password = environ['API_PASSWORD']
domainid = environ['DOMAINID']
dnsid = environ['DNSID']
host = environ['HOST']
dnsrecord = {'host': host, 'ttl': 300, 'type': 'A', 'data': ip}
dt = datetime.now()
time = dt.strftime("%H:%M:%S %Y-%m-%d")

session = Session()
session.auth = (user, password)
auth = session.post('https://' + hostname)
response = session.put('https://' + hostname + '/v0/domains/' + domainid + '/dns/' + dnsid, json=dnsrecord)
print(time + " " + response.url + " " + str(response.status_code))