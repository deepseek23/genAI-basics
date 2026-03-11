from langchain_mistralai.chat_models import ChatMistralAI
from dotenv import load_dotenv
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel, Field
load_dotenv()

model = ChatMistralAI(model="ministral-8b-2512",temperature=1)


class Person(BaseModel):

    name:str = Field(description="name of the person")
    age: int = Field(gt=18, description="age of the person")
    city: str = Field(description="name of city where person lives")

parser = PydanticOutputParser(pydantic_object=Person)

template = PromptTemplate(
    template='generate the name, age and city of a fictional {place} person\n {format_instruction}',
    input_variables=['place'],
    partial_variables={'format_instruction':parser.get_format_instructions()}
)

prompt = template.invoke({'place':'Germany'})

result = model.invoke(prompt)
final = parser.parse(result.content)
print(final)