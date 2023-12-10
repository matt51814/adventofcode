with open('day6-input.txt', 'r') as file:
    puzzle_input = file.read()


times_str = puzzle_input.split('\n')[0]
distances_str = puzzle_input.split('\n')[1]

print(times_str)
print(distances_str)


# how long the race lasts
times = [x for x in times_str.split(' ')[1:] if x != '']
# record distances
distances = [x for x in distances_str.split(' ')[1:] if x!= '']

time = int("".join(times))
distance = int("".join(distances))
print(time)
print(distance)

# # Your toy boat has a starting speed of zero millimeters per millisecond. 
# # For each whole millisecond you spend at the beginning of the race holding down the button, 
# # the boat's speed increases by one millimeter per millisecond.
def func(sec_hold):
    distance = sec_hold * (47986698 - sec_hold)
    return distance


sec_holds = [x for x in range(47986699)]
print(map(func, sec_holds))
print(len([x for x in map(func, sec_holds) if x > 400121310111540]))

# ways_to_win = []
# print("how long the race lasts: ", time)
# for sec in range(time+1):
#     speed = 0
#     print("possible time spent holding: ", sec)
#     for i in range(sec):
#         speed += 1
#     print("speed from hold: ", speed)
#     time_left = time - sec
#     tmp_distance = speed * time_left
#     print("distance travelled: ", tmp_distance)
#     if tmp_distance > distance:
#         ways_to_win.append(sec)
# print(len(ways_to_win))


# multi_result = 1
# for i in ways_to_win_dict.values():
#     print(i)
#     multi_result *= i

# print(multi_result)