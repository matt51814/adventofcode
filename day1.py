"""
Day 1 - Advent of Code
part 1
"""

WRITTEN_DIGITS = {
    'one':'1',
    'two':'2',
    'three':'3',
    'four':'4',
    'five':'5',
    'six':'6',
    'seven':'7', 
    'eight':'8', 
    'nine':'9'
}


with open('day1-input.txt', 'r') as file:
    input = file.read()

output_lines = []
for line in input.split():
    nums = []
    print(line)
    for s_idx in range(len(line)):
        if line[s_idx].isdigit():
            nums.append(int(line[s_idx]))

        for e_idx in range(2,6):
            if line[s_idx:s_idx+e_idx] in list(WRITTEN_DIGITS.keys()):
                nums.append(int(WRITTEN_DIGITS[line[s_idx:s_idx+e_idx]]))

    if len(nums) == 1:
        print(int(f"{nums[0]}{nums[0]}"))
        output_lines.append(int(f"{nums[0]}{nums[0]}"))
    elif len(nums) == 2:
        print(int(f"{nums[0]}{nums[1]}"))
        output_lines.append(int(f"{nums[0]}{nums[1]}"))
    elif len(nums) > 2:
        print(int(f"{nums[0]}{nums[-1]}"))
        output_lines.append(int(f"{nums[0]}{nums[-1]}"))

print(sum(output_lines))

