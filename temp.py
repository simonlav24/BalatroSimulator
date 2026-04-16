

file_path = r'C:\Simon\Projects\balatro\domain\jokers.py'


output = ''

with open(file_path, 'r') as file:
    for line in file.readlines():
        if line.strip().startswith('super().__init__'):
            line = line[:-2] + ', event_bus=event_bus)\n'
        output += line

with open('output.txt', 'w+') as file:
    file.write(output)