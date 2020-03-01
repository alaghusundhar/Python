###  Script : Python Code to Make a Simple and POST Request
###  Author : Alagusundaram Nithyanandam
###  Role : Senior Devops Engineer

import requests
import json

jsonurl="https://reqres.in/api/users"

## Simple Function to make the get request and iterates through Json data

def functionforgetrequests():

    getjson=requests.get(jsonurl)
    jsondata=getjson.json().get('data',[])
    for iteratejson in jsondata:
        print("This is the whole json data : ",iteratejson)
        print("Email from Json is : ",iteratejson["email"])
        print("First Name from Json is : ",iteratejson["first_name"])
        print("Last Name from Json is : ", iteratejson["last_name"])

## Simple Function to make the POST request to an API

def functionforpostrequests():
    data = {'name': "alagu",
            'job': "leader"}
    postrequest=requests.post(jsonurl,data=data)
    print(postrequest.text)

functionforgetrequests()
functionforpostrequests()

