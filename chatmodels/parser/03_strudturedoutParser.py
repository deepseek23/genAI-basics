# its depriciated structured output parser and i wasted 30 mins on it ):

from langchain_mistralai.chat_models import ChatMistralAI
from dotenv import load_dotenv
from langchain.output_parsers import StructuredOutputParser, ResponseSchema
from langchain_core.prompts import PromptTemplate

load_dotenv()

model = ChatMistralAI(model="mistral-small-latest")

schema = [
    ResponseSchema(name='fact_1', description='fact 1 on the topic'),
    ResponseSchema(name='fact_2', description='fact 2 on the topic'),
    ResponseSchema(name='fact_3', description='fact 3 on the topic'),
]
parser = StructuredOutputParser.from_response_schemas(schema)

template = PromptTemplate(
    template="give 3 about the {topic}.\n {format_instruction}",
    input_variables=['topic'],
    partial_variables={'format_instruction':parser.get_format_instructions()}
)

prompt = template.invoke({'topic':'Formula 1'})

result = model.invoke(prompt)
final_result = parser.parse(result.content)
print(result)