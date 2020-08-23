import urllib.request
import urllib.parse
import urllib.error
import json
import ssl

serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

address = input('Enter location: ')
api_key = 'AIzaSyCN2gKJpdqFGssvOVdKpofet_gatLQ1K64'
parms = dict()
parms['address'] = address
parms['key'] = api_key
url = serviceurl + urllib.parse.urlencode(parms)
print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read().decode()
print("retreived", len(data))

try:
    js = json.loads(data)
except:
    js = None

if not js or "status" not in js or js["status"] != "OK":
    print("======failure=====")
    print(data)

print(json.dumps(js, indent=4))
