if __name__ == "__main__":
    try:
        n = int(input())
        m = n
        r = 0
        while n > 0:
            last_digit = n % 10
            r = r * 10 + last_digit
            n //= 10
        if m == r:
            print("Palindrome", end="")
        else:
            print("Not Palindrome", end="")
    except EOFError:
        pass
