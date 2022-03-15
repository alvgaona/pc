"""
Computar la suma geométrica:
    Sumatoria de 0 a n del término a * r ** k
"""



def main():
    sum = geometric_sum(1, 1, 10)

    print(sum * 2)
    
    
def geometric_sum(a: float, r: float, n: int):
    sum = 0
    for k in range(0, n):
        sum += a * r ** k

    return sum

if __name__ == '__main__':
    main()
