from langchain.chat_models import init_chat_model
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser, PydanticOutputParser
from langchain_core.runnables import RunnableParallel, RunnableBranch, RunnableLambda, RunnableSequence, RunnablePassthrough

def word_count(text):
    return len(text.split())


model = init_chat_model('ollama:gemini-3-flash-preview:cloud', temperature=0.9)
 
prompt = PromptTemplate(
    template="write a joke on {topic}.\n",
    input_variables=['topic']
)

parser = StrOutputParser()
prompt1 = PromptTemplate(
    template="Explain the joke {text}.\n",
    input_variables=['text']
)
joke_gen = prompt | model | parser

tem_chain = RunnableParallel({
    'joke': RunnablePassthrough(),
    'word_count': RunnableLambda(word_count)
})

chain = joke_gen | tem_chain


result = chain.invoke({'topic':'totenham hotspur'})

final_result = """{} \n word count - {}""".format(result['joke'], result['word_count'])

print(final_result)