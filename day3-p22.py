# think this is almost there, check edge cases. numbers at start and ends of rows

#4361

from string import punctuation
from collections import Counter

punctuation = [x for x in punctuation if x != '.']

with open('day3-input.txt', 'r') as file:
    puzzle_input = file.read()

lines = puzzle_input.split('\n')
num_indices = []
for row in range(len(lines)):
    #print(lines[row])

    split_line = lines[row]

    for x in punctuation:
        if x in split_line:
            split_line = split_line.replace(x,'.')

    split_line = split_line.split('.')
    
    #print(split_line)
    for idx, val in enumerate(split_line):
        
        if val.isdigit():
            #print(idx, val)
            s_idx = 0
            e_idx = 0
            #print(".".join(split_line[:idx]))
            print(".".join(split_line[:idx+1]))
            e_idx = len(".".join(split_line[:idx+1]))
            s_idx = e_idx - (len(val))            
            num_indices.append((row, s_idx, e_idx))


for r, s, e in num_indices:
    print(lines[r][s:e])


# loop through num indices list, go round surrounding square and if theres a piece of punctuation store the number
gear_nums = []
for r, s, e in num_indices:
    #print(r, s, e)
    if r == 0:
        tmp_s = s
        tmp_e = e
        if tmp_s == 0:
            tmp_s += 1
        if tmp_e == len(lines[row]):
            tmp_e += -1
        #print(lines[r][s-1:e+1].strip('.'))
        #print(lines[r+1][s-1:e+1].strip('.'))
        mid_line = [x for x in lines[r][tmp_s-1:tmp_e+1].strip('.') if not x.isdigit()]
        bottom_line = [x for x in lines[r+1][tmp_s-1:tmp_e+1].strip('.') if not x.isdigit()]
        if mid_line or bottom_line:
            print(int(lines[r][s:e]))
            gear_nums.append(int(lines[r][s:e]))

    elif r == len(lines)-1:

        # print(lines[r-1][s-1:e+1].strip('.'))
        # print(lines[r][s-1:e+1].strip('.'))
        tmp_s = s
        tmp_e = e
        if tmp_s == 0:
            tmp_s += 1
        if tmp_e == len(lines[row]):
            tmp_e += -1

        top_line = [x for x in lines[r-1][tmp_s-1:tmp_e+1].strip('.') if not x.isdigit()]
        mid_line = [x for x in lines[r][tmp_s-1:tmp_e+1].strip('.') if not x.isdigit()]

        if top_line or mid_line:
            print(int(lines[r][s:e]))
            gear_nums.append(int(lines[r][s:e]))

    else:
        tmp_s = s
        tmp_e = e
        if tmp_s == 0:
            tmp_s += 1
        if tmp_e == len(lines[row]):
            tmp_e += -1

        top_line = [x for x in lines[r-1][tmp_s-1:tmp_e+1].strip('.') if not x.isdigit()]
        mid_line = [x for x in lines[r][tmp_s-1:tmp_e+1].strip('.') if not x.isdigit()]
        bottom_line = [x for x in lines[r+1][tmp_s-1:tmp_e+1].strip('.') if not x.isdigit()]

        if top_line or mid_line or bottom_line:
            print(int(lines[r][s:e]))
            gear_nums.append(int(lines[r][s:e]))

        # print(lines[r-1][s-1:e+1].strip('.'))
        # print(lines[r][s-1:e+1].strip('.'))
        # print(lines[r+1][s-1:e+1].strip('.'))
print(gear_nums)
print(sum(gear_nums))