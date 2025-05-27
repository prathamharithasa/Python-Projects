import random
#Home screen
print("Welcome to the workout routine generator!")
#Different types of excerises using lists
upper_body = ["Push-ups", "Pull-ups", "Shoulder Press"]
lower_body = ["Squats", "Lunges", "Calf Raises"]
core = ["Plank", "Sit-ups", "Leg Raises"]
cardio = ["Jumping Jacks", "Burpees", "Running"]
#Input choice
def generate_workout():
    print("Your workout for today is:")
    print("- Upper Body:", random.choice(upper_body))
    print("- Lower Body:", random.choice(lower_body))
    print("- Core:", random.choice(core))
    print("- Cardio:", random.choice(cardio))

generate_workout()
