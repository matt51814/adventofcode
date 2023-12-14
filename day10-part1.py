from collections import Counter

with open('day10-example-input.txt', 'r') as file:
    puzzle_input = file.read()


print(puzzle_input)

pipes = puzzle_input.split('\n')
print(pipes)


def find_start_position(pipes_list):
    for row in range(len(pipes_list)):
        for col in range(len(pipes_list[row])):
            if pipes_list[row][col] == 'S':
                return (row, col)
            
def check_top(pipes_list, row, col):
    if row - 1 < 0:
        return False
    if pipes_list[row-1][col] in ['|', 'F', '7']:
        return True
    return False

def check_bottom(pipes_list, row, col):
    if row >= len(pipes_list):
        return False
    if pipes_list[row+1][col] in ['|', 'J', 'L']:
        return True
    return False
    
def check_right(pipes_list, row, col):
    if col + 1 >= len(pipes_list[row]):
        return False
    if pipes_list[row][col+1] in ['-', 'J', '7']:
        return True
    return False

def check_left(pipes_list, row, col):
    if col - 1 < 0:
        return False
    if pipes_list[row][col-1] in ['-', 'F']:
        return True
    return False


print(find_start_position(pipes))
row, col = find_start_position(pipes)
print(pipes[row][col])
print(check_top(pipes, row, col))
print(check_bottom(pipes, row, col))
print(check_left(pipes, row, col))
print(check_right(pipes, row, col))

cycle = [pipes[row][col]]
print(cycle)
while 'S' not in cycle[1:]:
    print("HELLO")
