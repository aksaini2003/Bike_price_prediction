
#if want to deploy it on the render then we have to give the start command as follows 
#streamlit run app.py --server.port $PORT --server.address 0.0.0.0


import streamlit as st 

st.title("This is My First Website ") #for creating the header 

st.header('hello this is header ')
st.subheader('hello i am subheader')
st.text('''

        hello my name is aashish kumar saini
         i live in alwar rajasthan ''')  #this will print the text as it is 
st.write("""this print the string 
         in a 
         a 
         sequence 
         """)  #this will print in a line
st.caption('i am caption')
st.markdown('I am Markdown')
st.latex('I am latex')
