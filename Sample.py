# coding: utf-8
from settings import *
import json, requests
import pymongo



#Information from settings file
headers = { 'AccountKey': ACCOUNT_KEY,
            'UniqueUserID': UNIQUE_USER_ID,
            'accept':'application/json'}

#Set the URL from one of the urls in settings file or make your own
url = SPEED_BANDS

r = requests.get(url, headers=headers)

#Take note that r.json() is a list of dictionaries
result = r.json()

for i in result['d']:
    for k,v in i.iteritems():
        print k, '\n\t', v
    
    print '-------------------------------------------'


conn = pymongo.MongoClient('mongodb://localhost', safe=True)
db = conn.lta
collection = db.speedbands

for i in result['d']:
    collection.insert(i)
