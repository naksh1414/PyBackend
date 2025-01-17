import firebase_admin
from firebase_admin import credentials


def initialize_firebase():
    cred = credentials.Certificate('./xdrives-firebase-adminsdk-aemyz-b6135399f6.json')
    firebase_admin.initialize_app(cred)
