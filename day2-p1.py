with open('day2-input.txt', 'r') as file:
    puzzle_input = file.readlines()

max_r, max_g, max_b = 12, 13, 14

impossible_games = []
for line in puzzle_input:
    game = int(line[5:line.find(':')])
    for cube_set in line.split(':')[1].split(';'):
        for cube in cube_set.split(','):
            if 'red' in cube:
                num = int(cube.replace(" red", ""))
                if num > max_r:
                    impossible_games.append(game)
            if 'green' in cube:
                num = int(cube.replace(" green", ""))  
                if num > max_g:
                    impossible_games.append(game)
            if 'blue' in cube:
                num = int(cube.replace(" blue", ""))
                if num > max_b:
                    impossible_games.append(game)

print(list(set(impossible_games)))
possible_games = [x for x in range(100) if x not in list(set(impossible_games))]
print(possible_games)
print(sum(possible_games))
                
