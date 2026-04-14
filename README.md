# 📝 Task Tracker CLI (Python + JSON)

A simple **Task Tracker CLI tool** built with **Python** that stores tasks locally inside a `tasks.json` file.

This project is focused on practicing:
- CLI commands with `sys.argv`
- JSON file handling
- CRUD operations (Create, Read, Update, Delete)
- Task status management

---

## 🚀 Features

- Add tasks
- Update task title
- Remove tasks
- Mark tasks as `in-progress` or `done`
- List all tasks
- Filter tasks by status
- Stores everything in a local `tasks.json` file
- Automatically creates `tasks.json` if it does not exist

---

## 📂 Project Structure

task-tracker-cli/  
│── main.py  
│── tasks.json  
│── README.md  

---

## ⚙️ Requirements

- Python 3.x  
(No external libraries required)

---

## ▶️ How to Run

Run the program using:
```bash
python main.py <command> [arguments]
```
---

## 🆘 Help Command

To see all available commands, run:
```
python main.py --help```

or
```
python main.py -h```

Output:
```
---------Welcome to your todo tracker---------

Commands:
 -a "task name"                                       Add task
 -u ID "new task name"                                Update task
 -r ID                                                Remove task
 -p ID                                                Mark taks as in-progress
 -d ID                                                Mark task as done
 -l                                                   List all tasks
 -l --done                                            List done tasks
 -l --notdone                                         List not done tasks
 -l --in-progress                                     List in-progress tasks
 -h, --help                                           Show the help message (this message)
``
---

## 🗃️ JSON File Format

All tasks are stored inside `tasks.json` in this format:
```
[
  {
    "id": 1,
    "title": "Study Python",
    "status": "notdone",
    "createdAT": "2026-04-04T15:32:21.492832",
    "lastupdatedAT": "2026-04-04T15:32:21.492832"
  }
]
```

---

## 📌 Task Status

A task can have one of these statuses:

- notdone
- in-progress
- done

---

## 📜 License

This project is open-source and free to use.
