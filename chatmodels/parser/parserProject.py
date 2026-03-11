# this will help to understand of extraction of paragraph in a structured way
from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import Field, BaseModel
from typing import Optional

model = init_chat_model("ollama:kimi-k2.5:cloud")


class Extraction(BaseModel):
    name: str = Field(description="name of the movie")
    director: str = Field(description="director of the movie")
    cast: str = Field(description="cast of the move")
    rating: Optional[float] = Field(description="rating of the movie")
    genre: str = Field(description="genre of the movie")
    released_year: int = Field(description="released year of the movie")
    summary: str = Field(description="2 line summary of the movie")
    
parser = PydanticOutputParser(pydantic_object=Extraction)

template = ChatPromptTemplate.from_messages([
    ('system','extract the information from the paragraph.\n{format_instruction}'),
    ('human','{paragraph}')
])

para = input("enter your msg")

chain = template | model | parser
result = chain.invoke({'paragraph':para,
              'format_instruction':parser.get_format_instructions()})
result = result.model_dump_json()
print("your output is : \n",result)
print(type(result))



