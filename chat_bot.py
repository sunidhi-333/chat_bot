import google.generativeai as genai
import os
from dotenv import load_dotenv

class GeminiChat:
    def __init__(self):
        """Initialize the Gemini chat interface"""
        # Load environment variables
        load_dotenv()
        
        # Get API key from environment variable
        api_key = os.getenv('GOOGLE_API_KEY')
        if not api_key:
            raise ValueError("Please set GOOGLE_API_KEY environment variable")
            
        # Configure the Gemini API
        genai.configure(api_key=api_key)
        
        # Create the model instance
        self.model = genai.GenerativeModel('gemini-1.0-pro')
        
        # Start a new chat session
        self.chat = self.model.start_chat(history=[])

    def get_response(self, prompt):
        
        try:
            response = self.chat.send_message(prompt)
            return response.text
        except Exception as e:
            return f"Error generating response: {str(e)}"

    def reset_chat(self):
        self.chat = self.model.start_chat(history=[])

def main():
    try:
        chat_bot = GeminiChat()
        
        print("Gemini Chat initialized! (Type 'quit' to exit, 'reset' to start new chat)")
        
        while True:
            user_input = input("\nYou: ").strip()
            
            if user_input.lower() == 'quit':
                break
            elif user_input.lower() == 'reset':
                chat_bot.reset_chat()
                print("Chat history reset!")
                continue
            
            if user_input:
                response = chat_bot.get_response(user_input)
                print("\nGemini:", response)

    except Exception as e:
        print(f"Error initializing chat: {str(e)}")

if __name__ == "__main__":
    main()