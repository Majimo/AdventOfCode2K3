alphanumeric = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

def get_numeric_list(string_list):
    new_numeric_lines = []
    for string_line in string_list:
        numbers = [string_line for string_line in string_line if string_line.isdigit()]
        first_last = numbers[0] + numbers[-1] if numbers else None
        new_numeric_lines.append(first_last)
    return new_numeric_lines

def remplacer_mots(chaine, liste_mots): 
    for mot in liste_mots:
        chaine = chaine.replace(mot, mot[0] + str(liste_mots.index(mot) + 1) + mot[len(mot) - 1]) 
    return chaine

with open("input2.txt") as f:
    lines = [line.strip() for line in f.readlines()]
    
    for i, code in enumerate(lines):
        code = remplacer_mots(code, alphanumeric)
        lines[i] = code
        print(lines[i])

    numeric_lines = get_numeric_list(lines)
    final_result = sum(int(numbers) for numbers in numeric_lines if numbers)
    print(final_result)