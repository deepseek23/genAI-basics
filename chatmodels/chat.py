from dotenv import load_dotenv
load_dotenv()
from langchain_core.prompts import PromptTemplate

from langchain.chat_models import init_chat_model

model = init_chat_model(
    "ollama:gpt-oss:120b-cloud",
    temperature=0.7,
    max_tokens=50
)

template_1 = PromptTemplate(
    template="write a detailed report on {topic}",
    input_variables={'topic'}
)
# 2 summary
template_2 = PromptTemplate(
    template="write a summary on following text.\n {text}",
    input_variables={'text'}
)

prompt_1 = template_1.invoke({'topic': 'black hole'})

result = model.invoke(prompt_1)

prompt_2 = template_2.invoke({'text': result.content})

result2 = model.invoke(prompt_2)
print(result2.content)