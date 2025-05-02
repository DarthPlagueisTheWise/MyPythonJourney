# Simple CLI Notes App

notes = []

def show_menu():
    print("\n==== Notes App ====")
    print("1. View Notes")
    print("2. Add Note")
    print("3. Delete Note")
    print("4. Exit")

while True:
    show_menu()
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        if notes:
            print("\nYour Notes:")
            for i, note in enumerate(notes, start=1):
                print(f"{i}. {note}")
        else:
            print("No notes yet.")
    
    elif choice == "2":
        note = input("Enter your note: ")
        notes.append(note)
        print("Note added.")

    elif choice == "3":
        index = int(input("Enter note number to delete: ")) - 1
        if 0 <= index < len(notes):
            removed = notes.pop(index)
            print(f"Deleted note: {removed}")
        else:
            print("Invalid note number.")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")

