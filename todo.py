from sys import argv

def import_file(file_name):
    file = open(file_name, 'r')
    fr = file.readlines()
    file.close()
    items = []
    for line in fr:
        dictionary = {}
        if line[0] == '0':
            dictionary["complete"] = False
        elif line[0] == '1':
            dictionary["complete"] = True
        task = line[2:]
        dictionary['task'] = task
        items.append(dictionary)
    return items

def print_items(todos):
    if len(todos) == 0:
       print("No todos for today! :)")
    else:
        for index in range(len(todos)):
            print(str(index+1) + ' - ' + todos[index]['task']) 

todo = argv[0]

def get_arguments():
    arguments = argv[1:]
    list_of_arguments = ['-a', '-r', '-c', '-l']
    if len(arguments) > 0 and arguments[0] in list_of_arguments:
        return arguments
    else:
        return False

def get_add(giving_item):
    if len(argv) >= 3:
        giving_items = argv[2:]
        with open('todos.txt', 'a') as fw:
            fw.write('0 ' + ' '.join(giving_items) + '\n')
        fw.close()
        return import_file('todos.txt')
    else:
        print("Unable to add: no task provided")

# def delete_items():
        

def check_task(items):
    text = ""
    i = 1
    for line in items:
        text += str(i) + " - "
        print(line)
        if line['complete'] == False:
            text += '[ ] '
        else:
            text += '[X] '
        text += line['task']
        i += 1
    print(text)
            
def controller():
    arguments = get_arguments()
    todos = import_file('todos.txt')
    # useage_command()
    if not arguments:
        print_usage()
    elif arguments[0] == "-l":
        print_items(todos)
    elif arguments[0] == "-c":
        check_task(todos)
    elif arguments[0] == "-r":
        print("remove")
    elif arguments[0] == "-a":
        todos = get_add('todos.txt')
        
       
        # print("add")

def print_usage():
    print('Command line arguments: \n-l   Lists all the tasks\n-a   Adds a new task\n-r   Removes an task\n-c   Completes an task')

# def useage_command():
#     todos = import_file('todos.txt')
#     arguments = get_arguments()
#     text = ""
#     if not arguments:
#         return 'Command line arguments: \n-l   Lists all the tasks\n-a   Adds a new task\n-r   Removes an task\
#                 -c   Completes an task'
#     elif arguments[-1] == "-a" + 'text':
#         todos.append("text")
#         return (todos)
#     elif arguments[-1] == "-l":
#         print(todos)
#     elif arguments[-1] == "-r" + str(len(todos[0])):
#         todos.remove(todos[0])
#         return todos    
#     elif arguments[-1] == "-c" and str(len(todos[0])):
#         todos[todos[0]] = int(len(todos[0]))



controller()
# print(useage_command())