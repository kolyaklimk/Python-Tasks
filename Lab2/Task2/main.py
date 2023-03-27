import my_container

if __name__ == "__main__":
    username = input("Enter username: ")
    container = my_container.MyContainer(username)
    method_list = [method for method in dir(container) if method.startswith('__') is False]
    method_list.append('exit')
    
    while True:
        print(method_list)
