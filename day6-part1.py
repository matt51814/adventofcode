with open('day6-input.txt', 'r') as file:
    puzzle_input = file.read()


times_str = puzzle_input.split('\n')[0]
distances_str = puzzle_input.split('\n')[1]

# how long the race lasts
times = [int(x) for x in times_str.split(' ')[1:] if x != '']
# record distances
distances = [int(x) for x in distances_str.split(' ')[1:] if x!= '']

# create time distances pairs
time_dist_pairs = [(times[i], distances[i]) for i in range(len(times))]

print(time_dist_pairs)

# Your toy boat has a starting speed of zero millimeters per millisecond. 
# For each whole millisecond you spend at the beginning of the race holding down the button, 
# the boat's speed increases by one millimeter per millisecond.
race = 2
ways_to_win_dict = {}
for race in range(len(times)):
    ways_to_win = []
    print("how long the race lasts: ", times[race])
    for sec in range(times[race]+1):
        speed = 0
        print("possible time spent holding: ", sec)
        for i in range(sec):
            speed += 1
        print("speed from hold: ", speed)
        time_left = times[race] - sec
        distance = speed * time_left
        print("distance travelled: ", distance)
        if distance > distances[race]:
            ways_to_win.append(sec)
    print(len(ways_to_win))
    ways_to_win_dict[race] = len(ways_to_win)
    print(ways_to_win_dict)

multi_result = 1
for i in ways_to_win_dict.values():
    print(i)
    multi_result *= i

print(multi_result)