def is_palindrome(num):
    # Note: Function name from Java source is isPalindrome, 
    # but logic is for Armstrong number.
    sum_val = 0
    num1 = num
    while num > 0:
        last_digit = num % 10
        sum_val += last_digit * last_digit * last_digit
        num //= 10
    return num1 == sum_val

if __name__ == "__main__":
    try:
        n = int(input())
        print(is_palindrome(n))
    except EOFError:
        pass
