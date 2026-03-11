from langchain.chat_models import init_chat_model



model = init_chat_model("ollama:gemini-3-flash-preview:cloud")

while True:
    user_input = input('you: ')
    if user_input == 'exit.':
        break

    result = model.invoke(user_input)
    print("ai:", result.content)