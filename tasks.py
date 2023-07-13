import os

TASKS_FILE_PATH = os.path.join(os.path.expanduser('~'), 'Downloads', 'Your_todo_lists.txt')


def display_menu():
    print('*' * 10, 'Manage your Tasks', '*' * 10)
    print('-' * 15, 'MENU', '-' * 15)
    print(' ' * 10, '1. Add a task', ' ' * 10)
    print(' ' * 10, '2. Update a task', ' ' * 10)
    print(' ' * 10, '3. Delete a task', ' ' * 10)
    print(' ' * 10, '4. View tasks', ' ' * 10)
    print(' ' * 10, '5. Exit', ' ' * 10)
    print('-' * 36)
    option = input('Choose an Option to Continue: ')
    return option


def save_tasks_to_file(tasks):
    if len(tasks) == 0:
        print('You have no tasks to save :(')
        return

    with open(TASKS_FILE_PATH, 'w') as file:
        for count, task in enumerate(tasks):
            file.write(f'{count}: {task}\n')
    print('Tasks saved successfully!')
    print(f'Your file is located at {TASKS_FILE_PATH}')


tasks = []
option = display_menu()

while option != '5':
    if option == '1':
        task = input('What is the Task? ')
        tasks.append(task)
        option = display_menu()
    elif option == '2':
        count = 0
        for x in tasks:
            print(f'{count}: {x}')
            count += 1

        try:
            task_to_update = int(input('Choose the Task to Update (enter the number): '))
            if 0 <= task_to_update < len(tasks):
                updated_task = input('Enter the new task: ')
                tasks[task_to_update] = updated_task
                option = display_menu()
            else:
                print('Invalid task number!')
        except ValueError:
            print('Please choose by a number')
    elif option == '3':
        count = 0
        for x in tasks:
            print(f'{count}: {x}')
            count += 1
        try:
            task_to_delete = int(input('Choose the Task to Delete (enter the number): '))
            if 0 <= task_to_delete < len(tasks):
                tasks.pop(task_to_delete)
                option = display_menu()
            else:
                print('Invalid task number!')
        except ValueError:
            print('Please choose by a number')
    elif option == '4':
        count = 0
        for x in tasks:
            print(f'{count}: {x}')
            count += 1
        option = display_menu()
    else:
        print('Invalid option! Please choose a valid option.')
        option = display_menu()

print('You closed the program')
save_tasks = input('Do you want to save your Tasks? Enter "yes" or "no": ')
if save_tasks.lower() == 'yes':
    save_tasks_to_file(tasks)
else:
    print('Tasks not saved.')

exit(0)

