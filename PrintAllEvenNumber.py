def print_even(n):
    for i in range(0, n + 1):
        if i % 2 == 0:
            print(i)

if __name__ == "__main__":
    import sys
    # Using input() for simplicity, matching Scanner sc.nextInt()
    try:
        n = int(input())
        print_even(n)
    except EOFError:
        pass
