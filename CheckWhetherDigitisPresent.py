import sys

def is_present(num, d):
    found = False
    while num > 0:
        last_digit = num % 10
        if last_digit == d:
            found = True
            break
        num //= 10 # Added this from pseudo-code to avoid infinite loop
    return found

if __name__ == "__main__":
    try:
        input_data = sys.stdin.read().split()
        if len(input_data) >= 2:
            num = int(input_data[0])
            d = int(input_data[1])
            print(is_present(num, d))
    except Exception:
        pass
