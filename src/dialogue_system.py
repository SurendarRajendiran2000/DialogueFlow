from nlp_processing import process_input


def chat():
    print("Bot: Hi there! What can I do for you?")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Bot: Goodbye!")
            break
        processed_input = process_input(user_input)
        response = None
        for keyword in dialogue_flow:
            if keyword in processed_input:
                response = dialogue_flow[keyword]
                break
        if response:
            print("Bot:", response)
        else:
            print("Bot: Sorry, I didn't understand that. Can you please rephrase?")

dialogue_flow = {
    "hello": "Hi there! How can I help you?",
    "how are you": "I'm a computer program, so I don't have feelings, but thanks for asking!",
    "bye": "Goodbye! If you have more questions, feel free to ask."
}
