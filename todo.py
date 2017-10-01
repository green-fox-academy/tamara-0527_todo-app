from sys import argv

todo = argv[0]
todo_file="todos.txt"


def import_file():
    file = open(todo_file, 'r')
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


def add_task():
    if len(argv) >= 3:
        giving_items = argv[2:]
        with open(todo_file, 'a') as fw:
            fw.write('0 ' + ' '.join(giving_items) + '\n')
        return 'Task is added'
    else:
        return "Unable to add: no task provided"


def delete_item():
    if len(argv) >= 3:
        try:
            remove_index = int(argv[2])
            with open(todo_file,"r+") as f:
                fr = f.readlines()
                f.seek(0)
                if len(fr) >= remove_index:
                    for line_index in range(len(fr)):
                        if remove_index != line_index + 1:
                            f.write(fr[line_index])
                    f.truncate()
                    return 'Removed'
                else:
                    return 'Unable to remove: index is out of bound'
        except:
            return "Unable to remove: index is not a number"
    else:
        return "Unable to remove: no index provided"


def print_items():
    items = import_file()
    if len(items) == 0:
        return "No todos for today! :)"
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
        return text
            

def check_task():
    if len(argv) >= 3:
        try:
            check_index = int(argv[2])
            with open(todo_file,"r+") as f:
                fr = f.readlines()
                f.seek(0)
                if len(fr) >= check_index:
                        for line_index in range(len(fr)):
                            line = fr[line_index]
                            if check_index == line_index + 1:
                                line = line.replace('0', '1')
                            f.write(line)
                        f.truncate()
                        return 'Checked'
                else:
                    return 'Unable to check: index is out of bound'
        except:
            return "Unable to check: index is not a number"
    else:
        return "Unable to check: no index provided"


def print_usage():
    return 'Command line arguments: \n-l   Lists all the tasks\n-a   Adds a new task\n-r   Removes an task\n-c   Completes an task'


def controller():
    arguments = get_arguments()
    if not arguments:
        return print_usage()
    elif arguments[0] == "-l":
        return print_items()
    elif arguments[0] == "-c":
        return check_task()
    elif arguments[0] == "-r":
        return delete_item()
    elif arguments[0] == "-a":
        return add_task()
        
print(controller())