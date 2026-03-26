from langchain_core.tools import tool

@tool
def multiply(a: int, b: int) -> int:
    """multiply a and b values"""
    return a*b

print(multiply.invoke({'a':5, 'b':6}))