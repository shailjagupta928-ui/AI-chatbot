from dotenv import load_dotenv
load_dotenv()

import streamlit as st
from langchain_mistralai import ChatMistralAI
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage



col1, col2 = st.columns([5, 1])
col1.title("🤖 MoodBot")
if col2.button("🗑️ Clear"):
    st.session_state.messages = []

MODES = {"😂 Funny": "you are a funny ai chatbot",
         "😤 Angry": "you are an angry ai chatbot",
         "😢 Sad":   "you are a sad ai chatbot"}

mode = st.radio("Pick a mood:", list(MODES.keys()), horizontal=True)

if "messages" not in st.session_state or st.session_state.get("mode") != mode:
    st.session_state.messages, st.session_state.mode = [], mode

for m in st.session_state.messages:
    st.chat_message("user" if isinstance(m, HumanMessage) else "assistant").write(m.content)

if prompt := st.chat_input("Say something..."):
    st.session_state.messages.append(HumanMessage(content=prompt))
    st.chat_message("user").write(prompt)

    response = ChatMistralAI(model="mistral-small-2506", temperature=0.7).invoke(
        [SystemMessage(content=MODES[mode])] + st.session_state.messages)

    st.session_state.messages.append(AIMessage(content=response.content))
    st.chat_message("assistant").write(response.content)