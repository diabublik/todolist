import json
# To DO: надо исправить баг на 143 строке

def print_equal():
    for i in range(50):
        print("=", end="")
    print()


def print_dash():
    for i in range(50):
        print("-", end="")
    print()


def show_list():
    try:
        with open("todolist.json", "r", encoding="utf-8") as file:
            data = json.load(file)

        print_equal()
        for key, value in data.items():
            print(f"{value['priority']} | {key} | {value['tag']} | {value['date']}")
        print_equal()
    except (json.decoder.JSONDecodeError):
        print_equal()
        print("The list is empty")
        print_equal()


def sort():
    try:
        with open("todolist.json", "r", encoding="utf-8") as file:
            data = json.load(file)

        sorted_data = dict(sorted(data.items(), key=lambda x: int(x[1]["priority"])))
        
        with open("todolist.json", "w", encoding="utf-8") as file:
            json.dump(sorted_data, file, indent=4)
    except (json.decoder.JSONDecodeError):
        print("The list is empty")


def add_task():
    try:
        with open("todolist.json", "r", encoding="utf-8") as file:
            data = json.load(file)
    except (json.decoder.JSONDecodeError):
        data = {}
    
    print_dash()
    add_priority = input("Enter the priority of new task: ")
    add_taskname = input("Enter the name of new task: ")
    add_tag = input("Enter the tag of new task: ")
    add_date = input("Enter the date of new task: ")

    data[add_taskname] = {
        "priority": add_priority,
        "tag": add_tag,
        "date": add_date
    }

    with open("todolist.json", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)
    
    sort()


def find_task():    
    try:
        with open("todolist.json", "r", encoding="utf-8") as file:
            data = json.load(file)
        print_dash()
        print("What do you want to find:")
        print("1 - priority\n2 - name of task\n3 - tag\n4 - date")
        choice = input("Your choice: ")
        
        if choice == '1':
            need_priority = input("Enter the necessary priority: ")
            print("The found tasks:") 
            for key, value in data.items():
                if value["priority"] == need_priority:
                    print(f"{value['priority']} | {key} | {value['tag']} | {value['date']}")

        elif choice == '2':
            need_name_task = input("Enter the name of necessary key: ")
            print("The found tasks:") 
            for key, value in data.items():
                if key == need_name_task:
                    print(f"{value['priority']} | {key} | {value['tag']} | {value['date']}")

        elif choice == '3':
            need_tag = input("Enter the necessary tag: ")
            print("The found tasks:") 
            for key, value in data.items():
                if value["tag"] == need_tag:
                    print(f"{value['priority']} | {key} | {value['tag']} | {value['date']}")

        elif choice == '4':
            need_date = input("Enter the necessary date (DD-MM-YYYY): ")
            print("The found tasks:") 
            for key, value in data.items():
                if value["date"] == need_date:
                    print(f"{value['priority']} | {key} | {value['tag']} | {value['date']}")
        else:
            print("What the fuck are you typing -_-")
    except (json.decoder.JSONDecodeError):
        pass


def delete_task():
    try:
        with open("todolist.json", "r", encoding="utf-8") as file:
            data = json.load(file)
        
        print_dash()
        deleted_task = input("Enter the name of the task you want to delete: ")
        print("Deleted tasks:")

        if deleted_task in data:
            print(f"{data[deleted_task]['priority']} | {deleted_task} | {data[deleted_task]['tag']} | {data[deleted_task]['date']}")
            del data[deleted_task]
        else:
            print("There isn`t such task")

        with open("todolist.json", "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)
    except (json.decoder.JSONDecodeError):
        pass


def mark_completed():
    # читаем основной тудулист (если есть)
    try:
        with open("todolist.json", "r", encoding="utf-8") as file:
            data = json.load(file)

        print_dash()
        completed_task = input("Enter the name of the task that you have comleted: ")
        
        if completed_task in data:
            del data[completed_task]["priority"]

            #читаем список законченных дел (если есть)
            try:
                with open("completed_tasks.json", "r", encoding="utf-8") as comp_file: # если файл пуст, то блок if не выполнятеся
                    comp_data = json.load(comp_file)
            except(json.decoder.JSONDecodeError):
                comp_data = {}

            # сохраняем нужную задачу в список законченных дел
            comp_data[completed_task] = data[completed_task]
            
            #записываем эту задачу в этот список
            with open("completed_tasks.json", "w", encoding="utf-8") as comp_file:
                json.dump(comp_data, comp_file, indent=4)

            # удаляем законченную задачу из тудулиста и переписываем его содержимое
            del data[completed_task]
            with open("todolist.json", "w", encoding="utf-8") as file:
                json.dump(data, file, indent=4)
        else:
            print("There isn`t a such task")
    except (json.decoder.JSONDecodeError):
        print("The list is empty")


def show_comp_tasks():
    try:
        with open("completed_tasks.json", "r", encoding="utf-8") as comp_file:
            data = json.load(comp_file)
    
        print_equal()
        for key, value in data.items():
            print(f"{key} | {value['tag']} | {value['date']}")
        print_equal()
    except (json.decoder.JSONDecodeError):
        print_dash()
        print("The list is empty")
        print_dash()


def clear_completed_list():
    with open("completed_tasks.json", "w", encoding="utf-8") as comp_file:
        print_dash()
        print("The list was cleared")
        pass


def menu():
    choice: str = '-1'
    while choice != '7':
        show_list()

        print("1 - Add new task")
        print("2 - Find the task")
        print("3 - Delete the task")
        print("4 - Mark completed task")
        print("5 - Clear the list of the completed tasks")
        print("6 - Show the completed tasks")
        print("7 - Exit")
        
        choice = input("Enter the number: ")

        if choice == '1':
            add_task()
        elif choice == '2':
            find_task()
        elif choice == '3':
            delete_task()
        elif choice == '4':
            mark_completed()
        elif choice == '5':
            clear_completed_list()
        elif choice == '6':
            show_comp_tasks()
        elif choice == '7':
            print_dash()
            print("Bye")
            print_dash()
        else:
            print_dash()
            print("What the fuck are you typing -_-")


if __name__ == "__main__":
    menu()
