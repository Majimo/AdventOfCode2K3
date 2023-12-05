def create_mappings(seeds_map: list):
    result = {}
    for item in seeds_map:
        for key, values in item.items():
            if key in result:
                result[key].extend(values)
            else:
                result[key] = values

    mapping = {}
    for key, values in result.items():
        for line in values:
            if line:
                parts = list(map(int, line))
                source_start, source_end = parts[0], parts[0] + parts[2] - 1
                dest_start = parts[1]
                
                for source, dest in zip(range(source_start, source_end + 1), range(dest_start, dest_start + parts[2])):
                    mapping[source] = dest
    return mapping

with open("input.txt") as f:
    lines = [line.strip() for line in f.readlines()]

    seeds = []
    seeds_map = []
    current_label = None
    for i, line in enumerate(lines):
        if i == 0:
            seeds = line.split(':')[1][1:].split(' ')
        if line.endswith(':'):
            current_label = line[:-5]  # Remove ' map:'
            seeds_map.append({current_label: []})
        elif current_label and len(line) > 0:
            seeds_map[-1][current_label].append(line.split(' '))

    total_seeds_map = create_mappings(seeds_map)
    # Order from 0 to size
    total_seeds_map = {k: total_seeds_map[k] for k in sorted(total_seeds_map.keys())}

    # Match total_seeds_map.keys() with seeds
    seeds_match = {int(seeds[i]): total_seeds_map[i] for i in range(len(seeds))}
    
    print(total_seeds_map)
    print(seeds_match)

with open("input2.txt") as f:
    pass
