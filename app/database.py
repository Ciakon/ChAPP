import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use a service account.
cred = credentials.Certificate('app/ServiceAccounts.json')

app = firebase_admin.initialize_app(cred)

db = firestore.client()

obj1 = {
    'Banned':False,
    'Password':'1234',
    'Strikes':0,
    'Username':'user1',
}
obj2 = {
    'Banned':False,
    'Password':'5678',
    'Strikes':0,
    'Username':'user2',
    }


data = [obj1, obj2]

for record in data:
    doc_ref = db.collection('Accounts').document(record['Username'])
    doc_ref.set(record)

users_ref = db.collection("Accounts")
docs = users_ref.stream()

for doc in docs:
    print(f"{doc.id}'s Strikes => {doc.to_dict()['Strikes']}")

def get_user(username):
    return

def get_chat():
    return [{"user1" : "hej"}, {"user2" : "dræb dig selv"}]

def upload_message(user, message):
    pass