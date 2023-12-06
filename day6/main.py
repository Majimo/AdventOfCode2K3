from math import prod

# Calcul de la distance parcourue en fonction du temps pressé sur le bouton
def calculate_distance(available_times, distances_to_beat, i=0):
    distance = 0
    beated_times = 0
    for time_pressed in range(int(available_times[i])):
        speed = time_pressed + 1  # La vitesse augmente à chaque milliseconde pressée
        distance += -(speed - (int(available_times[i]) - time_pressed)) # La distance parcourue à chaque milliseconde est la vitesse à ce moment-là

        if distance > int(distances_to_beat[i]):
            beated_times += 1
    return beated_times

with open("input.txt") as f:
    lines = [line.strip() for line in f.readlines()]
    
    times = (' '.join(lines[0].split(':')[1].split())).split(' ')
    distances = (' '.join(lines[1].split(':')[1].split())).split(' ')

    times_to_distances = dict(zip(times, distances))

    beated_times = []
    for i in range(len(times)):
        beated_times.append(calculate_distance(times, distances, i))
        
    print('PART 1 :', prod(beated_times))
    
with open("input2.txt") as f:
    lines = [line.strip() for line in f.readlines()]
    
    times = ' '.join(lines[0].split(':')[1].split())
    distances = ' '.join(lines[1].split(':')[1].split())
    beated_times = calculate_distance([int(times.replace(' ', ''))], [int(distances.replace(' ', ''))])
        
    print('PART 2 :', beated_times)
