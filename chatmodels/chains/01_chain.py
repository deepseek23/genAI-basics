from langchain.chat_models import init_chat_model
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser


model = init_chat_model("ollama:kimi-k2.5:cloud")

template = PromptTemplate(
    template="give 5 facts of {topic}\n ",
    input_variables=['topic']
)
parser = StrOutputParser()


chain = template | model | parser
result = chain.invoke({'topic':'English first division football'})
print(result)

chain.get_graph().print_ascii()