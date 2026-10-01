def add_book():
    file = open("books.txt", "a")

    book_id = input("Enter Book ID: ")
    title = input("Enter Title: ")
    author = input("Enter Author: ")

    file.write(f"{book_id},{title},{author},Available\n")

    file.close()

    print("Book added successfully.")


def search_book():
    search = input("Enter Book ID: ")

    file = open("books.txt", "r")

    found = False

    for line in file:
        data = line.strip().split(",")

        if data[0] == search:
            print(data)
            found = True

    file.close()

    if not found:
        print("Book not found.")


def display_available():
    file = open("books.txt", "r")

    for line in file:
        data = line.strip().split(",")

        if data[3] == "Available":
            print(data)

    file.close()


def issue_book():
    book_id = input("Enter Book ID to issue: ")

    file = open("books.txt", "r")
    lines = file.readlines()
    file.close()

    file = open("books.txt", "w")

    for line in lines:
        data = line.strip().split(",")

        if data[0] == book_id:
            data[3] = "Issued"

        file.write(",".join(data) + "\n")

    file.close()

    print("Book issued.")


def return_book():
    book_id = input("Enter Book ID to return: ")

    file = open("books.txt", "r")
    lines = file.readlines()
    file.close()

    file = open("books.txt", "w")

    for line in lines:
        data = line.strip().split(",")

        if data[0] == book_id:
            data[3] = "Available"

        file.write(",".join(data) + "\n")

    file.close()

    print("Book returned.")


while True:
    print("\n1. Add Book")
    print("2. Search Book")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Available Books")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_book()
    elif choice == "2":
        search_book()
    elif choice == "3":
        issue_book()
    elif choice == "4":
        return_book()
    elif choice == "5":
        display_available()
    elif choice == "6":
        break
    else:
        print("Invalid choice")
