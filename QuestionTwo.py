if __name__ == "__main__":
    a = 2
    b = 5
    c = 10
    for i in range(3, 7):
        a = (a + a) + a
        a = (a ^ 11) + i
    b = (9 + 7) + a
    print(a + b)
