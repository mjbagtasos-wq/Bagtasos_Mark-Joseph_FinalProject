# Smart Task & Priority Manager

## 📺 Project Explanation Video
> **Video link** https://youtu.be/CXO2vIx7liU

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

## 🛠️ Technical Implementation
| Requirement | Implementation Detail |
| :--- | :--- |
| **OOP** | Defined a `Task` class in `task.py` to encapsulate title, priority, and status.  |
| **Algorithm** | Implemented a descending sort algorithm in `manager.py` using lambda keys.  |
| **Data Structure** | Utilized a Python **List** to store and manipulate `Task` objects in memory.  |
| **Advanced Concept** | Implemented **Context Managers** (`__enter__` / `__exit__`) for safe file I/O.  |
| **File Handling** | Uses the `csv` module to maintain a persistent database in `data/tasks.csv`.  |
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

---

## 📸 Sample Usage (Screenshots) 
Below are demonstrations of the CLI interface in action: 

| Feature | Screenshot |
| :--- | :--- |
| **Main Menu** | ![Main Menu](https://github.com/mjbagtasos-wq/Bagtasos_Mark-Joseph_FinalProject/blob/dc6707cb5caafa819544e2c884011beeca05dc44/screenshots/menu.png) |
| **Sorted Task View** | ! |
| **Input Validation** | ! |

---
