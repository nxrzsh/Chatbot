class RuleBasedChatbot:
    def generate_response(self, user_input):
        # Convert user input to lowercase for case-insensitive matching
        user_input_lower = user_input.lower()

        # Simple pattern matching using if-else conditions
        if 'hello' in user_input_lower or 'hi' in user_input_lower or 'hey' in user_input_lower:
            return 'Hello! How can I help you?'
        elif 'how are you' in user_input_lower:
            return 'I am just a machine, but thanks for asking!'
        elif 'your name' in user_input_lower:
            return 'I am a chatbot. You can call me ChatGPT.'
        elif 'bye' in user_input_lower or 'goodbye' in user_input_lower:
            return 'Goodbye! Have a great day.'
        elif 'help' in user_input_lower:
            return 'I can assist you with general information. Feel free to ask anything!'
        else:
            return 'I am sorry, I do not understand that.'

# Example usage
chatbot = RuleBasedChatbot()

while True:
    user_input = input('You: ')
    if user_input.lower() == 'exit':
        print('Chatbot: Goodbye!')
        break
    response = chatbot.generate_response(user_input)
    print('Chatbot:', response)