name = "John"


def func1():
    print(name)


def greet(name: str) -> str:
    return f'Hello, {name}'


def main():
    name = 'Mike'
    print(greet(name))


if __name__ == '__main__':
    main()
