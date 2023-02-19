from datetime import datetime
import streamlit as st
from fpdf import FPDF 
from tran import translatorit
import os




    
    

def pdf_impl(uploaded_file,src_name,folder_resulsts):
    pdf = FPDF()      
    pdf.add_page()  
    pdf.set_font("Arial", size = 15)
    
    file_path = f'{folder_resulsts}/{uploaded_file.name}'

    _src_name = src_name.replace('.txt','')
    dst = f'{folder_resulsts}/{_src_name}.pdf'

    if st.button('Convert + Upload'):
        with open(file_path, 'w+') as f:
            f.writelines(str(uploaded_file.read()))
            st.success('File Uploaded')
        f = open(file_path, "r")
        for x in f: 
            pdf.cell(50,5, txt = x, ln = 1, align = 'C') 
        pdf.output(dst)
        st.success('File Converted')
  


def files_handler(uploaded_file,src_name,folder_name):
    folder_resulsts = f'data/{folder_name}'
    if os.path.exists(folder_resulsts):
        pdf_impl(uploaded_file,src_name,folder_resulsts)
    else:
        os.mkdir(folder_resulsts)
        pdf_impl(uploaded_file,src_name,folder_resulsts)

def file_lister(folder_name_se):
    folder_resulsts = f'data/{folder_name_se}'
    if os.path.exists(folder_resulsts):
        liter_text = []
        liter_pdf  = []
        liter = os.listdir(folder_resulsts)
        for i in liter:
            if i.lower().endswith('.pdf'):
                liter_pdf.append(i)
            else:
                liter_text.append(i)
        sel = st.selectbox('Choose',liter_text )
        if st.button('Show'):
            fo = f'{folder_resulsts}/{sel}'
            f = open(fo,'r', encoding='utf8') 
            for i in f:
                st.write(i)
        sel = st.selectbox('Choose',liter_pdf )
        if sel:
            folder_resulsts += f'/{sel}'
            _open = open(folder_resulsts, 'rb')
            st.download_button(label='Download', data=_open, file_name=f'{folder_resulsts}', mime='application/pdf')
    else:
        st.warning('Folder is empty')

def delete_files(folder_name_se):
    folder_resulsts = f'data/{folder_name_se}'
    if os.path.exists(folder_resulsts):
        liter = os.listdir(folder_resulsts)
        ch = st.selectbox('Choose',liter )
        if st.button('Delete',):
            folder_resulsts += f'/{ch}'
            os.remove(folder_resulsts)
            st.error(f'File Deleted {ch}')
            with open('audit_logs.log', 'a') as f:
                f.writelines(f'{datetime.now()} - {ch} Deleted')
    else:
        st.warning('Folder is empty')


def translate(folder_name_se):
    folder_resulsts = f'data/{folder_name_se}'
    if os.path.exists(folder_resulsts):
        liter_text = []
        liter_pdf  = []
        liter = os.listdir(folder_resulsts)
        for i in liter:
            if i.lower().endswith('.pdf'):
                liter_pdf.append(i)
            else:
                liter_text.append(i)
        sel = st.selectbox('Choose',liter_text )
        if st.button('Show'):
            fo = f'{folder_resulsts}/{sel}'
            f = open(fo,'r', encoding='utf8') 
            for i in f:
                st.write(i)
    
        to  = st.multiselect('Choose',['de','fr','es','it','he','ar'])
        fo = f'{folder_resulsts}/{sel}'
        with open(fo,'r', encoding='utf8') as f:
            data = f.read()
        if st.button('Translate'):
    
            translatorit(data,to,translate_path=fo)
    else:
        st.warning('Folder is empty')