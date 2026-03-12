from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableBranch, RunnableLambda, RunnablePassthrough
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader


load_dotenv()


model = ChatGoogleGenerativeAI(model='gemini-3.1-flash-lite-preview', temperature=0.2)
parser = StrOutputParser()



loader = PyPDFLoader('new.pdf')

docs = loader.load()
print(len(docs))
print(docs[0].page_content)
print(docs[0].metadata)


