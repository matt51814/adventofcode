
from multiprocessing import Pool


with open('day5-input.txt', 'r') as file:
    puzzle_input = file.read()

def func(number, *args):
    for i in range(0,len(args[0]), 3):
        a = int(args[0][i])
        b = int(args[0][i+1])
        c = int(args[0][i+2])
        if number in range(b, b+c):
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
# print(tmp_dict)


seeds = [int(x) for x in tmp_dict['seeds:']]
# new_seeds = []
# for idx in range(len((seeds))):
#     if idx % 2 == 0:
#         for x in range(seeds[idx], seeds[idx]+seeds[idx+1]):
#             new_seeds.append(x)  

# new_seeds = (x for idx in range(0, len(seeds),2) for x in range(seeds[idx], seeds[idx] + seeds[idx + 1]) if idx < len(seeds) -1)
# print(new_seeds)

# triangles = ((x, y, z) for x in range(1, 1000) for y in range(1, 1000) for z in range(1, 1000))
# for triangle in triangles:
#     # do stuff

def seedtolocation(input_seed):
    soil = func(input_seed, tmp_dict['seed-to-soil'])
    fertilizer = func(soil, tmp_dict['soil-to-fertilizer'])
    water = func(fertilizer, tmp_dict['fertilizer-to-water'])
    light = func(water, tmp_dict['water-to-light'])
    temperature = func(light, tmp_dict['light-to-temperature'])
    humidity = func(temperature, tmp_dict['temperature-to-humidity'])
    location = func(humidity, tmp_dict['humidity-to-location'])
    return location

seeds = [int(x) for x in tmp_dict['seeds:']]
#new_seeds = (x for idx in range(0, len(seeds),2) for x in range(seeds[idx], seeds[idx] + seeds[idx + 1]) if idx < len(seeds) -1)
new_seeds = (x for idx in range(0, len(seeds),2) for x in range(seeds[idx], seeds[idx] + seeds[idx + 1]) if idx < len(seeds) -1)
# soils = (func(i, tmp_dict['seed-to-soil']) for i in new_seeds)
# fertilizers = (func(i, tmp_dict['soil-to-fertilizer']) for i in soils)
# waters = (func(i, tmp_dict['fertilizer-to-water']) for i  in fertilizers)
# lights = (func(i, tmp_dict['water-to-light']) for i in waters)
# temperatures = (func(i,  tmp_dict['light-to-temperature']) for i in lights)
# humiditys = (func(i, tmp_dict['temperature-to-humidity']) for i in temperatures)
# locations = (func(i, tmp_dict['humidity-to-location']) for i in humiditys)
# print(min(locations))



# soils = [func(i, ['50','98','2','52','50','48']) for i in seeds]
# fertilizers = [func(i, ['0', '15', '37', '37', '52', '2', '39', '0', '15']) for i in soils]
# waters = [func(i, ['49', '53', '8', '0', '11', '42', '42', '0', '7', '57', '7', '4']) for i  in fertilizers]
# lights = [func(i, ['88', '18', '7', '18', '25', '70']) for i in waters]
# temperatures = [func(i,  ['45', '77', '23', '81', '45', '19', '68', '64', '13']) for i in lights]
# humiditys = [func(i, ['0', '69', '1', '1', '0', '69']) for i in temperatures]
# locations = [func(i, [ '60', '56', '37', '56', '93', '4']) for i in humiditys]
# print(locations)
# print(min(locations))


def seedtosoil(number):
    return func(number, tmp_dict['seed-to-soil'])

def soiltofertilizer(number):
    return func(number, tmp_dict['soil-to-fertilizer'])

def fertilizertowater(number):
    return func(number, tmp_dict['fertilizer-to-water'])

def watertolight(number):
    return func(number, tmp_dict['water-to-light'])

def lighttotemperature(number):
    return func(number, tmp_dict['light-to-temperature'])

def temperaturetohumidity(number):
    return func(number, tmp_dict['temperature-to-humidity'])

def humiditytolocation(number):
    return func(number, tmp_dict['humidity-to-location'])
 
# protect the entry point
if __name__ == '__main__':
    # manager = Manager()
    # return_dict = manager.dict()
    # create all tasks
    # processes = [Process(target=seedtolocation, args=(i, return_dict)) for i in new_seeds]
    # # start all processes
    # for idx, process in enumerate(processes):
    #     print(idx)
    #     process.start()
    # # wait for all processes to complete
    # for process in processes:
    #     process.join()
    
    # print(return_dict.values())
    # # report that all tasks are completed
    # print('Done', flush=True)



    new_seeds = (x for idx in range(0, len(seeds),2) for x in range(seeds[idx], seeds[idx] + seeds[idx + 1]) if idx < len(seeds) -1)
    soils = set(map(seedtosoil, new_seeds))
    fertilizers = set(map(soiltofertilizer, soils))
    waters = set(map(fertilizertowater, fertilizers))
    lights = set(map(watertolight, waters))
    temperatures = set(map(lighttotemperature, lights))
    humiditys = set(map(temperaturetohumidity, temperatures))
    locations = set(map(humiditytolocation, humiditys))
    print(min(locations))
    # print("Running seeds-to-soil")
    # with Pool(4) as pool:
    #     soils = set(pool.map(seedtosoil, new_seeds))
    # print("Running soil to fertilizer")
    # with Pool(4) as pool:
    #     fertilizers = set(pool.map(soiltofertilizer, soils))
    # print("Running fertilizer-to-water")
    # with Pool(4) as pool:
    #     waters = set(pool.map(fertilizertowater, fertilizers))
    # print("Running water-to-light")
    # with Pool(4) as pool:
    #     lights = set(pool.map(watertolight, waters))
    # print("Running light-to-temperature")
    # with Pool(4) as pool:
    #     temperatures = set(pool.map(lighttotemperature, lights))
    # print("Running temperature-to-humidity")
    # with Pool(4) as pool:
    #     humiditys = set(pool.map(temperaturetohumidity, temperatures))
    # print("Running humidity-to-location")
    # with Pool(4) as pool:
    #     locations = set(pool.map(humiditytolocation, humiditys))
    # print(min(locations))
# soils = (func(i, tmp_dict['seed-to-soil']) for i in new_seeds)
# fertilizers = (func(i, tmp_dict['soil-to-fertilizer']) for i in soils)
# waters = (func(i, tmp_dict['fertilizer-to-water']) for i  in fertilizers)
# lights = (func(i, tmp_dict['water-to-light']) for i in waters)
# temperatures = (func(i,  tmp_dict['light-to-temperature']) for i in lights)
# humiditys = (func(i, tmp_dict['temperature-to-humidity']) for i in temperatures)
# locations = (func(i, tmp_dict['humidity-to-location']) for i in humiditys)
# print(min(locations))
    



    
