def father_son(father_age: int, son_age: int) -> int:
    return abs(father_age - son_age * 2)

def main():
    print(father_son(28, 2))


if __name__ == '__main__':
    main()
