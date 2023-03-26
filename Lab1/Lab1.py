def calculator(num1, num2, operation):
    match operation:
        case "add":
            return num1 + num2
        case "sub":
            return num1 - num2
        case "mult":
            return num1 * num2
        case "div": 
            if num2 == 0:
                return "div by 0"
            return num1 / num2
    return "Error"


def even_list(list_of_nums):
    return [even_num for even_num in list_of_nums if even_num % 2 == 0]


print(calculator(32, 51, "add"))
print(calculator(143, 252, "sub"))
print(calculator(623, 23, "mult"))
print(calculator(35, 23, "div"))
print(calculator(35, 0, "div"))
print(calculator(23, 6, "qwe"))

print(even_list([num for num in range(1, 10)]))

print('Hello world')
