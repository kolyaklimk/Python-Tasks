import my_container

if __name__ == "__main__":
    while True:
        username = input("Enter username: ")
        if len(username) != 0:
            break

    container = my_container.MyContainer(username)
    method_list = [method for method in dir(container) if method.startswith('__') is False]
    method_list.append('exit')

    while True:
        command = input(f'\nCommands: {method_list} \nEnter command: ')
        tokens = command.strip().split(' ')

        match tokens[0]:
            case "add":
                if len(tokens) == 1:
                    print('Error! Write <command> <value...>')
                    continue
                container.add(*tokens[1:])
            case "remove":
                if len(tokens) == 1:
                    print('Error! Write <command> <value...>')
                    continue
                container.remove(tokens[1])
            case "find":
                if len(tokens) == 1:
                    print('Error! Write <command> <value...>')
                    continue
                container.remove(*tokens[1:])
            case "list":
                container.list()
            case "grep":
                if len(tokens) == 1:
                    print('Error! Write <command> <value...>')
                    continue
                container.grep(tokens[1])
            case "save":
                container.save()
            case "load":
                container.load()
            case "switch":
                if len(tokens) == 1:
                    print('Error! Write <command> <value...>')
                    continue
                container.switch(tokens[1])
            case "exit":
                if input(f'Save {container.username} container?(y/n)') == 'y':
                    container.save()
                exit()
            case _:
                print('No such command!')
