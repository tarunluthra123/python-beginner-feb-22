def main():
    x = int(input())
    y = int(input()) 
    z = int(input())
    
    if x < y and x < z:
        print(x)
    elif y < z:
        print(y)
    else:
        print(z)
    
    

    return 0

if __name__ == '__main__':
    main()