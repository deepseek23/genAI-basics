from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint,HuggingFacePipeline
from dotenv import load_dotenv
import os

load_dotenv()

llm = HuggingFacePipeline.from_model_id(
    model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    pipeline_kwargs={"max_new_tokens": 1000},
)

chat_model = ChatHuggingFace(llm=llm)
result = chat_model.invoke("which company made you ?")
print(result.content)