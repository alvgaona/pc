def count_A(word: str) -> int:
    count = 0
    for letter in word:
        if letter.lower() == 'a':
            count += 1

    return count


def main():
    print(count_A("Argentina"))


if __name__ == '__main__':
    main()
