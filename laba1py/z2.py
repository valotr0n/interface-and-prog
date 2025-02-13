with open('numbers.txt', 'r') as file:
    content = file.readlines()

new_content = []
for line in content:
    numbers = line.split('.')
    new_numb = []
    for number in numbers:
        if number.isdigit():
            if int(number)%2 == 0:
                new_numb.append('0')
            else:
                new_numb.append(number)
    new_content.append('.'.join(new_numb))

file = open('numbers1.txt', 'w')
file.write(str(new_content))
file.close()

            
