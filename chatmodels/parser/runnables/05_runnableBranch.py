from langchain.chat_models import init_chat_model
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableBranch, RunnableLambda, RunnablePassthrough

model = init_chat_model('ollama:gemini-3-flash-preview:cloud', temperature=0.9)

parser = StrOutputParser()

prompt = PromptTemplate(
    template="generate a detailed report on {topic}.",
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template="summarize the given \n{text}.",
    input_variables=['text']
)

report_gen = prompt | model | parser

temp_chain = RunnableBranch(
    (lambda x: len(x.split()) > 300,
     RunnableLambda(lambda x: {"text": x}) | prompt2 | model | parser),
    RunnablePassthrough()
)

final_chain = report_gen | temp_chain

print(final_chain.invoke({'topic': 'Russia vs Ukraine'}))