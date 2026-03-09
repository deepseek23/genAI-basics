from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv
load_dotenv()

from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# initialize model
model = init_chat_model("ollama:gemini-3-flash-preview:cloud")

# request schema
class ParagraphInput(BaseModel):
    paragraph: str

# prompt template
prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """
You are an expert movie information extractor.

Extract the following fields from the paragraph:

- movie_title
- director
- release_year
- genre
- main_cast
- summary

If a field is missing return "Not Available".

Return the result in JSON format.
"""
    ),
    ("human", "{paragraph}")
])


@app.post("/extract")
def extract_movie_info(data: ParagraphInput):
    final_prompt = prompt.format(paragraph=data.paragraph)
    response = model.invoke(final_prompt)

    return {
        "result": response.content
    }