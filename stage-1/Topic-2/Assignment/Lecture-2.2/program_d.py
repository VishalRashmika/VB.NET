total_sum = 0

while True:
    number = int(input(f"Enter mark: "))
    if number == -999:
        break
    else:
        total_sum += number
print(total_sum)