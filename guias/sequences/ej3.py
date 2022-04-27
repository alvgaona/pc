def count(text: str, character: str) -> int:
    count = 0
    for letter in text:
        if letter.lower() == character:
            count += 1

    return count


def main():
    print(len("Esto es un texto"))


if __name__ == '__main__':
    main()
