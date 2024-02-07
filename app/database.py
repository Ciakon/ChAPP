import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import random


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


# data = [obj1, obj2]

# for record in data:
#     doc_ref = db.collection('Accounts').document(record['Username'])
#     doc_ref.set(record)



# for doc in docs:
#     print(f"{doc.id}'s Strikes => {doc.to_dict()['Strikes']}")

def get_user(Username):
    users_ref = db.collection("Accounts")
    docs = users_ref.stream()
        
    for doc in docs:
        user = doc.to_dict()

        if user["Username"] == Username:
            return user
        
    return False

def get_chat():
    
    return [{"user" : "user1", "content": "hej", "id" : 141340}, {"user" : "user2", "content": "L", "id" : 15380}]

def upload_message(user, message):
    message_id = random.randint(10000000, 99999999)
    data = {"user" : user, "content" : message, "id" : message_id}
    doc_ref = db.collection('Chat').document("Chat")
    doc_ref.update({"History": firestore.ArrayUnion([data])})

upload_message("user1", "OOFT")


def update_user(strikes):

    # data = [obj1, obj2]

    # for record in data:
    #     doc_ref = db.collection('Accounts').document(record['Username'])
    #     doc_ref.set(record)


    if strikes >= 3:
        banned =True

    pass

get_user("Noah")