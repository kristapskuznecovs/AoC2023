import math

def part1(data):
    limitations = {"red": 12, "green": 13, "blue": 14}
    limited = 0

    for line in data:
        game_info, sets = line.split(": ")
        groups = map(str.split, sets.replace(";", ",").split(", "))
        if all(int(cube_nums) <= limitations[cube_color] for cube_nums, cube_color in groups):
            limited += int(game_info.split(" ")[1])
    return limited

def part2(data):
    total_sum = 0
    
    for line in data:
        counts = {"red": 0, "green": 0, "blue": 0}

        _, sets = line.split(": ")
        sets = sets.split("; ")

        for _set in sets:
            _set = {k: int(v) for v, k in map(str.split, _set.split(", "))}
            counts = {k: max(v, _set.get(k, 0)) for k, v in counts.items()}
        total_sum += math.prod(counts.values())
    
    return total_sum

def process_data(data):
    result = part2(data)
    return result   