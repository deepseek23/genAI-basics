from langchain.chat_models import init_chat_model
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

# Initialize model
model = init_chat_model("groq:llama-3.1-8b-instant", temperature=0.4)

# 1. Detailed report
template_1 = PromptTemplate(
    template="write a 5 line report on {topic}",
    input_variables=["topic"]
)

# 2. Summary
template_2 = PromptTemplate(
    template="Summarize the following report in concise points:\n{text}",
    input_variables=["text"]
)

parser = StrOutputParser()

# Chain
chain = template_1 | model | parser | (lambda x: {"text": x}) | template_2 | model | parser

# Run
result = chain.invoke({"topic": "black hole"})
print(result)