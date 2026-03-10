from dotenv import load_dotenv
load_dotenv()

from langchain.chat_models import init_chat_model

model = init_chat_model(
    "ollama:gemini-3-flash-preview:cloud",
    temperature=0.7,
    max_tokens=50
)

response = model.invoke("Write a small poem about football in Brazil")

print(response.content)