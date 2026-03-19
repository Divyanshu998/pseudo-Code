if __name__ == "__main__":
    a = 7
    b = 10
    c = 9
    for i in range(3, 5):
        a = b
        if (b - a + i) < (c + b):
            continue
        else:
            break
    print(a + b)
