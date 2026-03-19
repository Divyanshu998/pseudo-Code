if __name__ == "__main__":
    a = 4
    b = 4
    c = 4
    # Fixed the condition from Java code a&b(b^b)&c to a & (b ^ b) & c as per pseudo-code
    if a & (b ^ b) & c:
        a >>= 1
    print(a + b + c)
