if __name__ == "__main__":
    p = 0
    q = 2
    r = 9
    r = 7 + p
    q = q + r
    for i in range(4, 8):
        p = (p + p) & q
        if (p + q) < (r - p) or (8 < p):
            p = (p + 2) + q
            break
    print(p + q)
