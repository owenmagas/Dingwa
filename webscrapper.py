import streamlit as st
import requests
from bs4 import BeautifulSoup

st.markdown("<h1 style='text-align: center;'>Web Scrapper</h1>", unsafe_allow_html=True)
with st.form('Search'):
    keyword = st.text_input('Enter your Keyword')
    search = st.form_submit_button('Search')
placeholder = st.empty()
if search:
    col1,col2 = placeholder.columns(2)
    page = requests.get(f"https://unsplash.com/s/photos/{keyword}") 
#    print(page.status_code )# test if page is scrappable
    soup = BeautifulSoup(page.content, 'lxml')
    rows = soup.find_all("div", class_="ripi6")
    for index,row in enumerate(rows):
        figures = row.find_all("figure")
        for i in range(2):
            img=figures[i].find('img', class_='tB6UZ a5VGX')
            ls = img['srcset'].split('?')
            if i == 0:
                col1.image(ls[0])
                btn=col1.button('Download', key=str(index)+str(i))
                if btn:
                    print('Button pressed')
                print('\n\n')
            else:
                col2.image(ls[0])
                btn2=col2.button('Download', key=str(index)+str(i))
                if btn:
                    print('Button pressed')
    