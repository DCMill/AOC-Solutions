def get_text():
    with open("day_4_input.txt","r") as f:
        return f.readlines()

def task1():
    input = get_text()
    total_xmas = 0
    def get_horizontals(i,j):
        count = 0
        left_string = ""
        right_string = ""
        total_col = len(input)
        total_rows = len(input[i])
        if j+3 < total_rows:
            right_string = "".join([input[i][j],input[i][j+1],input[i][j+2],input[i][j+3]])
        if j-3 >= 0:
            left_string = "".join([input[i][j],input[i][j-1],input[i][j-2],input[i][j-3]])
        if left_string == "XMAS":
            count += 1
        if right_string == "XMAS":
            count += 1
         
        return count
    def get_verticals(i,j):
        count = 0
        bottom_string = ""
        top_string = ""
        total_col = len(input)
        total_rows = len(input[i])
        if i+3 < total_col:
            top_string = "".join([input[i][j],input[i+1][j],input[i+2][j],input[i+3][j]])
        if i-3 >= 0:
            bottom_string = "".join([input[i][j],input[i-1][j],input[i-2][j],input[i-3][j]])
        if top_string == "XMAS":
            count += 1
        if bottom_string == "XMAS":
            count += 1
        return count
    def get_diagonals(i,j):
        total_col = len(input)
        total_rows = len(input[i])
        count = 0
        possibilities = []
        if i+3<total_col and j+3<total_rows:
            possibilities.append("".join([input[i][j],input[i+1][j+1],input[i+2][j+2],input[i+3][j+3]]))
        if i+3<total_col and j-3>=0:
            possibilities.append("".join([input[i][j],input[i+1][j-1],input[i+2][j-2],input[i+3][j-3]]))
        if i-3 >= 0 and j+3 < total_rows:
            possibilities.append("".join([input[i][j],input[i-1][j+1],input[i-2][j+2],input[i-3][j+3]]))
        if i-3 >= 0 and j-3 >= 0:
            possibilities.append("".join([input[i][j],input[i-1][j-1],input[i-2][j-2],input[i-3][j-3]]))
        for possibility in possibilities:
            if possibility == "XMAS":
                count += 1
        return count
    for i in range(len(input)):
        for j in range(len(input[i])):
            if input[i][j] == "X":
                total_xmas += (get_diagonals(i,j)+get_horizontals(i,j)+get_verticals(i,j))
                
    return total_xmas

def task2():
    input = get_text()
    mases = 0
    def get_x(i,j):
        right_x = ""
        left_x = ""
        total_col = len(input)
        total_rows = len(input[i])
        if (total_rows-1 > j > 0) and (total_col-1 > i > 0):
            right_x = "".join([input[i+1][j+1],input[i][j],input[i-1][j-1]])
            left_x = "".join([input[i+1][j-1],input[i][j],input[i-1][j+1]])
        if (right_x == "MAS" or right_x == "SAM") and (left_x == "MAS" or left_x == "SAM"):
            return 1
        else:
            return 0
    for i in range(len(input)):
        for j in range(len(input[i])):
            if input[i][j] == "A":
                mases += get_x(i,j)
    return mases
print(task2())

