with open('day2-input.txt', 'r') as file:
    puzzle_input = file.readlines()

powers = []
for line in puzzle_input:
    game = int(line[5:line.find(':')])
    print(line)
    max_r, max_g, max_b = 0, 0, 0
    for cube_set in line.split(':')[1].split(';'):
        for cube in cube_set.split(','):
            if 'red' in cube:
                num = int(cube.replace(" red", ""))
                if num > max_r:
                    max_r = num
            if 'green' in cube:
                num = int(cube.replace(" green", ""))  
                if num > max_g:
                    max_g = num
            if 'blue' in cube:
                num = int(cube.replace(" blue", ""))
                if num > max_b:
                    max_b = num
    print(max_r, max_g, max_b)
    powers.append(max_r * max_g * max_b)


print(sum(powers))