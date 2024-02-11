#!pip install streamlit
import streamlit as st
import pandas as pd

table = pd.read_excel(r'/Users/owenmagas/Documents/Practice/Dingwa/Ecliar_dataset.xlsx', sheet_name='Years')
st.markdown("""
<style>
.st-emotion-cache-6q9sum.ef3psqc4  
{
visibilt:hidden
}   
</styel>
""", unsafe_allow_html=True)
st.title('I am st webapp')
st.subheader('Hi i am a subheader')
st.header('I am header')
st.text('Hi i am in place of a paragraph from text function')
st.markdown('**Hello** *world*')
st.markdown('# Hello *world*')
st.markdown('[Google](https://www.google.com)')
st.markdown('---')
st.caption('I ma caption')
st.latex(r'\begin{pmatrix}a&b\\c&d\end{pmatrix}')#katex.org for more info
json={'a':"1,2,3",'b':'4,5,6'}
st.json(json)
#display code in the web function
code = """
    print('Hello world')
    def func():
            return 0;"""
st.code(code, language='python')

st.write("## H2")
st.metric(label='Wind Speed', value='120ms⁻¹', delta='-1.4ms⁻¹')
st.table(table)
st.dataframe(table)
st.image('img.jpg.png', caption='myscreen img', width=500)
st.audio('audio.mp3')
st.video('video.mp4')

def change():
    print(st.session_state.checker)
state = st.checkbox('Checkbox', value=True, on_change=change, key='checker')
if state:
    st.write('Hi')
else:
    st.write('not_hi')

radio_btn = st.radio('In which country do you live?', options=('US', 'UK','Canada'))
print(radio_btn)

def btn_clck():
    print('btn clicked')
btn = st.button('click me!', on_click=btn_clck)

select = st.selectbox('What dio you want?', options=('Audi', 'BMW','Benx','Ferrari'))
print(select)

multi_select = st.multiselect('What is your favorite Tech Brand', options=('MICRosoft', 'Apple','amazon','oracle'))