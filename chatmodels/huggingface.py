from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

load_dotenv()

# HuggingFace API model
llm = HuggingFaceEndpoint(
    repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    max_new_tokens=1000
)

model = ChatHuggingFace(llm=llm)

# 1st prompt detailed report
template_1 = PromptTemplate(
    template="write a detailed report on {topic}",
    input_variables=["topic"]
)

# 2nd prompt summary
template_2 = PromptTemplate(
    template="write a summary on following text.\n{text}",
    input_variables=["text"]
)

# First prompt
prompt_1 = template_1.invoke({"topic": "black hole"})
result = model.invoke(prompt_1)

# Second prompt
prompt_2 = template_2.invoke({"text": result.content})
result2 = model.invoke(prompt_2)

print(result2.content)