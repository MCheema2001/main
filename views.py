from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import pymongo
from pymongo import MongoClient

# Create your views here.
Username = "Musa"  # Username for Online MongoDB
Password = "1234"  # Password for Online MongoDB
GateID = "2345"

Online_Data_Base_URL = (
    "mongodb+srv://"
    + Username
    + ":"
    + Password
    + "@cluster0-ifrbh.mongodb.net/MIM?retryWrites=true&w=majority"
)

def index(response):
        json = ""
        cluster = MongoClient(
            Online_Data_Base_URL
        )  # Online DataBase is Accesed
        db = cluster[
            "MIM"
        ]  # Online Cluster is Accessed Name Should be Changed Accordingly if Not Changed it will auto create new one with this name
        coll = db.UsersInfo  # Acessing this DataBase Collection
        x = coll.find({"Email": "mcheema2010@gmail.com"})  # Email is found
        for i in x:  # For loop to Extract Load Data
            json = {
                "Name": i["Name"],
                "Credits": i["Credits"],
            }  # Json Is Made to Send Data that is Requested
        if json == "":  # If no User is Found Json is empty so 404 Abort is Called
            return JsonResponse({"Message":"Error"})
        return JsonResponse(json)
    