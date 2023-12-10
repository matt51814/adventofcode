with open('day5-input.txt', 'r') as file:
    puzzle_input = file.read()

def func(number, *args):
    print(args[0])
    for i in range(len(args[0])):
        if i % 3 == 0:
            a = int(args[0][i])
        if i % 3 == 1:
            b = int(args[0][i])
        if i % 3 == 2:
            c = int(args[0][i])
            if number in range(b,b+c):
                return(range(a,a+c)[range(b,b+c).index(number)])
    return number
        

# soils = [func(i, ['50','98','2','52','50','48']) for i in seeds]
# fertilizers = [func(i, ['0', '15', '37', '37', '52', '2', '39', '0', '15']) for i in soils]
# waters = [func(i, ['49', '53', '8', '0', '11', '42', '42', '0', '7', '57', '7', '4']) for i  in fertilizers]
# lights = [func(i, ['88', '18', '7', '18', '25', '70']) for i in waters]
# temperatures = [func(i,  ['45', '77', '23', '81', '45', '19', '68', '64', '13']) for i in lights]
# humiditys = [func(i, ['0', '69', '1', '1', '0', '69']) for i in temperatures]
# locations = [func(i, [ '60', '56', '37', '56', '93', '4']) for i in humiditys]
# print(locations)
# print(min(locations))

tmp_dict = {}
for val in puzzle_input.split():
    if not val.isdigit() and val != 'map:':
        mapping_name = val
        tmp_dict[mapping_name] = []
    if val.isdigit():
        tmp_dict[mapping_name].append(val)
print(tmp_dict)
seeds = [int(x) for x in tmp_dict['seeds:']]
print(seeds)
print(tmp_dict['seed-to-soil'])
soils = [func(i, tmp_dict['seed-to-soil']) for i in seeds]
print(soils)
fertilizers = [func(i, tmp_dict['soil-to-fertilizer']) for i in soils]
print(fertilizers)
waters = [func(i, tmp_dict['fertilizer-to-water']) for i  in fertilizers]
print(waters)
lights = [func(i, tmp_dict['water-to-light']) for i in waters]
print(lights)
temperatures = [func(i,  tmp_dict['light-to-temperature']) for i in lights]
print(temperatures)
humiditys = [func(i, tmp_dict['temperature-to-humidity']) for i in temperatures]
print(humiditys)
locations = [func(i, tmp_dict['humidity-to-location']) for i in humiditys]
print(locations)
print(min(locations))



# soils = [func(i, ['50','98','2','52','50','48']) for i in seeds]
# fertilizers = [func(i, ['0', '15', '37', '37', '52', '2', '39', '0', '15']) for i in soils]
# waters = [func(i, ['49', '53', '8', '0', '11', '42', '42', '0', '7', '57', '7', '4']) for i  in fertilizers]
# lights = [func(i, ['88', '18', '7', '18', '25', '70']) for i in waters]
# temperatures = [func(i,  ['45', '77', '23', '81', '45', '19', '68', '64', '13']) for i in lights]
# humiditys = [func(i, ['0', '69', '1', '1', '0', '69']) for i in temperatures]
# locations = [func(i, [ '60', '56', '37', '56', '93', '4']) for i in humiditys]
# print(locations)
# print(min(locations))