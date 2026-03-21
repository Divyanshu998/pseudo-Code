def palindrome(n):
    b = 0
    x = n
    while x > 0:
        a = x % 10
        x = x // 10
        b = b * 10 + a
    if b == n:
        print("Palindrome")
    else:
        print("Not a Palindrome")
palindrome(121)

