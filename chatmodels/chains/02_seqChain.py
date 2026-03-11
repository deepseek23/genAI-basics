from langchain.chat_models import init_chat_model
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser


model = init_chat_model("ollama:gemini-3-flash-preview:cloud", temperture=0.7)


prompt1 = PromptTemplate(
    template="write a detailed report on {topic}\n",
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template="write a summary on given {text}\n",
    input_variables=['text']
)

parser = StrOutputParser()

chain = prompt1 | model | parser | prompt2 | model | parser

final = chain.invoke({'topic':'Self Attention Mechanism developed by Google Brain'})
print(final)
chain.get_graph().print_ascii()