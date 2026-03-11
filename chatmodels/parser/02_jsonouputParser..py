from langchain.chat_models import init_chat_model
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from dotenv import load_dotenv

load_dotenv()

# Initialize model
model = init_chat_model("groq:llama-3.1-8b-instant", temperature=1.6)

parser = JsonOutputParser()

template = PromptTemplate(
    template="write 5 facts about {topic}.\n{format_instruction}",
    input_variables=['topic'],
    partial_variables={"format_instruction": parser.get_format_instructions()}
)

chain = template | model | parser
result = chain.invoke({'topic':'spainish football'})
print(result)