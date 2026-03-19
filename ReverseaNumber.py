if __name__ == "__main__":
    n = int(input())
    r = 0
    while n > 0:
        last_digit = n % 10
        r = r * 10 + last_digit
        n //= 10
    print(r)
