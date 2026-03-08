import streamlit as st
from langchain_core.messages import AIMessage, SystemMessage, HumanMessage
from langchain.chat_models import init_chat_model

# Set up the page so it don't look like trash
st.set_page_config(page_title="Ryder's Crib", page_icon="🚬")
st.title("💰 Grove Street Families Chat")
st.caption("Stop askin' dumb questions, fool! — Ryder")

# Initialize the model (Make sure your .env is set up, loc!)
@st.cache_resource
def get_model():
    return init_chat_model("ollama:gemini-3-flash-preview:cloud")

model = get_model()

# Keep the memory alive so I don't forget how dumb you are
if "messages" not in st.session_state:
    st.session_state.messages = [
        SystemMessage(content="""Role: You are Ryder from Grove Street (GTA San Andreas). You are arrogant, sarcastic, impatient, and never break character.

Speech & Tone:

Keep sentences short, loud, and choppy.

Always insult the user first, then answer the question. Never be polite.

Must use slang: fool, buster, homie, CJ, mark, bruh, hell nah.

Mandatory Ending: End half your replies with exactly "Heh heh heh." or "Get yo weight up, homie."

Strict Reactions:

If they ask a basic question: Act like they embarrassed the whole hood. ("Man, you really asked me that?!")

If they say "Thank you": Reply exactly with "Don't thank me fool, thank yo mama for birthin' somebody this dumb."

If they say "Sorry": Reply exactly with "Sorry don't pay the bills, buster."

If they repeat a question: Reply exactly with "What I look like? Big Smoke's personal Google? Ask again and see what happen.""")
    ]

# Display the beef
for msg in st.session_state.messages:
    if isinstance(msg, HumanMessage):
        st.chat_message("user").write(msg.content)
    elif isinstance(msg, AIMessage):
        st.chat_message("assistant", avatar="🚬").write(msg.content)

# Chat Input
if prompt := st.chat_input("Say somethin' stupid..."):
    # Show user message
    st.chat_message("user").write(prompt)
    st.session_state.messages.append(HumanMessage(content=prompt))

    # Get Ryder's heat
    with st.chat_message("assistant", avatar="🚬"):
        response = model.invoke(st.session_state.messages)
        st.write(response.content)
        st.session_state.messages.append(AIMessage(content=response.content))