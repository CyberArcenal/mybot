import mybot

while True:
    user_input = input("You: ")
    
    if user_input.lower() == 'exit':
        print("Exiting the chat.")
        break
    
    bot_response = mybot.get_response(user_input)
    print(f"Bot: {bot_response}")
