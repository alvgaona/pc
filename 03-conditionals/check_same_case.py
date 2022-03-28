def is_uppercase(letter: str):
    return True if 65 <= ord(letter) <= 90 else False


def is_lowercase(letter: str):
    return True if 97 <= ord(letter) <= 122 else False


def check_same_case(first: str, second: str) -> bool:
    if is_uppercase(first) and is_uppercase(second):
        return True

    if is_lowercase(first) and is_lowercase(second):
        return True

    return False


def main():
    same_case = check_same_case('?', '?')
    print(same_case)


if __name__ == '__main__':
    main()
