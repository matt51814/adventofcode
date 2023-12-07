# think this is almost there, check edge cases. numbers at start and ends of rows

from string import punctuation

with open('day3-input.txt', 'r') as file:
    puzzle_input = file.read()

lines = puzzle_input.split('\n')
num_indices = []
for row in range(len(lines)):
    #print(lines[row])
    s_idx, e_idx = -1, -1    
    for col in range(len(lines[row])):
        elem = lines[row][col]
        if elem.isdigit() and (col == 0 or lines[row][col-1] == '.' or lines[row][col-1] in punctuation):
            s_idx = col
        if (elem == '.' or elem in punctuation) and lines[row][col-1].isdigit():
            e_idx = col
        elif col == len(lines[row])-1 and lines[row][col-1].isdigit():
            e_idx = col + 1
        if s_idx != -1 and e_idx != -1:
            #print(lines[row][s_idx:e_idx]) 
            num_indices.append([row, s_idx, e_idx])   
            s_idx, e_idx = -1, -1    

# loop through num indices list, go round surrounding square and if theres a piece of punctuation store the number
gear_nums = []
for r, s, e in num_indices:
    #print(r, s, e)
    if r == 0:
        #print(lines[r][s-1:e+1].strip('.'))
        #print(lines[r+1][s-1:e+1].strip('.'))
        mid_line = [x for x in lines[r][s-1:e+1].strip('.') if not x.isdigit()]
        bottom_line = [x for x in lines[r+1][s-1:e+1].strip('.') if not x.isdigit()]
        if mid_line or bottom_line:
            print(int(lines[r][s:e]))
            gear_nums.append(int(lines[r][s:e]))

    elif r == len(lines)-1:
        # print(lines[r-1][s-1:e+1].strip('.'))
        # print(lines[r][s-1:e+1].strip('.'))

        top_line = [x for x in lines[r-1][s-1:e+1].strip('.') if not x.isdigit()]
        mid_line = [x for x in lines[r][s-1:e+1].strip('.') if not x.isdigit()]

        if top_line or mid_line:
            print(int(lines[r][s:e]))
            gear_nums.append(int(lines[r][s:e]))

    else:

        top_line = [x for x in lines[r-1][s-1:e+1].strip('.') if not x.isdigit()]
        mid_line = [x for x in lines[r][s-1:e+1].strip('.') if not x.isdigit()]
        bottom_line = [x for x in lines[r+1][s-1:e+1].strip('.') if not x.isdigit()]

        if top_line or mid_line or bottom_line:
            print(int(lines[r][s:e]))
            gear_nums.append(int(lines[r][s:e]))

        # print(lines[r-1][s-1:e+1].strip('.'))
        # print(lines[r][s-1:e+1].strip('.'))
        # print(lines[r+1][s-1:e+1].strip('.'))
print(gear_nums)
print(sum(gear_nums))