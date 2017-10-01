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

# def print_items(todos):
#     if len(todos) == 0:
#        print("No todos for today! :)")
#     else:
#         for index in range(len(todos)):
#             print(str(index+1) + ' - ' + todos[index]['task']) 


todo = argv[0]

def get_arguments():
    arguments = argv[1:]
    list_of_arguments = ['-a', '-r', '-c', '-l']
    if len(arguments) == 0:
        return False
    elif arguments[0] in list_of_arguments:
        return arguments
    else:
        print('Unsupported argument')
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

def delete_item():
    if len(argv) >= 3:
        try:
            remove_index = int(argv[2])
            with open("todos.txt","r+") as f:
                fr = f.readlines()
                f.seek(0)
                if len(fr) >= remove_index:
                    for line_index in range(len(fr)):
                        if remove_index != line_index + 1:
                            f.write(fr[line_index])
                    f.truncate()
                else:
                    print('Unable to remove: index is out of bound')
        except:
            print("Unable to remove: index is not a number")
    else:
        print("Unable to remove: no index provided")

def print_items(items):
    if len(items) == 0:
        print("No todos for today! :)")
    else:
        text = ""
        i = 1
        for line in items:
            text += str(i) + " - "
            if line['complete'] == False:
                text += '[ ] '
            else:
                text += '[X] '
            text += line['task']
            i += 1
        print(text)
            

def check_task():
    if len(argv) >= 3:
        try:
            check_index = int(argv[2])
            with open("todos.txt","r+") as f:
                fr = f.readlines()
                f.seek(0)
                if len(fr) >= check_index:
                        for line_index in range(len(fr)):
                            if check_index != line_index + 1:
                                f.write(fr[line_index])
                            else:
                                line = fr[line_index]
                                new_line = line.replace('0', '1')
                                f.write(new_line)
                        f.truncate()
                else:
                    print('Unable to check: index is out of bound')
        except:
            print("Unable to check: index is not a number")
    else:
        print("Unable to check: no index provided")
    
def controller():
    arguments = get_arguments()
    todos = import_file('todos.txt')
    # useage_command()
    if not arguments:
        print_usage()
    elif arguments[0] == "-l":
        print_items(todos)
    elif arguments[0] == "-c":
        check_task()
    elif arguments[0] == "-r":
        delete_item()
    elif arguments[0] == "-a":
        todos = get_add('todos.txt')
        

def print_usage():
    print('Command line arguments: \n-l   Lists all the tasks\n-a   Adds a new task\n-r   Removes an task\n-c   Completes an task')


controller()