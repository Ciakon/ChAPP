import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use a service account.
cred = credentials.Certificate('ServiceAccounts.json')

app = firebase_admin.initialize_app(cred)

db = firestore.client()

obj1 = {
    'Banned':False,
    'Password':'',
    'Strikes':0,
    'Username':'',
}
obj2 = {
    'Banned':False,
    'Password':'',
    'Strikes':0,
    'Username':'',
    }


data = [obj1, obj2]

for record in data:
    doc_ref = db.collection('Accounts').document(record['Username'])
    doc_ref.set(record)

users_ref = db.collection("Accounts")
docs = users_ref.stream()

for doc in docs:
    print(f"{doc.id}'s Strikes => {doc.to_dict()['Strikes']}")