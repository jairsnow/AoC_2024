
safe_report = 0
with open('raw_input.txt', 'r') as file:
    for report in file:
        levels = report.strip().split(" ")
        
        if len(levels) < 2:
            print("There is a report has less than 2 elements :/")
            exit()

        report_direction = 0
        good_report = True

        for i, _level in enumerate(levels):

            if i == 0:
                continue

            level = int(_level)
            perv_level = int(levels[i-1])

            direction = 0
            level_difference =  abs(level - perv_level)
            
            # Unsafe report conditions
            if level_difference > 3 or level_difference < 1:
                good_report = False
                break
            
            if level > perv_level:
                # increasing
                direction = 1

            if level < perv_level:
                # decreasing
                direction = 2
            
            if report_direction == 0:
                report_direction = direction
            
            if report_direction != direction:
                good_report = False
                break
            
        if good_report:
            safe_report += 1

print(safe_report)





