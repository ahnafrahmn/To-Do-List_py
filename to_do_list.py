


#==================>>>           A To-Do List Project:


import json
import os

fname = "todolist.json"
AppOn = True
task_List = []  # main task list

def isDigit(n):
    try:
        int(n)
        return True
    except ValueError:
        return False

def askValidInt(s, x, y):  # this function will retrun when user input is integer and also in the range of x <= input <= y
    while True:
        temp = input(s)
        if not isDigit(temp) or y < int(temp) or int(temp) < x: 
            print("\t **Invalid Input !!\n") 
        else:
            return int(temp)

def load_tasks():  # JSON file load
    global task_List
    if os.path.exists(fname):
        with open(fname, "r") as file:
            task_List = json.load(file)["tasks"]
    else: 
        task_List = []

def save_tasks():  # JSON save files
    with open(fname, "w") as file:
        json.dump({"tasks" : task_List}, file, indent=4)

def task_done():
    task = askValidInt("Enter task no: ", 1, len(task_List))

    if task_List[task-1].startswith("[DONE]"):
        print("\n\t This task is already marked as 'DONE'.\n")
        return

    task_List[task-1] = "[DONE] > " + task_List[task-1]
    save_tasks()
    print("\n\t Congratulations! You have complited a task.\n")

def task_delete():
    task = askValidInt("Enter task no: ", 1, len(task_List))
    del task_List[task-1]
    save_tasks()
    print("\n\t Task Deleted.")

def main_page():
    print("\n================================================================")
    print("\t\t\t To-Do List ")
    print("================================================================\n")

    print("\t\t Menu \n")
    print("\t (1) Add a new task")
    print("\t (2) Show List")
    print("\t (3) Delete List")
    print("\t (4) Exit")
    print("\n================================================================\n\n")

    opt = askValidInt("\t Choose your option : ", 1, 4)
    
    if len(task_List)==0 and opt != 1 and opt != 4:
        print("\n\t Task list is empty. Please add a new task.\n")
        return
    
    match opt:
        case 1: new_task()
        case 2: show_List()
        case 3: delete_list() 
        case 4: exitApp() 
    
    return



def new_task():
    print("\n\n================================================================")
    while True:
        task = input("\t Write a task:\n\t >> ").strip()
        if task:
            task_List.append(task)
            save_tasks()
            print("\n\t Task Listed Successfully! \n\n")
            return
        else:
            print("\t Invalid Task!\n")


def show_List():
    print("=================> Task list <=================")
    for i, _ in enumerate(task_List, start=1):
        print(f"\t {i} : {_}")
    
    opt = askValidInt("\n\n\t (1) Return to menu\
                       \n\t (2) Mark a task as DONE\
                       \n\t (3) Delete a task\
                       \n\n\t Enter option :  ", 1, 3)
    match opt:
        case 1: return
        case 2: task_done()
        case 3: task_delete()

def delete_list():
    task_List.clear()
    save_tasks()
    print("\n\t List is deleted.")

def exitApp():
    print("\n\n\n\t\t Thank You!\n\n")
    save_tasks()
    global AppOn
    AppOn = False

load_tasks()

while AppOn:
    main_page()