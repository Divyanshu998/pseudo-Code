def funn(a, b, c):
    if (a + 3) < (b - 2):
        c = 4 + b
        b = (c + c) + b
    else:
        c = (a + 3) ** 2
        c = (10 + 8) + b

    return a + b + c


print(funn(9, 7, 20))