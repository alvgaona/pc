def good_way(ip):
    ip = ip.replace('.', '[.]')

    return ip


def other(ip):
    ip = ip.split('.')

    return '[.]'.join(ip)


def not_so_good(ip):
    result = ""

    for letter in ip:
        if letter == '.':
            result += '[.]'
        else:
            result += letter

    return result


def main():
    ip = '192.168.0.1'

    #ip = good_way(ip)
    #ip = not_so_good(ip)

    #print(ip)


if __name__ == '__main__':
    main()
