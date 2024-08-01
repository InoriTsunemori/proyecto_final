import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate('clave_json_firebase\proyectopinaldass-firebase-adminsdk-q0mci-b5f55f4c18.json')
firebase_admin.initialize_app(cred)
db = firestore.client()

