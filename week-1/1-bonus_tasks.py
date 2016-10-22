import re


def are_anagrams(s1, s2):
    # works for current purpose, but I guess there are more efficient solutions
    return hash(str(sorted(s1.lower()))) == hash(str(sorted(s2.lower())))


def gas_stations(distance, tank_size, stations):
    res = [0]
    stations.append(distance)
    for i in range(len(stations) - 1):
        diff = stations[i + 1] - stations[i]
        size = tank_size - (stations[i] - res[-1])
        print(size)
        if size < diff:
            res.append(stations[i])
            size = tank_size
    return res[1:]


def reduce_file_path(path):
    print(path)
    splited = path.split('/')
    result = []
    for x in splited:
        if x != '.' and x != '' and x != '..':
            result.append(x)
        elif x == '..' and len(result) > 0:
            result.pop()

    if len(result) == 0:
        return '/'
    elif len(result) == 1 and re.match('[a-zA-Z]', result[0]):
        return '/' + result[0]
    return '/' + '/'.join(result)
