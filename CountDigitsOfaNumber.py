def counter(num):
    count = 0
    while num > 0:
        num //= 10
        count += 1
    return count

if __name__ == "__main__":
    num = 789456
    print(counter(num))
