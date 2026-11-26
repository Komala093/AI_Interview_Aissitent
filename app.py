import streamlit as st
from groq import Groq
st.set_page_config(page_title='AI INTERVIEW ASSISTANT',layout='centered')
st.title('AI INTERVIEW ASSISTANT')
st.caption('practice interviews with AI-generated question and constructive feedback.')
st.caption('Ishwariya S')
st.write("Department of AI&DS")

try:
  client=Groq(api_key=st.secrets['GROQ_API_KEY'])
  st.write("API connection sucessful")
except(KeyError,FileNotFoundError):
  st.error('GROQ_API_KEY is missing.Add it to streamlit cloud -->App setting')
  st.stop()
