import re

def check_if_number_list_is_matching_symbol_position_in_grid(number_list, symbols):
    for symbol in symbols:
        for number in number_list:
            if number['line'] == symbol['line'] or number['line'] == symbol['line'] + 1 or number['line'] == symbol['line'] - 1:
                if symbol['position'] in number['positions'] or symbol['position'] + 1 in number['positions'] or symbol['position'] - 1 in number['positions']:
                    return True
    return False

def detect_numbers_in_line_and_position(line, j):
    numbers = re.findall(r'\d+', line)
    result = []
    for num in numbers:
        positions = []
        matches = re.finditer(num, line)
        for match in matches:
            start_index = match.start()
            for i in range(len(num)):
                positions.append(start_index + i)
        result.append({'number': int(num), 'positions': positions, 'line': j})
    return result

def detect_symbols_in_line_and_position(line):
    special_characters = ['$','*', '+', '#']
    positions = []
    for j, char in enumerate(line):
        if char in special_characters:
            positions.append({'line': i, 'position': j})
    return positions


with open("input.txt") as f:
    lines = [line.strip() for line in f.readlines()]
    result = 0

    for i, line in enumerate(lines):
        final_number_list = []
        number_list = detect_numbers_in_line_and_position(line, i)
        symbols = detect_symbols_in_line_and_position(line)
        if len(number_list) > 0: print(number_list)
        if len(symbols) > 0: 
            print(symbols)
            if check_if_number_list_is_matching_symbol_position_in_grid(number_list, symbols):
                final_number_list.append(number_list)
        print(final_number_list)
