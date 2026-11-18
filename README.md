# UPM Library Management System

A Python-based Library Management System developed using Object-Oriented Programming (OOP). The application allows users to manage books, members, borrowing, and returning operations through a graphical interface.
It's a Small and simple prgramm for a uni project 

## Features

- **Book Management**
  - Add and remove books.
  - Display available books.
  - Sort books by title.
  - Track available copies.

- **Member Management**
  - Register regular and premium members.
  - Manage member information.
  - View borrowed books.

- **Borrowing and Returning**
  - Borrow books using member and book IDs.
  - Return borrowed books.
  - Update available book copies.
  - Keep track of borrowing history.

- **Graphical Interface**
  - Built using CustomTkinter.
  - Easy navigation between pages.
  - Separate login pages for regular and premium members.
  - Light and dark modes.

- **Data Storage**
  - Store data locally in a JSON file.
  - Load previously saved data.
  - Save books, members, and borrowing records.

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| CustomTkinter | Graphical interface |
| Tkinter | GUI framework |
| Pillow | Image handling |
| JSON | Data storage |

## Project Structure

```text
OOPproject/
│
├── img/                  # Images and icons
│
├── AddRmv.py             # Add and remove books
├── Book.py               # Book class
├── BorrowReturn.py       # Borrowing and returning
├── LibararyGUI.py        # Main graphical interface
├── Library.py            # Library management
├── Member.py             # Member class
├── PremiumLogin.py       # Premium member login
├── UserLogin.py          # Regular member login
├── Shared.py             # Shared resources
│
├── library_data.txt      # Saved library data
├── menu run.py           # Command-line application
└── README.md
```

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/Hal716/OOPproject.git
```

### 2. Open the project directory

```bash
cd OOPproject
```

###
