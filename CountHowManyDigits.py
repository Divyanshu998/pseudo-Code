def counter(num, d):
    count = 0
    while num > 0:
        last_digit = num % 10
        if last_digit == d:
            count += 1
        num //= 10
    print(count)

if __name__ == "__main__":
    try:
        # Reading num and d from space-separated input or multiple lines
        input_str = sys.stdin.read().split()
        if len(input_str) >= 2:
            num = int(input_str[0])
            d = int(input_str[1])
            counter(num, d)
    except Exception:
        pass

import sys
