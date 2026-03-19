a = 5
b = 9
c = 2

def funn(a, b, c):
    for i in range(4, 9):
        a = (a + b) // b
        a = (c + b) + a

    b = (5 + 10) + a
    a = (10 + b) + a
    for c in range(2, 6):
        a = (c - 2) * a
        b = (3 * c) + a

    return a + b


result = funn(a, b, c)
print(result)