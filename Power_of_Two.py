num = int(input("Enter A Number: "))

if num < 0:  # Check if it's a negative number
    print('Negative Number')
elif num == 1:
    print('True')  # 1 is a power of 2 (2^0)
else:
    while num % 2 == 0:
        num = num / 2  # Keep dividing by 2

    if num == 1:
        print('True')  # If we reach 1, it's a power of 2
    else:
        print('False')  # Otherwise, it's not a power of 2
