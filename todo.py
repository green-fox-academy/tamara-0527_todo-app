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
        dictionary['task'] = task[:-1]
        items.append(dictionary)
    return items


todo = argv[0]

def get_arguments():
    arguments = argv[1:]
    list_of_arguments = ['-a', '-r', '-c', '-l']
    if len(arguments) == 0:
        return False
    if arguments[0] in list_of_arguments:
        return arguments
    else:
        return False
    
def controller():
    arguments = get_arguments()
    if not arguments:
        print("usage")
    elif arguments[0] == "-l":
        todos = import_file('todos.txt')
        print(todos)
    elif arguments[0] == "-c":
        print("completed")
    elif arguments[0] == "-r":
        print("remove")
    elif arguments[0] == "-a":
        print("add")

controller()
        

