from langchain_core.tools import StructuredTool
from pydantic import BaseModel, Field

class Multiply_input(BaseModel):
    a: int = Field(description='the first number to multiply')
    b: int = Field(description='the second number to multiply')


def multiply_fnc(a: int, b: int) -> int:
    return a*b

multiply_tool = StructuredTool.from_function(
    func=multiply_fnc,
    description="multipy two numbers",
    args_schema=Multiply_input
)

result = multiply_tool.invoke({'a':5, 'b':6})
print(result)