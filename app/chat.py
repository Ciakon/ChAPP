import database as db
import tisane as ts
import time

current_message_id = 0
current_user_data = None



def login():
    global current_user_data
    print("---------------login---------------")
    #while not logged in
    logged_in = False
    while not logged_in:

        entered_username = db.get_user(input('username: '))
        entered_password = input('password: ')

        if(entered_username and entered_username['Password']==entered_password):
            current_user_data = entered_username
            print("Login success :)")
            logged_in = True

        else:
            print('username or password is incorrect')
        

def start_chat():
    global current_message_id

    chat_history = db.get_chat()

    print("\n\n----------------chat---------------")
    for message in chat_history:
        print(f"{message['user']}: {message['content']}\n")
        current_message_id = message["id"]

def update_chat():
    global current_message_id

    chat_history = db.get_chat()
        
    message_position = 0

    chat_length = len(chat_history)

    for i in range(chat_length-1, -1, -1):
        print(i)
    
        message_id = chat_history[i]["id"]

        # start sending message, after last message in client
        if message_id == current_message_id:
            message_position = i + 1

    if message_position > chat_length:
        return
    
    for i in range(message_position, chat_length):
        content = chat_history[i]["content"]
        user = chat_history[i]["user"]
        current_message_id = chat_history[i]["id"]

        print(f"{user}: {content}\n")
        


login()
    

start_chat()

typing = True
local_strikes=0

while typing:
    update_chat()
    time.sleep(0.05)
    message = input(f"{current_user_data['Username']}: ")
    abuse, reasons = ts.get_abuse(message)
    if (current_user_data["Banned"]):
        print ("You have been banned, because you continuesly have written abusive messages, and your message has not been sent.")
    else:
        if (not abuse):
            db.upload_message(current_user_data['Username'], message)
        else:
            print(f"Your message has been blocked, because of the following: {reasons}.\nYou now have {current_user_data['Strikes']} strike(s).")
            local_strikes += 1
            db.update_user(local_strikes)
    
        











