import streamlit as st
from pdferchanger import files_handler , file_lister , delete_files , translate
import os
import yaml

def start():
    folders_name = ['-- Select --','game', 'sudoku', 'tictactoe','scramble','hangman']
    selct = st.selectbox('Choose', ['-- Select --','Text to PDF', 'List Files', 'Delete File','Translate File'])
    
    if selct == 'Text to PDF':
        st.write('Text to PDF')
        
        folder_name = st.selectbox('Choose', folders_name)
        if folder_name != '-- Select --':
            uploaded_file = st.file_uploader('Choose a text file', type=['txt','text','text/plain','text/html'],accept_multiple_files=False)
            if uploaded_file is not None:
                src_name = uploaded_file.name
                st.write(src_name)
                files_handler(uploaded_file,src_name,folder_name)
    elif selct == 'List Files':
        st.write('List Files')
        folder_name_se = st.selectbox('Choose', folders_name)
        if folder_name_se != '-- Select --':
            file_lister(folder_name_se)
    elif selct == 'Delete File':
        st.warning('Delete File')
        folder_name_se = st.selectbox('Choose', folders_name)
        delete_files(folder_name_se)

    elif selct == 'Translate File':
        st.warning('Translate File')
        folder_name_se = st.selectbox('Choose', folders_name)
        translate(folder_name_se)



# usr = st.text_input("Username")
# pas = st.text_input("Password", type="password")

# if st.button("Login"):
#     if usr == "admin" and pas == "admin":
#         st.success("Logged in successfully")
#         # Key features selection, just to demonstrate how usernames are passed


        
#     else:
#         st.error("Incorrect Username/Password")

        

import streamlit_authenticator as stauth
with open('config.yaml') as file:
    config = yaml.safe_load(file)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)
st.title("Simple PDF Convert App")
name, authentication_status, username = authenticator.login('Login', 'main')
if authentication_status:
    authenticator.logout('Logout', 'main')
    st.write(f'Welcome *{name}*')
    start()
elif authentication_status is False:
    st.error('Username/password is incorrect')
elif authentication_status is None:
    st.warning('Please enter your username and password')


# st.title("Simple PDF Convert App")
# user = st.text_input('Enter Username')
# password = st.text_input('Enter Password', type='password')
# lo = st.button('Login')
# if lo:
#     if user == 'admin':
#         if password == os.getenv('UI_PASSWORD'):
#             st.success('Logged in successfully')
#             start()
#     else:
#         st.warning('Incorrect Username/Password')
    


