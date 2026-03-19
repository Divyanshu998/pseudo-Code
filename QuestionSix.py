if __name__ == "__main__":
    x = 10
    y = 16
    z = 3
    if x > y:
        x = 2 * y
    else:
        y = x // 2
    
    if z > y:
        z = 2 * y
    else:
        y = z // 2
    
    print(x + y + z)
