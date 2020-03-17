import yaml
import os
import requests
import json
import graphene
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
        get_data = requests.post(self.app, json={'query': self.data }, headers=eval(self.secret)) #may need to create instance variable for {data} to work with Actions, without writing another request variable
        print(get_data.status_code)
        print(get_data.text)
        return (get_data.text) #this is a dict & json

    def author_post(self):
        secret = self.authkey
        self.secret = secret
        get_data = requests.get(self.app, json={'query': self.data }, headers=eval(self.secret)) #may need to create instance variable for {data} to work with Actions, without writing another request variable
        print(get_data.status_code)
        print(get_data.text)
        return (get_data.text)
        



monday_getauth = Authentication(Authentication.monday_auth, Authentication.monday_url,monday_api.monday_boards_items(419051066))
monday_getauth.author_get() #this is the monday data

