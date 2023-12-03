def part1(data):
    return sum((digits := [int(i) for i in line if i.isdigit()])[0] * 10 + digits[-1] for line in data)

def part2(data):
    mappings = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    new_data = [[x if (x := "".join([str(idx) for idx, val in enumerate(mappings, 1) if line[i:].startswith(val)])) else line[i] for i in range(len(line))] for line in data]
    return part1(new_data)

def process_data(data):
    result = part2(data)
    return result