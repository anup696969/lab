d = {}
new = {}

n = int(input("How many students? "))
for i in range(n):
    m = []
    key = input(f"Enter the name of student {i+1}: ")
    print(f"Enter the marks in three subjects of {key}:")
    for j in range(1, 4):
        m.append(int(input(f"Mark {j}: ")))
    d[key] = m

for key in d:
    avg = round(sum(d[key]) / 3, 3)
    new[key] = avg

print("\nThe average of marks of the students is:")
print(new)

update = input("\nDo you want to update marks of any student? (y/n): ").lower()

while update == 'y':
    student = input("Enter the name of the student whose marks you want to update: ")
    if student in d:
        print(f"Current marks for {student}: {d[student]}")
        new_marks = []
        print("Enter the new marks for three subjects:")
        for i in range(1, 4):
            mark = int(input(f"Mark {i}: "))
            new_marks.append(mark)
        d[student] = new_marks
        avg = round(sum(new_marks) / 3, 2)
        new[student] = avg
        print(f"Marks and average updated for {student}!")
    else:
        print("Student not found.")
    update = input("\nDo you want to update marks of another student? (y/n): ").lower()

print("\nUpdated marks dictionary:")
print(d)

print("\nUpdated averages dictionary:")
print(new)

sorted_new = dict(sorted(new.items(), key=lambda item: item[1]))
print(sorted_new)
topper = max(new, key=lambda k: new[k])
print(f"\nStudent with highest marks is: {topper}")
print(f"Their average is: {new[topper]:.2f}")