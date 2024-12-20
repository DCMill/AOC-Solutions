def get_reports():
    with open("day_2_input.txt",'r') as f:
        reports = f.readlines()
        parsed_reports = []
        for report in reports:
            parsed_report = report.split(" ")
            parsed_report = list(map(int, parsed_report))
            parsed_reports.append(parsed_report)
    return parsed_reports
def isSafe(report: list[int]):
    mistakes = 0
    isIncreasing = True if report[0] < report[1] else False
    for (index, number) in enumerate(report):
        if index > 0:
            if (number > report[index-1] and isIncreasing == True) or (number < report[index-1] and isIncreasing == False):
                if abs(number - report[index-1]) > 3:
                    mistakes += 1
            else:
                mistakes += 1
    return mistakes
def task1():
    reports = get_reports()
    safe_reports = 0
    for report in reports:
        if isSafe(report) == 0:
            safe_reports += 1
    return safe_reports

def task2():
    reports = get_reports()
    safe_reports = 0
    for report in reports:
        if isSafe(report) <2:
            safe_reports += 1
    return safe_reports
print(task2())
