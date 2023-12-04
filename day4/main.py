import re

def separate_numbers_in_two_piles(line):
    separate_symbol = '|'
    line_after_card_number = line.split(':')[1]
    separate_string_by_symbol = line_after_card_number.split(separate_symbol)
    winning_numbers = re.findall(r'\d+', separate_string_by_symbol[0])
    scratched_numbers = re.findall(r'\d+', separate_string_by_symbol[1])
    return winning_numbers, scratched_numbers

def determine_duplicate_lines_on_win(lines, winning_line_idx, indent):
    for i in range(indent):
        if i > 0:
            lines.append(lines[winning_line_idx + i])
    return lines

with open("input.txt") as f:
    lines = [line.strip() for line in f.readlines()]
    global_result = 0

    for line in lines:
        result = 0
        winning_numbers, scratched_numbers = separate_numbers_in_two_piles(line)
        for scratch_number in scratched_numbers:
            if scratch_number in winning_numbers:
                if result > 1: 
                    result = result * 2
                else: 
                    result += 1
                
        global_result += result
    print('PART 1 : ', global_result)

with open("input2.txt") as f:
    lines = [line.strip() for line in f.readlines()]

    for i, line in enumerate(lines):
        result = 0
        winning_numbers, scratched_numbers = separate_numbers_in_two_piles(line)
        for scratch_number in scratched_numbers:
            if scratch_number in winning_numbers:
                result += 1
        pattern = re.compile(r'\d+(?=:)', re.MULTILINE)

        matches = int(pattern.findall(line)[0]) - 1
        lines = determine_duplicate_lines_on_win(lines, matches, result + 1)
        print('Progress : ', len(lines))
    print('PART 2 : ', len(lines))
