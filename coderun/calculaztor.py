def main():
    x, y, z = map(int, input().split())
    N = input().strip()
    
    available_digits = {x, y, z}
    missing_digits = set()
    
    for digit in N:
        if int(digit) not in available_digits:
            missing_digits.add(int(digit))
    
    print(len(missing_digits))

if __name__ == '__main__':
    main()