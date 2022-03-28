# %%

num1 = 100
g = 20
g = (g + num1/g) / 2
g = (g + num1/g) / 2
g = (g + num1/g) / 2
g = (g + num1/g) / 2
g = (g + num1/g) / 2
print(g)

num2 = 10000
g = 20
g = (g + num2/g) / 2
g = (g + num2/g) / 2
g = (g + num2/g) / 2
g = (g + num2/g) / 2
g = (g + num2/g) / 2
print(g)

num3 = 16
g = 20
g = (g + num3/g) / 2
g = (g + num3/g) / 2
g = (g + num3/g) / 2
g = (g + num3/g) / 2
g = (g + num3/g) / 2
print(g)

num4 = 81
g = 20
g = (g + num4/g) / 2
g = (g + num4/g) / 2
g = (g + num4/g) / 2
g = (g + num4/g) / 2
g = (g + num4/g) / 2
print(g)

# %%


def heron(objective, initial):
    g = initial
    g = (g + objective/g) / 2
    g = (g + objective/g) / 2
    g = (g + objective/g) / 2
    g = (g + objective/g) / 2
    g = (g + objective/g) / 2

    return g


print(heron(100, 20))
print(heron(10000, 20))
print(heron(16, 20))
print(heron(81, 20))

# %%


def heron(objective, initial):
    g = initial

    g = heron_iteration(g, objective)
    g = heron_iteration(g, objective)
    g = heron_iteration(g, objective)
    g = heron_iteration(g, objective)
    g = heron_iteration(g, objective)

    return g


def heron_iteration(g, objective):
    return (g + objective/g) / 2


print(heron(100, 20))
print(heron(10000, 20))
print(heron(16, 20))
print(heron(81, 20))

# %%


def heron(objective: float, initial: float, n: int):
    g = initial

    for i in range(0, n):
        g = (g + objective/g) / 2
        print("Hello")

    return g


print(heron(100, 20, 100))
#print(heron(10000, 20, 5))
#print(heron(16, 20, 5))
#print(heron(81, 20, 5))
