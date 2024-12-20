import re

def get_text():
    with open("day_3_input.txt",'r') as f:
        return f.read()
def task1():
    pattern = r"mul\([0-9]+,[0-9]+\)"
    input = get_text()
    occurences = re.findall(pattern=pattern, string=input)
    sum = 0
    for occurence in occurences:
        extracted_numbers = occurence.replace("mul(","").replace(")","").split(",")
        extracted_numbers = [int(number) for number in extracted_numbers]
        sum += (extracted_numbers[1]*extracted_numbers[0])
    return sum


def task2():
    pattern = r"do\(\)|don't\(\)|mul\(\d+,\d+\)"
    input = get_text()
    occurences = re.findall(pattern,input)
    do = True
    sum = 0
    for occurence in occurences:
        if occurence == "do()":
            do = True
        elif occurence == "don't()":
            do = False
        else:
            if do == True:
                extracted_numbers = occurence.replace("mul(","").replace(")","").split(",")
                extracted_numbers = [int(number) for number in extracted_numbers]
                sum += (extracted_numbers[1]*extracted_numbers[0])
    return sum
print(task2())

