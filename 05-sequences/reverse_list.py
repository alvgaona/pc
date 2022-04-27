"""
Write a function that takes a list as an argument and returns the list in reverse order.

Example:

Input -> [4, 9, 44, 21]
Output -> [21, 44, 9, 4]
"""


def reverse_list(one_list):
    output = []

    for i in range(len(one_list) - 1, -1, -1):
        output.append(one_list[i])

    return output


def reverse_optimized(one_list):
    left = 0
    right = len(one_list) - 1

    while left < right:
        aux = one_list[right]
        one_list[right] = one_list[left]
        one_list[left] = aux

        left += 1
        right -= 1

    return one_list


def main():
    one_list = [1, 2, 3, 4]
    output = reverse_optimized(one_list)
    print(output)


if __name__ == '__main__':
    main()
