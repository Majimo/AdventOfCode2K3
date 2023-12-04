import re

def separate_numbers_in_two_piles(line):
    separate_symbol = '|'
    line_after_card_number = line.split(':')[1]
    separate_string_by_symbol = line_after_card_number.split(separate_symbol)
    winning_numbers = re.findall(r'\d+', separate_string_by_symbol[0])
    scratched_numbers = re.findall(r'\d+', separate_string_by_symbol[1])
    return winning_numbers, scratched_numbers

with open("input.txt") as f:
    lines = [line.strip() for line in f.readlines()]
    global_result = 0

    for line in lines:
        result = 0
        winning_numbers, scratched_numbers = separate_numbers_in_two_piles(line)
        print('win', winning_numbers)
        print('scr', scratched_numbers)
        for scratch_number in scratched_numbers:
            if scratch_number in winning_numbers:
                if result > 1: 
                    result = result * 2
                    print('result', result * 2)
                else: 
                    result += 1
                    print('result', result)
                
        global_result += result
    print(global_result)

# 1 -> 1
# 2 -> 2
# 3 -> 4
# 4 -> 8
# 5 -> 16

# result * 2
# 