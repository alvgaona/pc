def greet_msg(name):
    return "Hello, " + name


def greet():
    name = input("Ingrese nombre: ")
    msg = greet_msg(name)
    print(msg)


greet()
