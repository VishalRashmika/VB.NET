marks = [0, 0, 0, 0, 0]
for i in range(0,5):
    mark = int(input(f"Enter mark: "))
    marks[i] = mark

for mark in marks:
    if mark > 75:
        print("A")
    elif mark >= 65 and mark <= 75:
        print("B")
    elif mark >= 55 and mark <= 64:
        print("C")
    elif mark >= 45 and mark <= 54:
        print("S")
    elif mark < 45:
        print("F")