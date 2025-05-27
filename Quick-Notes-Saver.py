#Input note and save
def save_note():
    note = input("Write your note: ").strip()
    if note:
        with open("notes.txt", "a", encoding="utf-8") as f:
            f.write(note + "\n")
        print("Note saved!")
    else:
        print("Note is empty, not saved.")

#View note
def view_notes():
    try:
        with open("notes.txt", "r", encoding="utf-8") as f:
            print("\nYour Notes:")
            print(f.read())
    except FileNotFoundError:
        print("No notes found yet.")

#Home screen
while True:
    print("\nWelcome to Quick Notes")
    print("1. Add Note")
    print("2. View Notes")
    print("3. Exit")
    choice = input("What would you like to do? ").strip()

    #Input choice
    if choice == "1":
        save_note()
    elif choice == "2":
        view_notes()
    elif choice == "3":
        print("Goodbye! Have a nice day!")
        break
    else:
        print("Invalid option, please try again.")
