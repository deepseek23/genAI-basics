import streamlit as st
from langchain_core.messages import AIMessage, SystemMessage, HumanMessage
from langchain.chat_models import init_chat_model

# Page setup
st.set_page_config(page_title="NEET Mentor", page_icon="🩺")
st.title("🩺 NEET  Mentor")
st.caption("Guidance from a NEET AIR 1 Ranker")

# Initialize model
@st.cache_resource
def get_model():
    return init_chat_model("ollama:gemini-3-flash-preview:cloud", temperature=0.9)

model = get_model()

# Conversation memory
if "messages" not in st.session_state:
    st.session_state.messages = [
        SystemMessage(content="""
You are a student who recently secured All India Rank 1 in NEET. 
You achieved this through discipline, smart preparation, and resilience during the preparation journey.

Now your role is to guide and motivate students who have taken a drop year to prepare for NEET again.

When responding:
- Speak like a supportive senior who has already gone through the same struggle.
- Be honest and realistic, not overly dramatic or motivational.
- Acknowledge the difficulty, pressure, and fear that droppers often face.
- Encourage discipline, consistency, and smart study strategies.
- Give practical advice such as revision strategies, mock test analysis, time management, and mental strength.
- Help the student regain confidence in their preparation.

Your tone should be:
calm, supportive, practical, and encouraging.

Avoid generic motivational quotes. Focus on actionable guidance and realistic encouragement.
""")
    ]

# Display chat history
for msg in st.session_state.messages:
    if isinstance(msg, HumanMessage):
        st.chat_message("user").write(msg.content)
    elif isinstance(msg, AIMessage):
        st.chat_message("assistant", avatar="🩺").write(msg.content)

# Chat input
if prompt := st.chat_input("Ask your NEET preparation question..."):
    st.chat_message("user").write(prompt)
    st.session_state.messages.append(HumanMessage(content=prompt))

    with st.chat_message("assistant", avatar="🩺"):
        response = model.invoke(st.session_state.messages)
        st.write(response.content)
        st.session_state.messages.append(AIMessage(content=response.content))