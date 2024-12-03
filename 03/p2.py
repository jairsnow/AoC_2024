import re

with open('raw_input.txt', 'r') as file:
    file_content = file.read()

    # Lol, is a small one, but I'm proud to have reached a point in my life where I'm able to do regex without any AI support XD
    pattern = r'mul\((\d{1,3}),(\d{1,3})\)|(do\(\))|(don\'t\(\))'

    matches = re.findall(pattern, file_content)

    sum = 0
    do_enabled = True

    for match in matches:

        if match[2] == "do()":
            do_enabled = True
        elif match[3] == "don't()":
            do_enabled = False
        else:
            if do_enabled: 
                print(match)
                sum += int(match[0])*int(match[1])
    
    print(sum)
