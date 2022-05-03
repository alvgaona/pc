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

    if type(ip) != str and ip == "":
        return result
    
    if ip_is_invalid(ip):
        raise ValueError("Invalid IP address")

    for letter in ip:
        if letter == '.':
            result += '[.]'
        else:
            result += letter
    
    return result


def find_max(a_list: List[int]) -> int:
    max_value = a_list[0]
    for value in a_list:
        if value > max_value:
            max_value = value
    return max_value


def ip_is_invalid(ip: str) -> bool:
    ip_values = ip.split('.')
    
    for value in ip_values:
        if int(value) < 0 or int(value) > 255:
            return True

    return False


if __name__ == '__main__':
    print(find_max([-1, 4, 5, -0.5]))