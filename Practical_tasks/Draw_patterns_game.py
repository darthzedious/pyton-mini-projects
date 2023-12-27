print('Pattern Drawing Program')
print()
print('Menu:')
print('1. Draw a Triangle')
print('2. Draw a Rectangle')
print('3. Draw a Pyramid')
print('4. Quit')
print()
choice = int(input('Enter your choice (1/2/3/4): '))
print()
while choice != 4:
    if choice == 1:
        number_of_rows = int(input('Enter the number of rows for the triangle: '))
        direction = input("Enter 'u' for upward or 'd' for downward: ")
        print()
        if direction == 'u':
            for i in range(number_of_rows):
                for j in range(number_of_rows - 1):
                    print(end='')
                for j in range(i + 1):
                    print('*', end='')
                print()
        elif direction == 'd':
            for i in range(number_of_rows, 0, -1):
                for j in range(number_of_rows + 1):
                    print(end='')
                for j in range(i):
                    print('*', end='')
                print()
    elif choice == 2:
        number_of_rows = int(input('Enter the number of rows for the rectangle: '))
        number_of_columns = int(input('Enter the number of columns for the rectangle: '))
        print()
        for i in range(number_of_rows):
            print(end='')
            for j in range(number_of_columns):
                print('*', end='')
            print()
    elif choice == 3:
        number_of_rows = int(input("Enter the number of rows for the pyramid: "))
        print()
        k = 0

        for i in range(1, number_of_rows + 1):
            for space in range(1, (number_of_rows - i) + 1):
                print(end="  ")

            while k != (2 * i - 1):
                print("* ", end="")
                k += 1

            k = 0
            print()
    elif choice == 4:
        break
    print()
    choice = int(input('Enter your choice (1/2/3/4): '))
    print()

print()
print('Goodbye!')
