from Library import Library

def main():
    library = Library()

    while True:
        print("\nWelcome to ONE LAST Library.")
        print("\n===== Library Menu =====")
        print("1. Show available books")
        print("2. Show members")
        print("3. Add new book")
        print("4. Remove book")
        print("5. Register new member")
        print("6. Borrow book")
        print("7. Return book")
        print("8. Display member borrowed list")
        print("9. Display all books sorted by title")
        print("10. Show transaction history")
        print("11. Exit and Save")

        choice = input("Enter your choice: ").strip().lower()
#chosing system
        if choice == "11":
            library.save_data()
            print("Saving and exiting...")
            break

        elif choice == "1":
            if not library.available_books:
                print("No books available.")
            else:
                for book in library.available_books:
                    print(book)

        elif choice == "2":
            if len(library.members) == 0:
                print("No members yet.")
            else:
                library.print_member()

        elif choice == "3":
            library.add_new_books()

        elif choice == "4":
            library.remove_book()

        elif choice == "5":
            library.register_new_members()

        elif choice == "6":
            library.borrow_books()

        elif choice == "7":
            library.return_books()

        elif choice == "8":
            library.display_member_borrowed_books()

        elif choice == "9":
            library.display_all_books_sorted()
        
        elif choice == "10":
            library.show_history()

        else:
            print("Invalid choice. Please try again.")
#run the code
if __name__ == "__main__":
    main()
