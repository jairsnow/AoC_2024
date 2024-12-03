import re

with open('raw_input.txt', 'r') as file:
    file_content = file.read()

    # Lol, is a small one, but I'm proud to have reached a point in my life where I'm able to do regex without any AI support XD
    pattern = r'mul\((\d{1,3}),(\d{1,3})\)'

    matches = re.findall(pattern, file_content)

    sum = 0
    for match in matches:
        sum += int(match[0])*int(match[1])
    
    print(sum)
