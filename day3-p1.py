from string import punctuation

with open('day3-input.txt', 'r') as file:
    puzzle_input = file.read()


full_results_list = []
line = puzzle_input.split()
for row in range(1,len(puzzle_input.split())-1):
    print(row)
    line_results_list = []
    for col in range(len(line[1])):
        if line[row][col] in punctuation and line[row][col] != '.':
            # print(line[row-1][col-1], line[row-1][col], line[row-1][col+1])
            # print(line[row][col-1], line[row][col], line[row][col+1])
            # print(line[row+1][col-1], line[row+1][col], line[row+1][col+1])

            for row2 in [-1, 0, 1]:
                for col2 in [-1, 0, 1]:
                    if line[row+row2][col+col2].isdigit():

                        # look right
                        i = 0
                        num_string1 = ""
                        while line[row+row2][col+col2+i].isdigit():
                            num_string1 += line[1+row2][col+col2+i]
                            i += 1
                        #print(num_string1)

                        # look left
                        j = 0
                        num_string2 = ""
                        while line[row+row2][col+col2-j].isdigit():
                            num_string2 += line[row+row2][col+col2-j]
                            j += 1
                        #print(num_string2)
                        num_string2 = num_string2[::-1]

                        if len(num_string1) > len(num_string2):
                            if num_string1 not in line_results_list:
                                line_results_list.append(num_string1)
                        elif len(num_string2) > len(num_string1):
                            if num_string2 not in line_results_list:
                                line_results_list.append(num_string2)
                        
    #print(line_results_list)
    full_results_list.append(line_results_list)

print(full_results_list)
        