def are_anagrams(s1, s2):
    # works for current purpose, but I guess there are more efficient solutions
    return hash(str(sorted(s1.lower()))) == hash(str(sorted(s2.lower())))


def gas_stations(distance, tank_size, stations):
    max_tank_size = tank_size
    i = 0
    previous = stations[0]
    recharging_stations = []
    print(stations)

    while i < len(stations) and stations[i] + max_tank_size < distance:
        # c = 0
        if i == 0:
            j = i
            while tank_size > stations[j]:
                previous = stations[j]
                j += 1
            recharging_stations.append(previous)
        else:
            j = i

            tank_size = max_tank_size + stations[i]

            while j < len(stations) and tank_size > stations[j]:
                previous = stations[j]
                j += 1
                # c += 1
            recharging_stations.append(previous)

        i += 1

    print(recharging_stations)

st = [50, 80, 110, 180, 220, 290]
st2 = [70, 90, 140, 210, 240, 280, 350]
print(are_anagrams('ad', 'bc'))
# gas_stations(320, 90, st)
gas_stations(320, 90, st)

# todo : fix logic :O
