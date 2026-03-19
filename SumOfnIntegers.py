def sum_n_integers(n):
    sum_val = 0
    for i in range(1, n + 1):
        sum_val += i
    return sum_val

if __name__ == "__main__":
    n = int(input())
    print(sum_n_integers(n))
