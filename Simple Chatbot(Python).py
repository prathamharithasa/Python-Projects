import datetime
import pytz
import random

# Timezone set to Singapore
singapore_tz = pytz.timezone("Asia/Singapore")

# Predefined responses
simple_responses = {
    "hi": "Hello! How can I help you today?",
    "hello": "Hi there! What can I do for you?",
    "how are you": "I'm just a bot, but I'm doing great!",
    "what is your name": "I'm Chatpy, your Python chatbot!",
    "who made you": "I was created by a student using Python!",
    "bye": "Goodbye! Have a great day!",
    "thank you": "You're welcome!",
    "thanks": "No problem!",
}

# Chat history and user data
chat_history = []
user_profile = {
    "name": "",
    "messages_sent": 0
}

# Predefined joke list
jokes = [
    "Why did the computer go to the doctor? Because it had a virus!",
    "Why do programmers prefer dark mode? Because the light attracts bugs!",
    "Why did the robot go on vacation? Because it needed to recharge!"
]

# Function to greet user
def greet_user():
    print("Hello! I'm Chatpy, your friendly Python chatbot.")
    name = input("What's your name? ")
    print(f"Nice to meet you, {name}!")
    user_profile["name"] = name
    return name

# Function to get current time in Singapore
def get_current_time():
    now = datetime.datetime.now(singapore_tz)
    return now.strftime("%I:%M %p")

# Function to get current date in Singapore
def get_current_date():
    now = datetime.datetime.now(singapore_tz)
    return now.strftime("%A, %d %B %Y")

# Help menu
def show_help():
    return (
        "Here are some things you can ask me:\n"
        "- What is the time?\n"
        "- What is the date?\n"
        "- Tell me a joke\n"
        "- Tell me the weather\n"
        "- Ask a math question (e.g. what is 5 + 2)\n"
        "- Count characters or words in a sentence\n"
        "- Play a quiz\n"
        "- Say 'bye' to end the chat"
    )

# Simulated weather
def get_weather():
    weather_options = [
        "It's sunny and bright in Singapore.",
        "Looks like it's going to rain. Take an umbrella!",
        "It's cloudy and cool outside.",
        "The weather is humid as usual in Singapore."
    ]
    return random.choice(weather_options)

# Math processor
def evaluate_math(expression):
    try:
        result = eval(expression)
        return f"The answer is {result}"
    except:
        return "Sorry, I couldn't understand the math question."

# Word counter
def count_words(sentence):
    count = len(sentence.split())
    return f"There are {count} words."

# Character counter
def count_characters(sentence):
    count = len(sentence)
    return f"There are {count} characters."

# Quiz with multiple categories
def quiz():
    print("Choose a quiz category:")
    print("1. General Knowledge")
    print("2. Math")
    print("3. Science")

    choice = input("Enter 1, 2, or 3: ").strip()

    if choice == "1":
        questions = [
            ("What is the capital of Japan?", "tokyo"),
            ("Which planet is known as the Red Planet?", "mars"),
            ("How many continents are there?", "7")
        ]
        category = "General Knowledge"
    elif choice == "2":
        questions = [
            ("What is 8 x 7?", "56"),
            ("What is the square root of 81?", "9"),
            ("What is 100 divided by 4?", "25")
        ]
        category = "Math"
    elif choice == "3":
        questions = [
            ("What gas do plants use to make food?", "carbon dioxide"),
            ("What part of the body pumps blood?", "heart"),
            ("What is H2O also known as?", "water")
        ]
        category = "Science"
    else:
        return "Invalid choice. Please enter 1, 2, or 3 next time."

    print(f"\nStarting {category} Quiz!\n")
    score = 0

    for q, a in questions:
        ans = input(q + " ").lower()
        if ans == a:
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Oops! The correct answer is: {a}")

    return f"\nYou got {score} out of {len(questions)} correct in the {category} quiz!"


# Main input processor
def process_input(user_input):
    user_input = user_input.lower().strip()
    user_profile["messages_sent"] += 1

    if "time" in user_input:
        return f"The current time is {get_current_time()}."

    elif "date" in user_input or "day" in user_input:
        return f"Today's date is {get_current_date()}."

    elif "help" in user_input:
        return show_help()

    elif "weather" in user_input:
        return get_weather()

    elif "joke" in user_input:
        return random.choice(jokes)

    elif "i am sad" in user_input or "i'm sad" in user_input:
        return "I'm here for you. It's okay to feel sad sometimes."

    elif "i am happy" in user_input or "i'm happy" in user_input:
        return "Yay! I'm happy you're happy!"

    elif "how many words in" in user_input:
        start = user_input.find('"')
        end = user_input.rfind('"')
        if start != -1 and end != -1 and start < end:
            sentence = user_input[start + 1:end]
            return count_words(sentence)
        else:
            return "Use quotes like: how many words in \"hello world\""

    elif "how many characters in" in user_input:
        start = user_input.find('"')
        end = user_input.rfind('"')
        if start != -1 and end != -1 and start < end:
            sentence = user_input[start + 1:end]
            return count_characters(sentence)
        else:
            return "Use quotes like: how many characters in \"hello world\""

    elif "what is" in user_input:
        parts = user_input.replace("what is", "").strip()
        return evaluate_math(parts)

    elif "quiz" in user_input:
        return quiz()

    for keyword in simple_responses:
        if keyword in user_input:
            return simple_responses[keyword]

    return "I'm sorry, I don't understand that. Type 'help' to see what I can do."

# Summary at the end
def show_summary():
    print("\nChat Summary:")
    print("Name:", user_profile["name"])
    print("Total messages sent:", user_profile["messages_sent"])
    print("Thanks for chatting with Chatpy!")

# Main chat loop
def start_chat():
    greet_user()
    print("\nYou can start chatting now! Type 'help' if you're not sure what to say.\n")

    while True:
        user_message = input("You: ")
        response = process_input(user_message)
        print("Chatpy:", response)

        chat_history.append((user_message, response))

        if "bye" in user_message.lower():
            break

    show_summary()

# Run the chatbot
start_chat()
