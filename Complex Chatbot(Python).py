import datetime
import pytz
import random
import requests
import html

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

# Store seen joke IDs to avoid repeats
seen_joke_ids = set()

# Jokes using API
def get_programming_joke():
    try:
        response = requests.get("https://official-joke-api.appspot.com/jokes/programming/ten")
        jokes = response.json()
        for joke in jokes:
            joke_id = joke["id"]
            if joke_id not in seen_joke_ids:
                seen_joke_ids.add(joke_id)
                return f"{joke['setup']} — {joke['punchline']}"
        return "I've already told you all the programming jokes I know! 😅"
    except:
        return "Oops! I couldn't get a joke right now. Please try again later."

# Live weather data using API
def get_weather():
    try:
        url = "https://api.met.no/weatherapi/locationforecast/2.0/compact"
        headers = {
            "User-Agent": "chatpy-weather-bot"
        }
        params = {
            "lat": 1.3521,       # (Singapore)
            "lon": 103.8198
        }

        response = requests.get(url, headers=headers, params=params)
        data = response.json()

        timeseries = data.get("properties", {}).get("timeseries", [])
        if not timeseries:
            return "Sorry, I couldn't get the weather data."

        current = timeseries[0]
        symbol = current["data"]["next_1_hours"]["summary"]["symbol_code"]
        temperature = current["data"]["instant"]["details"]["air_temperature"]
        summary_clean = symbol.replace("_", " ").capitalize()

        return f"The current weather in Singapore is {summary_clean} with a temperature of {temperature}°C."

    except Exception as e:
        return f"Oops! Something went wrong: {str(e)}"

# Greeting
def greet_user():
    print("Hello! I'm Chatpy, your friendly Python chatbot.")
    name = input("What's your name? ")
    print(f"Nice to meet you, {name}!")
    user_profile["name"] = name
    return name

# Time and date
def get_current_time():
    now = datetime.datetime.now(singapore_tz)
    return now.strftime("%I:%M %p")

def get_current_date():
    now = datetime.datetime.now(singapore_tz)
    return now.strftime("%A, %d %B %Y")

# Help
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

# Math evaluation
def evaluate_math(expression):
    try:
        result = eval(expression)
        return f"The answer is {result}"
    except:
        return "Sorry, I couldn't understand the math question."

# Word and char counters
def count_words(sentence):
    count = len(sentence.split())
    return f"There are {count} words."

def count_characters(sentence):
    count = len(sentence)
    return f"There are {count} characters."

# Quiz using Open Trivia DB API
def quiz():
    print("Choose a quiz category:")
    print("1. General Knowledge")
    print("2. Science & Nature")
    print("3. Mathematics")

    choice = input("Enter 1, 2, or 3: ").strip()

    category_map = {
        "1": 9,   # General Knowledge
        "2": 17,  # Science & Nature
        "3": 19   # Mathematics
    }

    if choice not in category_map:
        return "Invalid choice. Please enter 1, 2, or 3 next time."

    category_id = category_map[choice]

    try:
        # Fetch 5 easy difficulty questions
        url = f"https://opentdb.com/api.php?amount=5&category={category_id}&difficulty=easy&type=multiple"
        response = requests.get(url)
        data = response.json()

        if data["response_code"] != 0:
            return "Sorry, I couldn't fetch the quiz questions right now."

        score = 0
        print("\nStarting quiz...\n")

        for i, item in enumerate(data["results"], 1):
            question = html.unescape(item["question"])
            correct_answer = html.unescape(item["correct_answer"])
            options = [html.unescape(opt) for opt in item["incorrect_answers"]]
            options.append(correct_answer)
            random.shuffle(options)

            print(f"Q{i}: {question}")
            for idx, opt in enumerate(options, 1):
                print(f"{idx}. {opt}")

            user_ans = input("Your answer (1-4): ").strip()
            if user_ans.isdigit() and 1 <= int(user_ans) <= 4:
                chosen = options[int(user_ans) - 1]
                if chosen == correct_answer:
                    print("Correct!\n")
                    score += 1
                else:
                    print(f"Wrong! The correct answer was: {correct_answer}\n")
            else:
                print(f"Invalid input. The correct answer was: {correct_answer}\n")

        return f"You scored {score} out of 5. Well done!"

    except Exception as e:
        return f"An error occurred while fetching quiz data: {str(e)}"


# Input processing
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
        return get_programming_joke()
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
            return 'Use quotes like: how many words in "hello world"'
    elif "how many characters in" in user_input:
        start = user_input.find('"')
        end = user_input.rfind('"')
        if start != -1 and end != -1 and start < end:
            sentence = user_input[start + 1:end]
            return count_characters(sentence)
        else:
            return 'Use quotes like: how many characters in "hello world"'
    elif "what is" in user_input:
        parts = user_input.replace("what is", "").strip()
        return evaluate_math(parts)
    elif "quiz" in user_input:
        return quiz()

    for keyword in simple_responses:
        if keyword in user_input:
            return simple_responses[keyword]

    return "I'm sorry, I don't understand that. Type 'help' to see what I can do."

# Summary
def show_summary():
    print("\nChat Summary:")
    print("Name:", user_profile["name"])
    print("Total messages sent:", user_profile["messages_sent"])
    print("Thanks for chatting with Chatpy!")

# Start chatbot
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

# Run chatbot
start_chat()
