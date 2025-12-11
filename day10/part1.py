import re
from itertools import combinations

pattern = r'^\[(.+)\] (.+) {(.+)}$'
machines = []

with open('input') as f:
    total = 0
    for line in f:
        match = re.search(pattern, line.strip())
        goal = match[1].replace('.','0').replace('#','1')
        buttons = match[2].split(' ')
        joltage = match[3]
        converted_buttons = []
        for button in buttons:
            template = ['0'] * len(goal)
            numbers = list(map(int, button[1:-1].split(',')))
            for number in numbers:
                template[number] = '1'
            converted_buttons.append(''.join(template)[::-1])
        #machines[goal[::-1]] = converted_buttons
        machines.append([goal[::-1], converted_buttons, joltage])

    machine_count = 0
    for machine in machines:
        lights = machine[0]
        buttons = machine[1]
        machine_count += 1
        i = 1
        end = int(lights,2)
        if end == 0:
            continue
        while True:
            end = int(lights,2)
            done = False
            permutations = list(combinations(buttons, i))
            for sequence in permutations:
                result = 0
                for x in sequence:
                    result = result ^ int(x,2)
                if result == end:
                    done = True
                    #print(f'{machine_count:<3} Goal: {lights:<10} {i:<3} presses: {sequence}')
                    break
            if done:
                total += i
                break
            i += 1
    print(total)