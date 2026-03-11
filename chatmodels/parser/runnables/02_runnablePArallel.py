from langchain.chat_models import init_chat_model
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser, PydanticOutputParser
from langchain_core.runnables import RunnableParallel, RunnableBranch, RunnableLambda, RunnableSequence

model = init_chat_model('ollama:gemini-3-flash-preview:cloud', temperature=0.9, max_tokens=100)
parser = StrOutputParser()
prompt1 = PromptTemplate(
    template='write a tweet for X on {topic}.',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='write a post for linkedin on {topic}.',
    input_variables=['topic']
)


chain = RunnableParallel({
    'tweet': prompt1 | model | parser,
    'post': prompt2 | model | parser
})

result = chain.invoke({'topic': 'unprotected sex'})
print(result['tweet'])
print(result['post'])

