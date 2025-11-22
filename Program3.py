a = int(input("Enter a: "))

# If even, reduce by 1 to get last odd number
if a % 2 == 0:
    a = a - 1

for i in range(1, a+1, 2):
    print(i, end=" ")