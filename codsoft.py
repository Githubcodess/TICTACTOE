# Simple Chatbot using if-else conditions

def chatbot():
    print("Hello! I'm a simple chatbot. How can I assist you today?")
    
    while True:
        user_input = input("You: ").lower()  # Convert input to lowercase for easier matching
        
        # Exit condition
        if "exit" in user_input or "bye" in user_input:
            print("Chatbot: Goodbye! Have a great day!")
            break
        
        # Greetings
        elif "hello" in user_input or "hi" in user_input:
            print("Chatbot: Hello! How can I help you?")
        
        # Asking how the chatbot is
        elif "how are you" in user_input:
            print("Chatbot: I'm just a bot, but I'm doing well! How about you?")
        
        # Asking for the time (basic simulation)
        elif "time" in user_input:
            print("Chatbot: Sorry, I can't tell the time right now. Maybe check your phone?")
        
        # Asking for help
        elif "help" in user_input:
            print("Chatbot: I'm here to help! You can ask me simple questions or type 'bye' to exit.")
        
        # Default response for unrecognized queries
        else:
            print("Chatbot: I'm sorry, I didn't understand that. Can you try asking something else?")
    
# Start the chatbot
chatbot()
