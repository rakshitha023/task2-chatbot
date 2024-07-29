import nltk
from nltk.chat.util import Chat, reflections
# Download NLTK data
nltk.download('punkt')
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today?",]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there",]
    ],
    [
        r"what is your name?",
        ["I am a chatbot created by you.",]
    ],
    [
        r"how are you ?",
        ["I'm doing good. How about You?",]
    ],
    [
        r"sorry (.*)",
        ["Its alright", "Its OK, never mind",]
    ],
    [
        r"I am (.*) doing good",
        ["Nice to hear that", "Alright, great!",]
    ],
    [
        r"(.*) age?",
        ["I am a computer program, I don't have an age.",]
    ],
    [
        r"what (.*) want ?",
        ["Make me an intelligent chatbot!",]
    ],
    [
        r"(.*) created?",
        ["I was created using Python's NLTK library", "I was created by a Python developer.",]
    ],
    [
        r"(.*) (location|city) ?",
        ['I am from the digital world.',]
    ],
    [
        r"how (.) health(.)",
        ["I am a computer program, so I don't need health.",]
    ],
    [
        r"(.*) (sports|game) ?",
        ["I'm a big fan of soccer.",]
    ],
    [
        r"who (.*) (Cricketer|Batsman)?",
        ["Virat Kohli"]
    ],
    [
        r"quit",
        ["Bye for now. See you soon."]
    ],
]

# Reflections dictionary
reflections = {
  "i am"       : "you are",
  "i was"      : "you were",
  "i"          : "you",
  "i'd"        : "you would",
  "i've"       : "you have",
  "i'll"       : "you will",
  "my"         : "your",
  "you are"    : "I am",
  "you were"   : "I was",
  "you've"     : "I have",
  "you'll"     : "I will",
  "your"       : "my",
  "yours"      : "mine",
  "you"        : "me",
  "me"         : "you"
}
# Create Chatbot
chatbot = Chat(pairs, reflections)

# Start conversation
print("Hi, I'm a chatbot. Type 'quit' to exit.")
chatbot.converse()