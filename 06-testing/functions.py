from typing import List, Any

def reverse_list(one_list: List[Any]) -> List[Any]:
    tail = 0
    head = len(one_list) - 1

    while tail < head:
        aux = one_list[head]
        one_list[head] = one_list[tail]
        one_list[tail] = aux

        tail += 1
        head -= 1

    return one_list


def format_ip_address(ip: str) -> str:
    result = ""

    for letter in ip:
        if letter == '.':
            result += '[.]'
        else:
            result += letter
    
    return result


def find_max(a_list: List[int]) -> int:
    max_value = 0
    for value in a_list:
        if value > max_value:
            max_value = value
    return max_value
