with open('date.txt', 'r') as file:
    content = file.readlines()

days = []
months = []

for line in content:
    day, month, year = line.split('/')
    days.append(int(day))
    months.append(int(month))


file2 = open('day.txt', 'w')
file2.write('\n'.join(map(str, reversed(days))))
file2.close()


file3 = open('month.txt', 'w')
file3.write(str(month))
file3.close()
