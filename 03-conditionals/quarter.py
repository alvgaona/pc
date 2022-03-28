def ask_for_month():
    return int(input("Insert month: "))


def quarter(month):
    if month <= 3:
        return "Q1"
    elif month <= 6:
        return "Q2"
    elif month <= 9:
        return "Q3"
    elif month <= 12:
        return "Q4"


def main():
    month = ask_for_month()

    while month < 1 or month > 12:
        month = ask_for_month()

    q = quarter(month)

    print(f"Usted esta en el {q}")


if __name__ == '__main__':
    main()
