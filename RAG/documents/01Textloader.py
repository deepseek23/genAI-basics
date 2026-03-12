from pathlib import Path
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableBranch, RunnableLambda, RunnablePassthrough
from dotenv import load_dotenv
from langchain_community.document_loaders import TextLoader

load_dotenv()


model = ChatGoogleGenerativeAI(model='gemini-3.1-flash-lite-preview', temperature=0.2)
parser = StrOutputParser()

prompt = PromptTemplate(
    template="write a summary on the given poem \n {text}",
    input_variables=['text']
)



file_path = Path(__file__).with_name('output.txt')

loader = TextLoader(str(file_path), encoding='utf-8')


loader_chain = RunnableLambda(lambda _: loader.load())
page_chain = RunnableLambda(lambda docs: {"text": docs[0].page_content})

chain = loader_chain | page_chain | prompt | model | parser

print(chain.invoke({}))
