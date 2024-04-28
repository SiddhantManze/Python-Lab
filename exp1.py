start = int(input("Enter the start of range : "))
end = int(input("Enter the end of range : "))

print("\nThe Odd Numbers from", start, "to", end)
for num in range(start, end + 1):
    if num % 2 != 0:
        print(num)

print("\nThe Even Numbers from", start, "to", end)
for num1 in range(start, end + 1):
    if num1 % 2 == 0:
        print(num1)

