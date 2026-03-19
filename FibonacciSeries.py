def fibonacci(n):
    sum_val = 0
    prev = 0
    next_val = 1
    while n >= 0:
        sum_val = prev + next_val
        prev = next_val
        next_val = sum_val
        n -= 1
    print(sum_val)

if __name__ == "__main__":
    try:
        n = int(input())
        fibonacci(n)
    except EOFError:
        pass
