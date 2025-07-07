a = []
b = []

n = int(input("Enter the value of n: "))
for i in range(1, n + 1):
    num = int(input(f"Enter {i} number: "))
    a.append(num)
unique = []
for i in a:
    if i not in unique:
        unique.append(i)
maximum = unique[0]
minimum = unique[0]
for j in unique:
    if j > maximum:
        maximum = j
    if j < minimum:
         minimum = j
print(f"Maximum number is = {maximum}")
print(f"Minimum number is = {minimum}")


# Sort the unique list using bubble sort
for i in range(len(unique)):
    for j in range(0, len(unique) - i - 1):
        if unique[j] > unique[j + 1]:
            temp = unique[j]
            unique[j] = unique[j + 1]
            unique[j + 1] = temp

print("Sorted list of unique numbers (original list without duplicates):")
print(unique)
