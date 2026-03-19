if __name__ == "__main__":
    a = 7
    b = 8
    c = 9
    if (a ^ b ^ c) < (b + c + a):
        b = 6 + a
    a = 8 ^ b
    print(a + b + c)
