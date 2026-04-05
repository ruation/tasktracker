import os
import sys
import json
from datetime import datetime

FILE = 'tasks.json'
def load_json():
    if not os.path.exists(FILE):
        with open(FILE, 'w') as f:
            json.dump([], f)
    try:
        with open(FILE, 'r') as file:
            return json.load(file)
    except json.JSONDecodeError:
        print('Error: JSON file is corrupted.')
        sys.exit(1)
def save_task(tasks):
    with open(FILE, 'w') as f:
        json.dump(tasks, f)

def add_task(title):
    tasks = load_json()
    new_id = 1
    if tasks:
        new_id = tasks[-1]['id'] + 1

    new_task = {'id' : new_id, 'title': title, 'status': 'notdone', 'createdAT': datetime.now().isoformat(), 'lastupdatedAT': datetime.now().isoformat()}
    tasks.append(new_task)
    save_task(tasks)
    print(f'Task "{title}", Id: {new_id}, added.')

def update_task(ID, new_title):
    tasks = load_json()
    for task in tasks:
        if task['id']==int(ID):
            task['title']=new_title
            save_task(tasks)
            print(f'Task ID:{ID} now have the title: "{new_title}"')
            return

def remove_task(ID):
    tasks = load_json()
    new_task = [task for task in tasks if task['id'] != int(ID)]
    save_task(new_task)
    print(f'Task ID:{ID} removed')

def mark_as(ID, status):
    tasks = load_json()
    for task in tasks:
        if task['id'] == int(ID):
            task['status'] = status
            task['lastupdatedAT'] = datetime.now().isoformat()
            save_task(tasks)
            print(f'Task ID:{ID} updated to {status}')
            return
    print('Error: Task ID not found')

def list_tasks(status = None):
    tasks = load_json()
    if status:
        tasks = [task for task in tasks if task['status']==status]
    if not tasks:
        print('No tasks found.')
        return
    for task in tasks:
        print(f'ID: {task['id']} Title: {task['title']} Status: {task['status']} CreatedAT: {task['createdAT']} LastUpdatedAT: {task['lastupdatedAT']}')

def show_mini_help():
    print(' "--help" for a guide.')
def show_help():
    print('\n---------Welcome to your todo tracker---------\n\nCommands:')
    print(' -a \"task name\"                                       Add task')
    print(' -u ID \"new task name\"                                Update task')
    print(' -r ID                                                Remove task')
    print(' -p ID                                                Mark taks as in-progress')
    print(' -d ID                                                Mark task as done')
    print(' -l                                                   List all tasks')
    print(' -l --done                                            List done tasks')
    print(' -l --notdone                                         List not done tasks')
    print(' -l --in-progress                                     List in-progress tasks')
    print(' -h, --help                                           Show the help message (this message)')
def main():
    load_json()
    if len(sys.argv) < 2:
        show_mini_help()
        return
    command = sys.argv[1]
    if command == '-a':
        if len(sys.argv) >= 3:
            title = ' '.join(sys.argv[2:])
            add_task(title)
            return
        print('Error: Missing task title')
        show_mini_help()
    elif command == '-u':
        if len(sys.argv) >= 4:
            new_title = ' '.join(sys.argv[3:])
            update_task(sys.argv[2], new_title)
            return
        show_mini_help()
    elif command == '-r' and len(sys.argv) == 3:
        remove_task(sys.argv[2])
        return
    elif command == '-p' and len(sys.argv) == 3:
        mark_as(sys.argv[2], 'in-progress')
        return
    elif command == '-d' and len(sys.argv) == 3:
        mark_as(sys.argv[2], 'done')
        return
    elif command == '-l':
        if len(sys.argv) >= 3:
            if sys.argv[2] == '--done':
                list_tasks('done')
                return
            elif sys.argv[2] == '--notdone':
                list_tasks('notdone')
                return
            elif sys.argv[2] == '--in-progress':
                list_tasks('in-progress')
                return
            else:
                status_not_found = ' '.join(sys.argv[2:])
                print(f'Error: "{status_not_found}" not found')
                show_mini_help()
                return
        list_tasks()
    elif command == '--help' or command == '-h':
        show_help()
        return
    else:
        print('Error: Unknown command')
        show_mini_help()
main()




