
def get_numbers():
    with open("day_1_input.txt", "r") as input:
        string = input.readlines()
        numbers = []
        for line in string:
            numbers.append((int(line.split("   ")[0]),int(line.split("   ")[1])))
        print(numbers)
        numbers = list(zip(*numbers))
        sorted_list1 = sorted(numbers[0])
        sorted_list2 = sorted(numbers[1])
        sorted_pairs = zip(sorted_list1, sorted_list2)
        return sorted_pairs, numbers
def task1():
    sorted_pairs,numbers = get_numbers()
    distance = 0
    for pair in sorted_pairs:
        distance += abs(pair[1] - pair[0])
    return distance
print(task1())
def task2():
    sorted, normal = get_numbers()
    similarity = 0
    def get_num_occurences(number,selected_list):
        return len([index for index in range(len(selected_list)) if selected_list[index] == number])
    for number in normal[0]:
        similarity += get_num_occurences(number,normal[1]) * number
    return similarity
print(task2())
