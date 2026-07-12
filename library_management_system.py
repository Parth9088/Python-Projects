# ==========================================
# LIBRARY MANAGEMENT SYSTEM (Python Only)
# ==========================================

library = []


# -------------------------------
# Add Book
# -------------------------------
def add_book():
    print("\n--- Add New Book ---")

    book_id = input("Book ID: ")
    title = input("Book Title: ")
    author = input("Author: ")

    book = {
        "ID": book_id,
        "Title": title,
        "Author": author,
        "Issued": False
    }

    library.append(book)
    print("\n✅ Book Added Successfully!")


# -------------------------------
# View Books
# -------------------------------
def view_books():
    if len(library) == 0:
        print("\nNo Books Available.")
        return

    print("\n========== BOOK LIST ==========")

    for book in library:
        status = "Issued" if book["Issued"] else "Available"

        print(f"""
Book ID : {book['ID']}
Title   : {book['Title']}
Author  : {book['Author']}
Status  : {status}
---------------------------------
""")


# -------------------------------
# Search Book
# -------------------------------
def search_book():
    keyword = input("\nEnter Book ID or Title: ").lower()

    found = False

    for book in library:
        if keyword == book["ID"].lower() or keyword in book["Title"].lower():
            status = "Issued" if book["Issued"] else "Available"

            print("\nBook Found")
            print("--------------------")
            print("Book ID :", book["ID"])
            print("Title   :", book["Title"])
            print("Author  :", book["Author"])
            print("Status  :", status)

            found = True

    if not found:
        print("Book Not Found.")


# -------------------------------
# Issue Book
# -------------------------------
def issue_book():
    book_id = input("\nEnter Book ID: ")

    for book in library:

        if book["ID"] == book_id:

            if book["Issued"]:
                print("Book is already issued.")
            else:
                book["Issued"] = True
                print("✅ Book Issued Successfully.")

            return

    print("Book Not Found.")


# -------------------------------
# Return Book
# -------------------------------
def return_book():
    book_id = input("\nEnter Book ID: ")

    for book in library:

        if book["ID"] == book_id:

            if not book["Issued"]:
                print("Book is already available.")
            else:
                book["Issued"] = False
                print("✅ Book Returned Successfully.")

            return

    print("Book Not Found.")


# -------------------------------
# Delete Book
# -------------------------------
def delete_book():
    book_id = input("\nEnter Book ID: ")

    for book in library:

        if book["ID"] == book_id:
            library.remove(book)
            print("✅ Book Deleted Successfully.")
            return

    print("Book Not Found.")


# -------------------------------
# Available Books
# -------------------------------
def available_books():

    print("\n====== AVAILABLE BOOKS ======")

    count = 0

    for book in library:

        if not book["Issued"]:
            print(f"{book['ID']} - {book['Title']} ({book['Author']})")
            count += 1

    if count == 0:
        print("No Available Books.")


# -------------------------------
# Total Books
# -------------------------------
def total_books():
    print(f"\nTotal Books in Library: {len(library)}")


# -------------------------------
# Main Menu
# -------------------------------
while True:

    print("""
====================================
      LIBRARY MANAGEMENT SYSTEM
====================================
1. Add Book
2. View Books
3. Search Book
4. Issue Book
5. Return Book
6. Delete Book
7. Available Books
8. Total Books
9. Exit
====================================
""")

    choice = input("Enter Your Choice: ")

    if choice == "1":
        add_book()

    elif choice == "2":
        view_books()

    elif choice == "3":
        search_book()

    elif choice == "4":
        issue_book()

    elif choice == "5":
        return_book()

    elif choice == "6":
        delete_book()

    elif choice == "7":
        available_books()

    elif choice == "8":
        total_books()

    elif choice == "9":
        print("\nThank You for Using Library Management System!")
        break

    else:
        print("❌ Invalid Choice. Please Try Again.")