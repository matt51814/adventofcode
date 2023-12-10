from string import punctuation

with open('day3-input.txt', 'r') as file:
    puzzle_input = file.read()


full_results_list = []
line = puzzle_input.split()
for row in range(1,len(puzzle_input.split())-1)[:1]:
    line_results_list = []
    prev_line_results = []
    for col in range(len(line[row])):
        if line[row][col] in punctuation and line[row][col] != '.':
            # print(line[row-1][col-1], line[row-1][col], line[row-1][col+1])
            # print(line[row][col-1], line[row][col], line[row][col+1])
            # print(line[row+1][col-1], line[row+1][col], line[row+1][col+1])
            for row2 in [-1, 0, 1]:
                for col2 in [-1, 0, 1]:
                    if line[row+row2][col+col2].isdigit():
                        # look right
                        i = 0
                        right_moves = []
                        num_string1 = ""
                        while line[row+row2][col+col2+i].isdigit():
                            num_string1 += line[row+row2][col+col2+i]
                            i += 1
                            # if our index is greater than the length of the list then break the while loop
                            if col+col2+i >= len(line[row]):
                                break    
                    
                        # look left
                        j = 0
                        left_moves = []
                        num_string2 = ""
                        while line[row+row2][col+col2-j].isdigit():
                            num_string2 += line[row+row2][col+col2-j]
                            j += 1

                            # if our index becomes negative then break the while loop
                            if col+col2-j < 0:
                                break
                        
                        num_string2 = num_string2[::-1]

                        if num_string1 == num_string2:
                            line_results_list.append(num_string1)
                        else:
                            if num_string1 in num_string2:
                                line_results_list.append(num_string2)
                            elif num_string2 in num_string1:
                                line_results_list.append(num_string1)
            line_results_list = list(x for x in set(line_results_list) if x not in prev_line_results)
            print(line_results_list)
            prev_line_results = line_results_list
            full_results_list.append(line_results_list)
                        
    #print(line_results_list)
    #line_results_list = list(set(line_results_list))

print(full_results_list)

answers_list = []
for list in full_results_list:
    for elem in list:
        answers_list.append(int(elem))

print(answers_list)
print(sum(answers_list))

# print(answers_list)
# print(sum(answers_list))