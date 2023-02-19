import streamlit as st
from pdferchanger import files_handler , file_lister , delete_files , translate
import os


def start():
    password = st.text_input('Enter Password', type='password')
    user = st.text_input('Enter Username')
    if user == 'admin' and password == os.getenv('UI_PASSWORD'):
        st.success('Logged in successfully')
    else:
        st.warning('Incorrect Username/Password')
        start()
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

        

    

st.title("Simple PDF Convert App")
start()
