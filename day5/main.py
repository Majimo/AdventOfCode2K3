def create_mappings(seeds_map: list):
    result = {}
    for item in seeds_map:
        for key, values in item.items():
            if key in result:
                result[key].extend(values)
            else:
                result[key] = values

    mappings = {}
    temp_max = 0
    for key, values in seeds_map:
        mapping = {}
        for line in values:
            if line:
                parts = list(map(int, line))
                source_start, source_end = parts[1], parts[1] + parts[2] - 1
                dest_start = parts[0]
                
                for source, dest in zip(range(source_start, source_end + 1), range(dest_start, dest_start + parts[2])):
                    mapping[source] = dest
        if max(mapping.keys()) > temp_max:
            temp_max = max(mapping.keys()) + 1
        # Any source numbers that aren't mapped correspond to the same destination number. So, seed number 10 corresponds to soil number 10.
        for i in range(0, temp_max):
            if i not in mapping:
                mapping[i] = i
        mappings[key] = mapping
        
    return mappings

def match_seeds(locations, converted_seeds, seeds, depth=0, match=None):
    if match is None:
        match = {}

    if depth < len(converted_seeds):
        for seed in seeds:
            match[seed] = converted_seeds[depth][seed]
            match_seeds(locations, converted_seeds, [converted_seeds[depth][seed]], depth + 1, match)
    if depth == len(converted_seeds) - 1:
        locations.append(list(match.values())[-1])
    return locations

with open("input.txt") as f:
    lines = [line.strip() for line in f.readlines()]

    seeds = list(map(int,lines[0].split(':')[1][1:].split(' ')))
    print('Seeds:', seeds)
    seeds_map = []
    current_label = None
    for line in lines:
        if line.endswith(':'):
            current_label = line[:-5]  # Remove ' map:'
            seeds_map.append({current_label: []})
        elif current_label and len(line) > 0:
            seeds_map[-1][current_label].append(line.split(' '))

    converted_seeds = []
    # Order from 0 to size of total_seeds_map
    for line in create_mappings(seeds_map).values():
        line = {k: line[k] for k in sorted(line.keys())}
        converted_seeds.append(line)

    location = min(match_seeds([], converted_seeds, seeds))
    print('PART 1 :', location)
    
with open("input2.txt") as f:
    pass
