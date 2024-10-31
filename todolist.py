tasks=[]
def add_task():
    task=input("enter a new task")
    tasks.append(task)
    print("Task addedd sucessfully")

def view_task():

    if len(tasks)==0:
        print("No tasks")
    else:
        print("List of tasks:")
        for i , task in enumerate(tasks):
            print(f'{i+1}.{task}')

def delete_task():
    if len(tasks) == 0:
        print("No tasks to delete")
    else:
        print("List of tasks:")
        for i, task in enumerate(tasks):
            print(f'{i + 1}.{task}')
        choice=int(input("Enter your choice to delete the task number:"))
        if 0<choice <=len(tasks):
            del tasks[choice-1]
            print("deleted")
        else:
            print("invalid no")

def main():
    while True:
        print("1. Add task")
        print("2. View task")
        print("3. Delete task")
        print("4.QUIT")

        choice=int(input("Enter your choice"))
        if choice==1:
            add_task()
        elif choice==2:
            view_task()
        elif choice==3:
            delete_task()
        elif choice==4:
            print("Thank you for using To do list app.")
            break
        else:
            print("Invalid choice.Please try again")



if __name__=='__main__':
    main()