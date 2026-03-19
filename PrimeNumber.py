import math

def is_prime(n):
    if n == 1:
        return False
    if n == 2:
        return False
    else:
        for i in range(2, int(math.sqrt(n))):
            if n % i == 0:
                return False
    return True

if __name__ == "__main__":
    try:
        n = int(input())
        print(is_prime(n))
    except EOFError:
        pass
