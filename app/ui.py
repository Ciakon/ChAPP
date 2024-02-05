import gradio as gr



def login():
    print("your mother, respectfully")
    random_password = 'e234skdmfAA0'
    print(Password.value)
        


user = 'Gregers'

with gr.Blocks() as startPage:

    username_field = gr.Textbox(interactive=True, placeholder="Username")    


    login_btn = gr.Button("Login")
    login_btn.click(fn=login)



    welcome_user = gr.Textbox(f"Welcome {user}!", container=True, scale=4, type='text')
    Password = gr.Textbox(interactive=True, type='password')







    

    #main_user_textbox.submit(fn = a, inputs=main_user_textbox.value)

startPage.launch(share=True)