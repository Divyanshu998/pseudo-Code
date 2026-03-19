if __name__ == "__main__":
    x = 259
    if x % 9 == 5:
        print("0")
    elif x % 9 == 0:
        print("9")
    else:
        print(x % 9)
