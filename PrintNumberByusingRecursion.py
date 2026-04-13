def print_numbers(n):
    if n > 100:
        return

    print(n)
    print_numbers(n + 1)

num = int(input("Enter the number: "))
print_numbers(num)

