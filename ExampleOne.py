if __name__ == "__main__":
    x = 15
    y = 12
    y = x - 1
    while True:
        print(x)
        x = y + (x - 2)
        if not (x < 40):
            break
