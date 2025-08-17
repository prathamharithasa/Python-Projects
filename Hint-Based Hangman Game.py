import random
import turtle
import tkinter.messagebox as messagebox  # Import messagebox for hints and feedback

# Set up the screen
screen = turtle.Screen()
screen.title("Hint-Based Hangman Game")
screen.bgcolor("white")

# Set up turtle for writing text
writer = turtle.Turtle()
writer.hideturtle()
writer.penup()
writer.goto(0, 150)
writer.pendown()

# Words and their hints (3 hints per word)
words_with_hints = {
    "python": [
        "It's a popular programming language.",
        "It's named after a type of snake.",
        "It's known for its simplicity."
    ],
    "turtle": [
        "An animal with a shell.",
        "Also a Python graphics library.",
        "It moves slowly."
    ],
    "hangman": [
        "A classic guessing game.",
        "You guess letters to reveal a word.",
        "If you run out of tries, you lose."
    ],
    "computer": [
        "An electronic device for processing data.",
        "Has a CPU, memory, and storage.",
        "Has a keyboard, mousepad and a screen."
    ],
    "programming": [
        "The act of writing instructions for a computer.",
        "Python is one example.",
        "It can be done in many languages."
    ],
    "developer": [
        "A person who writes and builds software.",
        "Often works with code.",
        "Another word for programmer."
    ],
    "software": [
        "The set of instructions a computer follows.",
        "Can be an app or program.",
        "The opposite of hardware."
    ]
}

# Function to display the word with blanks
def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    writer.clear()
    writer.write(display, align="center", font=("Arial", 24, "normal"))

# Function to play the game
def play_game():
    word, hints = random.choice(list(words_with_hints.items()))
    guessed_letters = []
    hint_index = 0
    max_hints = 3

    while True:
        display_word(word, guessed_letters)

        # Win condition
        if all(letter in guessed_letters for letter in word):
            result = messagebox.askyesno("You Win!", "Congrats! You WON!!! Do you want to play again?")
            return result

        # Player input
        choice = screen.textinput(
            "Guess or Hint",
            "Type 'hint' for a hint or guess a letter:"
        )

        if choice is None:
            return False

        choice = choice.lower()

        if choice == "hint":
            if hint_index < max_hints:
                messagebox.showinfo("Hint", hints[hint_index])  # Show hint
                hint_index += 1

                if hint_index == max_hints:
                    display_word(word, guessed_letters)
                    final_guess = screen.textinput(
                        "Final Guess",
                        "This is your final guess! Enter a single letter or the full word:"
                    )
                    if final_guess is None:
                        return False
                    final_guess = final_guess.lower()

                    # Check if it's a single letter guess
                    if len(final_guess) == 1 and final_guess.isalpha():
                        if final_guess in word:
                            guessed_letters.append(final_guess)
                            if all(letter in guessed_letters for letter in word):
                                result = messagebox.askyesno("You Win!", "Congrats, you won! Do you want to play again?")
                                return result
                            else:
                                messagebox.showinfo("Correct Word", f"The correct word was: {word}")
                                result = messagebox.askyesno("You Lose!", "Sorry, you lost! Do you want to play again?")
                                return result
                        else:
                            messagebox.showinfo("Correct Word", f"The correct word was: {word}")
                            result = messagebox.askyesno("You Lose!", "Sorry, you lost! Do you want to play again?")
                            return result
                    # Check if it's a full word guess
                    elif final_guess == word:
                        result = messagebox.askyesno("You Win!", "Congrats, you won! Do you want to play again?")
                        return result
                    else:
                        messagebox.showinfo("Correct Word", f"Sorry, you lost! The correct word was: {word}")
                        result = messagebox.askyesno("You Lose!", "Do you want to play again?")
                        return result
            else:
                messagebox.showinfo("No Hints", "You've already used all hints.")
            continue

        # Letter guessing
        if not choice.isalpha() or len(choice) != 1:
            messagebox.showinfo("Invalid Input", "Please enter a single letter.")
            continue

        if choice in guessed_letters:
            messagebox.showinfo("Already Guessed", "You've already guessed that letter.")
            continue

        guessed_letters.append(choice)

# Main game loop with play again functionality
def main():
    while True:
        play_again = play_game()
        if not play_again:
            break
        writer.clear()  # Clear the screen for the next game

# Start the game
main()

# Exit on click
screen.exitonclick()
