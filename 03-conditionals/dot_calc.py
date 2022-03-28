def calculator(txt):
    first = 0
    second = 0
    op = None
    
    for value in txt:
        if value == '.' and op is None:
            first += 1
        
        if value == '+' or value == '-' or value == '/' or value == '*':
            op = value
        
        if value == '.' and op is not None:
            second += 1
            
    if op == '+':
        return (first + second) * '.'
    elif op == '-':
        return (first - second) * '.'
    elif op == '/':
        return (first // second) * '.'
    elif op == '*':
        return (first * second) * '.'

if __name__ == '__main__':
    print(calculator('. - ...'))
