import streamlit as st
import pandas as pd
import time
from datetime import time as ts

st.title('upload files app')
st.markdown('---')
images = st.file_uploader("please upload files", type=['jpg','png','pdf'], accept_multiple_files=True)
if images is not None:
    for image in images:
        st.image(image)

value = st.slider('A slider', min_value=20, max_value=300, value=70)
print(value)

st.text_input("enter you course title",max_chars=60)

val1 = st.text_area('Enter text description')

val2 = st.date_input('Enter date')

def converter(value):
    m,s,ms = value.split(':')[0],value.split(':')[1],value.split(':')[2],
    t_s = int(m)*60+int(s)+int(ms)/1000
    return t_s
val=st.time_input('Enter the timer', value=ts(0,0,0))
print(val)
if str(val) is '00:00:00':
    st.write('Please set time')
else:
    sec=converter(str(val))
    bar = st.progress(0)
    pers = sec/100
    progress_status = st.empty()
    for i in range(100):
        bar.progress((i+1))
        progress_status.write(str(i+1)+'%')
        time.sleep(pers)
        

