


def navigate_through_map(direction, instructions, count):
    print(instructions)
    start_index = instructions[0].find('(')
    end_index = instructions[0].find(')')

    content = instructions[0][start_index + 1:end_index]
    values = [value.strip() for value in content.split(',')]
    result = values[1] if direction == 'R' else values[0]

    print(result)
    count += 1
    return result, count

with open("input.txt") as f:
    lines = [line.strip() for line in f.readlines()]
    directions = [char for char in lines[0]]
    instructions = [line for line in lines[1:]]

    steps = 0
    next_step = 'AAA'
    for i, direction in enumerate(directions):
        next_map = [line for line in instructions[(i + 1):] if next_step in line]
        if len(next_map) == 0:
            next_map = [line for line in instructions if next_step in line]
        print(next_map)
        next_step, steps = navigate_through_map(direction, next_map, steps)
        if len(next_step) == 0:
            print('oh non !')

    print('PART 1 :', steps)

with open("input2.txt") as f:
    
    print('PART 2 :')