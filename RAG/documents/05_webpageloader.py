from langchain_community.document_loaders import WebBaseLoader
from langchain_core.prompts import PromptTemplate
from langchain.chat_models import init_chat_model
from langchain_core.output_parsers import StrOutputParser

model = init_chat_model('ollama:gemini-3-flash-preview:cloud', temperature=0.4)
parser = StrOutputParser()

prompt = PromptTemplate(
    template="answer the following question \n {question} from the following text \n {text}",
    input_variables=['question', 'text']
)

url = 'https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html'
loader = WebBaseLoader(url)
docs = loader.load()

chain = prompt | model | parser
final = chain.invoke({'question':'what is pipeline ?',
                      'text':docs[0].page_content})
print(final)