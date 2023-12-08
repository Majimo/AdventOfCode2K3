def check_if_next_step_is_ZZZ(next_step, instructions, directions, r = 0):
    r += 1
    print('RESET .....', r, next_step)
    directions = directions + directions 
    steps = 0
    next_step = 'AAA'
    for direction in directions:
        next_step, steps = navigate_through_map(direction, instructions, next_step, steps)
        if next_step == 'ZZZ':
            break

    if next_step != 'ZZZ':
        next_step = (instructions[0].split(' ='))[0]
        check_if_next_step_is_ZZZ(next_step, instructions, directions, r)
    
    print(steps)
    return steps


def navigate_through_map(direction, instructions, next_step, count):
    i = next((index for index, ligne in enumerate(instructions) if next_step + ' =' in ligne), None)
    start_index = instructions[i].find('(')
    end_index = instructions[i].find(')')

    content = instructions[i][start_index + 1:end_index]
    values = [value.strip() for value in content.split(',')]
    result = values[1] if direction == 'R' else values[0]

    count += 1
    return result, count

with open("input.txt") as f:
    lines = [line.strip() for line in f.readlines()]
    directions = [char for char in lines[0]]
    instructions = [line for line in lines[2:]]

    steps = 0
    next_step = (instructions[0].split(' ='))[0]

    for direction in directions:
        next_step, steps = navigate_through_map(direction, instructions, next_step, steps)
        if next_step == 'ZZZ':
            break
    
    if next_step != 'ZZZ':
        next_step = (instructions[0].split(' ='))[0]
        steps = check_if_next_step_is_ZZZ(next_step, instructions, directions)

    print('PART 1 :', steps)

with open("input2.txt") as f:
    
    print('PART 2 :')