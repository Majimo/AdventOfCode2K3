from math import prod
import re

def determine_id_from_line(line):
    # Get digits in a string following "Game " but ignoring everything after ":"
    return int(line[line.find("Game ") + len("Game "):line.find(":")])

def determine_max_for_each_color(line):
    possible_colors = [" red", " blue", " green"]
    max_for_each_color = []
    regex = r', |; '
    for color in possible_colors:
        numbers_in_color = []
        for number in re.split(regex, line):
            if color in number:
                # Replace the color with nothing
                number = number.replace(color, "")
                numbers_in_color.append(int(number))
        max_for_each_color.append(max(numbers_in_color))
    return max_for_each_color

with open("input2.txt") as f:
    lines = [line.strip() for line in f.readlines()]
    result = 0

    for i, line in enumerate(lines):
        computed_line = line.replace("Game " + str(determine_id_from_line(line)) + ": ", "")
        print(computed_line)
        lines[i] = [{"id": determine_id_from_line(line), "line": determine_max_for_each_color(computed_line)}]
        print(lines[i])

        # 12 red cubes, 13 green cubes, and 14 blue cubes
        if lines[i][0]["line"][0] <= 12 and lines[i][0]["line"][1] <= 14 and lines[i][0]["line"][2] <= 13:
            print("ok", lines[i][0]["id"])
        print(lines[i][0]["line"])
        result += prod(lines[i][0]['line'])
            
    print(result)