from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader(
    file_path='dl-curriculum.pdf'
)

docs = loader.load()


spliter = CharacterTextSplitter(
    chunk_size=200,
    chunk_overlap=0,
    separator=''
)

var = spliter.split_documents(docs)
print(var[4].page_content)