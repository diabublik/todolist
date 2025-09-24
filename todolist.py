import json
# TO DO: добавить обработку исключений, если файлы пустые
#        и добавить функцию очистки списка завершённых задач

def print_equal():
    for i in range(50):
        print("=", end="")
    print()


def print_dash():
    for i in range(50):
        print("-", end="")
    print()


def show_list():
    with open("todolist.json", "r", encoding="utf-8") as file:
        data = json.load(file)
    
    print_equal()
    for key, value in data.items():
        print(f"{value['priority']} | {key} | {value['tag']} | {value['date']}")
    print_equal()


def sort():
    with open("todolist.json", "r", encoding="utf-8") as file:
        data = json.load(file)

    sorted_data = dict(sorted(data.items(), key=lambda x: int(x[1]["priority"])))
    
    with open("todolist.json", "w", encoding="utf-8") as file:
        json.dump(sorted_data, file, indent=4)


def add_task():
    add_priority = input("Enter the priority of new task: ")
    add_taskname = input("Enter the name of new task: ")
    add_tag = input("Enter the tag of new task: ")
    add_date = input("Enter the date of new task: ")

    with open("todolist.json", "r", encoding="utf-8") as file:
        data = json.load(file)

    data[add_taskname] = {
        "priority": add_priority,
        "tag": add_tag,
        "date": add_date
    }

    with open("todolist.json", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)
    
    sort()


def find_task():
    print("What do you want to find:")
    print("1 - priority\n2 - name of task\n3 - tag\n4 - date")
    choice = int(input("Your choice: "))
    
    with open("todolist.json", "r", encoding="utf-8") as file:
        data = json.load(file)
    
    if choice == 1:
        need_priority = input("Enter the necessary priority: ")
        print("The found tasks:") 
        for key, value in data.items():
            if value["priority"] == need_priority:
                print(f"{value['priority']} | {key} | {value['tag']} | {value['date']}")

    elif choice == 2:
        need_name_task = input("Enter the name of necessary key: ")
        print("The found tasks:") 
        for key, value in data.items():
            if key == need_name_task:
                print(f"{value['priority']} | {key} | {value['tag']} | {value['date']}")

    elif choice == 3:
        need_tag = input("Enter the necessary tag: ")
        print("The found tasks:") 
        for key, value in data.items():
            if value["tag"] == need_tag:
                print(f"{value['priority']} | {key} | {value['tag']} | {value['date']}")

    elif choice == 4:
        need_date = input("Enter the necessary date (DD-MM-YYYY): ")
        print("The found tasks:") 
        for key, value in data.items():
            if value["date"] == need_date:
                print(f"{value['priority']} | {key} | {value['tag']} | {value['date']}")


def delete_task():
    deleted_task = input("Enter the name of the task you want to delete: ")
    print("Deleted tasks:")
    with open("todolist.json", "r", encoding="utf-8") as file:
        data = json.load(file)

    if deleted_task in data:
        print(f"{data[deleted_task]['priority']} | {deleted_task} | {data[deleted_task]['tag']} | {data[deleted_task]['date']}")
        del data[deleted_task]
    else:
        print("There isn`t such task")

    with open("todolist.json", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)


def mark_completed():
    with open("todolist.json", "r", encoding="utf-8") as file:
        data = json.load(file)

    completed_task = input("Enter the name of the task that you have comleted: ")
    print_dash()
    
    if completed_task in data:
        del data[completed_task]["priority"]

        with open("completed_tasks.json", "r+", encoding="utf-8") as comp_file:
            comp_data = json.load(comp_file)
            comp_data[completed_task] = data[completed_task]
            json.dump(comp_data, comp_file, indent=4)

        del data[completed_task]
        with open("todolist.json", "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)
    else:
        print("There isn`t such task")


def menu():
    choice: int = -1
    while choice != 6:
        show_list()

        print("1 - Add new task")
        print("2 - Find the task")
        print("3 - Delete the task")
        print("4 - Mark completed task")
        print("6 - Exit")
        
        choice = int(input("Enter the number: "))
        print_dash()

        if choice == 1:
            add_task()
        elif choice == 2:
            find_task()
        elif choice == 3:
            delete_task()
        elif choice == 4:
            mark_completed()
        elif choice == 6:
            print("Bye")
            print_dash()
        else:
            print("What the fuck are you inputing -_-")


if __name__ == "__main__":
    menu()
