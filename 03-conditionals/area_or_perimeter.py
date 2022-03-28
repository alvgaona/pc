def area_or_perimeter(w: float, h: float) -> float:
    if w == h:
        return w * h
    else:
        return 2*w + 2*h


def main():
    print(area_or_perimeter(3, 3))


if __name__ == '__main__':
    main()
