# Smart Task & Priority Manager

## 📺 Project Explanation Video
> **CRITICAL:** https://youtu.be/CXO2vIx7liU
> *This video includes a 10–15 minute walkthrough of the application features, code explanation, and reflection.*

---

## 📝 Project Description
The **Smart Task & Priority Manager** is a terminal-based application designed to help users organize their daily responsibilities through logic-driven prioritization. Unlike basic list apps, this tool treats tasks as unique objects and utilizes sorting algorithms to ensure high-stakes tasks are always front-and-center. 

Built as a Final Project for **Intermediate Programming (CCCS_ 103)**, it demonstrates mastery of Object-Oriented Programming (OOP), data persistence, and defensive programming.

---

## 🚀 Key Features

* **Object-Oriented Design:** Uses a custom `Task` class to encapsulate data including title, priority levels (1-5), and deadlines.
* **Intelligent Sorting:** Features a non-trivial sorting algorithm that automatically reorganizes the list to place high-priority items at the top.
* **Data Persistence:** Implements professional file handling using a `.csv` format inside a dedicated `data/` directory.
* **Advanced Context Management:** Utilizes Python’s `with` statement and magic methods (`__enter__`, `__exit__`) to automate the loading and saving of data safely.
* **Defensive Programming:** Robust input validation (try-except blocks) prevents application crashes during user data entry.

---

## 📂 Project Structure
The repository is organized according to professional standards to ensure modularity and clarity:

```text
Bagtasos_Mark-Joseph_FinalProject/
├── data/
│   └── tasks.csv          # Persistent data storage
├── src/
│   ├── main.py            # Entry point of the application
│   ├── manager.py         # TaskManager logic & Context Manager
│   └── task.py            # Task class definition (OOP)
├── .gitignore             # Prevents tracking of junk files
└── README.md              # Project documentation
