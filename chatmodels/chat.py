from dotenv import load_dotenv

load_dotenv()
from langchain.chat_models import init_chat_model

model = init_chat_model("ollama:deepseek-v3.1:671b-cloud")
response = model.invoke("write a story. ")
print(response.content)