def reverse(n):
    b = 0
    x = n

    while x > 0:
        a = x % 10
        x = x // 10
        b = b * 10 + a

    return b

print(reverse(1234))