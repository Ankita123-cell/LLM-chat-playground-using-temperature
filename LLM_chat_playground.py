from langchain_openai import ChatOpenAI
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.messages import HumanMessage
from dotenv import load_dotenv
import os
import pandas as pd
import streamlit as st

load_dotenv()
# hf_token = os.getenv("HUGGINGFACEHUB_API_TOKEN")
do_sample=True
Task_temperature_map = {
    "Summarization":0.3,
    "Email Drafting":0.5,
    "Brainstorming":0.8,
    "Requirement Writing":0.6,
    "SQL Help":0.2
}
temp_compare = [0.2,0.6,1.2]
st.title("LLM Chat Playground with Temperature")
# model_input = st.selectbox("Select Model Name",["Llama","ChatGpt"])
# temperature_input = st.number_input("Enter temperature parameter")
Mode = st.radio(
    "Select Temperature Mode",
    ["Select temperature","Select task type for auto suggestion"]
)
if Mode == "Select temperature":
   st.markdown("Adjust the model response style using temperature")
   temperature_input = st.selectbox("Select temperature range",["Low Temperature (0.0-0.3)","Moderate Temperature (0.4-0.8)","High Temperature (0.9-1+)"])
   if temperature_input == "Low Temperature (0.0-0.3)":
      temperature_input1 = 0.2
   elif temperature_input == "Moderate Temperature (0.4-0.8)":
      temperature_input1 = 0.6
   elif temperature_input == "High Temperature (0.9-1+)":
      temperature_input1 = 1.2
if Mode == "Select task type for auto suggestion":
   st.markdown("Select task type for automated suggestions")
   task_type_input = st.selectbox("Task Type",["Summarization","Email Drafting","Brainstorming","Requirement Writing","SQL Help"])
   suggested_temp = Task_temperature_map[task_type_input]
   temperature_input1 = st.slider("Temperature",min_value=0.0,max_value=1.2,value=suggested_temp,step=0.1)
# max_new_tokens_input = st.number_input("Enter temperature parameter")
user_input = st.text_input('Enter your prompt')
#if model_input == "ChatGpt":
model = ChatOpenAI(model="gpt-4o-mini", temperature=temperature_input1)
#elif model_input == "Llama":
#    llm = HuggingFaceEndpoint(
#    repo_id='Tinyllama/TinyLlama-1.1B-Chat-v1.0',
#    huggingfacehub_api_token=hf_token,
#    task='text-generation',
#    temperature=float(temperature_input) if temperature_input > 0 else 0.1,
#        max_new_tokens=100,
#        do_sample=True
#    )
#    model = ChatHuggingFace(llm=llm)
st.subheader("Response basis selected temperature")
if st.button('Answer'):
    if user_input:
        formatted_input = [HumanMessage(content=user_input)]
    result = model.invoke(formatted_input)
    st.write(result.content)
st.subheader("Compare results for different temperature values")
if st.button('Compare'):
    # st.markdown("Results of three temperature values 0.2 , 0.6 , 1.2 compared are")
    if user_input:
        formatted_input = [HumanMessage(content=user_input)]
    for i in range(0,3):
        temperature_input1 = temp_compare[i]
        st.write(f"Temperature is {temperature_input1}")
        result = model.invoke(formatted_input)
        st.write(result.content)