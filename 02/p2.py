class ReportDirection():
    def __init__(self):
        self.unknown = 0
        self.increasing = 1
        self.decreasing = 2

class ReportResponse:
    def __init__(self):
        self.report_is_safe = False
        self.report_failed_index = 0

def get_report_direction(levels) -> ReportDirection:
    
    increasing = 0
    decreasing = 0
    for i, level in enumerate(levels):

        perv_level = levels[i-1]
        
        if level > perv_level:
            increasing += 1

        if level < perv_level:
            decreasing += 1

    if increasing > decreasing:
        return ReportDirection().increasing
    elif decreasing > increasing:
        return ReportDirection().decreasing
    else:
        return ReportDirection().unknown

def analyze_report(levels) -> ReportResponse:
    
    report_response = ReportResponse()
    report_direction = get_report_direction(levels)

    if report_direction == ReportDirection().unknown:
        report_response.report_failed_index = -1
        return report_response
    
    for i, level in enumerate(levels):

        if i == 0:
            continue

        perv_level = levels[i-1]
        direction = 0
        level_difference =  abs(level - perv_level)

        # Unsafe report conditions
        if level_difference > 3 or level_difference < 1:
            report_response.report_failed_index = i
            return report_response
        
        if level > perv_level:
            # increasing
            direction = ReportDirection().increasing

        if level < perv_level:
            # decreasing
            direction = ReportDirection().decreasing
        
        if report_direction == 0:
            report_direction = direction
        
        if report_direction != direction:
            report_response.report_failed_index = i
            return report_response
        
    report_response.report_is_safe = True
    return report_response


safe_report = 0
bad_reports = 0
with open('raw_input.txt', 'r') as file:
    for report in file:

        levels = report.strip().split(" ")
        # Cast everything as int so I don't have to deal with it later
        levels = [int(level) for level in levels]

        ### First analysis
        report1 = analyze_report(levels)
        if report1.report_is_safe == True:
            safe_report += 1
            continue
        
        # So, if the report is not good, the issue could be in one of the 2 numbers that I'm confornting
        # It could the current number/index of the pervious one

        # Check removing the current index that gave me the error
        levels2 = levels.copy()
        levels2.pop(report1.report_failed_index)
        
        report2 = analyze_report(levels2)
        if report2.report_is_safe == True:
            safe_report += 1
            continue

        # Check again the result removing the number/index before the one that gave me the error
        # There are edge cases like this one => 34 33 34 35 38 41 42 45, where it should increasing, I detect the error
        # on the number 33, because is decreasing but the issue is the first 34, that should notbe there
        levels3 = levels.copy()
        levels3.pop(report1.report_failed_index-1)

        report3 = analyze_report(levels3)
        if report3.report_is_safe == True:
            safe_report += 1
            continue

print(safe_report)





