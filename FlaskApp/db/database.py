import pymongo
import requests
import certifi
import ssl
ca = certifi.where()

client = pymongo.MongoClient("mongodb+srv://admin:EngageAdmin@cluster0.chousnu.mongodb.net/?retryWrites=true&w=majority",ssl=True, ssl_cert_reqs=ssl.CERT_NONE)
Database = client.get_database('Engage')
# Table
# SampleData = Database.get_collection("User").find_one()
# SampleData2 = Database.get_collection("Engage").find_one()
# print(SampleData)
# print(SampleData2)

