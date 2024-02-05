import gradio as gr

user = 'Gregers'
random_password = 'e234skdmfAA0'

def login():
    print("your mother, respectfully")
    entered_password = password_field.value
    print(entered_password)
        




with gr.Blocks() as startPage:

    gr.Label("Log-in", show_label=False)

    username_field = gr.Textbox(interactive=True, placeholder="Username", show_label=False)
    password_field = gr.Textbox(interactive=True, placeholder="Password", show_label=False, type='password')

    login_btn = gr.Button("Login")
    login_btn.click(fn=login)



    welcome_user = gr.Textbox(f"Welcome {user}!", container=True, scale=4, type='text', visible=False)
    







    

    #main_user_textbox.submit(fn = a, inputs=main_user_textbox.value)

startPage.launch(share=True)