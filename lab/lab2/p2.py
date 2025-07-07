a=[]
b=[]
n=int(input("Enter the value of n for first list"))
m=int(input("enter the value of m for second list"))
print("Enter first list:\n")
for i in range(1,n+1):
    a.append(int(input(f"Enter {i} number")))
print("Enter second list")
for i in range(1,m+1):
    b.append(int(input(f"Enter {i} number")))
merged=a + b
print(list(set(merged)))

