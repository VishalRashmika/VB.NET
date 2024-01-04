marks = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for i in range(0,10):
    mark = int(input("Enter marks: "))
    marks[i] = mark
print(f"Maximum: {max(marks)}")
print(f"Minimum: {min(marks)}")
print(f"Average: {sum(marks)/len(marks)}")