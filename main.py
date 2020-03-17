import json
import os
import requests
import monday_api
from dotenv import load_dotenv


load_dotenv() 

class bigData():
    load_dotenv() 
    monday_auth = os.getenv('Monday_Authorization')
    monday_url = ('https://api.monday.com/v2/')
    def __init__(self, authKey, app, data):
        self.authkey = authKey
        self.app = app
        self.data = data

    def author_get(self):
        secret = self.authkey
        self.secret = secret
        get_data = requests.post(self.app, data={'query': self.data}, headers=eval(self.secret))
        print(get_data.status_code)
        print(get_data.text)
        return (get_data.text) #this is a dict & json

    def author_post(self):
        secret = self.authkey
        self.secret = secret
        get_data = requests.get(self.app, data={'query': self.data}, headers=eval(self.secret))
        print(get_data.status_code)
        print(get_data.text)
        return (get_data.text)
        



monday_getauth = bigData(bigData.monday_auth, bigData.monday_url, monday_api.monday_board_get('419053564')) #<- for this function only board ID is required.
monday_getauth.author_get() #this is the monday data


