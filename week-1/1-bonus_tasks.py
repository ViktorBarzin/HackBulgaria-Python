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

st = [50, 80, 110, 180, 220, 290]
st2 = [70, 90, 140, 210, 240, 280, 350]
print(are_anagrams('ad', 'bc'))
# gas_stations(320, 90, st)
gas_stations(320, 90, st)

# todo : fix logic :O
