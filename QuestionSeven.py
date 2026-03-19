if __name__ == "__main__":
    x = 8
    y = 6
    z = 4
    if x > y:
        x = y
    else:
        y = x
    
    if z > y:
        z = y
    else:
        y = z
    
    print(x + y + z)
