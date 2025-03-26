import random
import nltk
from nltk.corpus import wordnet
from nltk.chat.util import Chat, reflections

# Download required NLTK data files (only needed the first time)
nltk.download('wordnet')
nltk.download('omw-1.4')

class TechChatBot:
    def __init__(self):
        self.introductions = [
            "Hello! I’m here to help you with information about electronic devices and the latest technology trends.",
            "Hi there! Ask me anything about electronic gadgets or new technology.",
            "Hey! Need help choosing a gadget or want to learn about new tech? I’m here for you."
        ]

        self.goodbyes = [
            "Goodbye! Let me know if you have more tech questions in the future.",
            "See you! Feel free to return if you need more gadget guidance.",
            "Thanks for chatting! Keep me in mind for tech advice."
        ]

        self.fallback_responses = [
            "I’m not sure I understand. Could you rephrase?",
            "That’s interesting! Can you tell me more?",
            "I’m here to help with technology. Can you clarify your question about devices or trends?"
        ]

        self.responses = {
            r"hi|hello|hey": random.choice(self.introductions),
            r"(.*)(laptop|computer)(.*)": "Laptops have various specs. Are you looking for something specific like a gaming or lightweight laptop?",
            r"(.*)(smartphone|phone|mobile)(.*)": "Smartphones come with a range of features! Are you interested in Android or iPhone models?",
            r"(.*)(tablet|ipad)(.*)": "Tablets are great for productivity and entertainment. Would you like recommendations?",
            r"(.*)(smartwatch|watch)(.*)": "Smartwatches can track health, notifications, and more. Do you have a brand or feature in mind?",
            r"(.*)(camera|dslr)(.*)": "Cameras come in different types, from DSLR to mirrorless. Are you into photography or videography?",
            r"(.*)(latest technology|trends|gadgets)(.*)": "The latest trends include AI in wearables, foldable phones, and AR/VR tech. What would you like to know more about?",
            r"(.*)(bye|goodbye|see you)(.*)": random.choice(self.goodbyes)
        }

    def generate_response(self, message):
        for pattern, response in self.responses.items():
            if nltk.re.search(pattern, message.lower()):
                if callable(response):  # If response is a function, call it
                    return response()
                else:
                    return response
        return random.choice(self.fallback_responses)


# Initialize chatbot
bot = TechChatBot()
print("Tech ChatBot: " + random.choice(bot.introductions))

# Chat loop
while True:
    user_input = input("You: ")
    if "bye" in user_input.lower():
        print("Tech ChatBot:", random.choice(bot.goodbyes))
        break
    print("Tech ChatBot:", bot.generate_response(user_input))
