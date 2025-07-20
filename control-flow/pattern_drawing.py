size = int(input("Enter the size of the pattern: "))
symbol = "*"

for x in range (size):
    for y in range(size):
        print(symbol, end="")
    print()