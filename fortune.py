import os
import random


#Open text file
with open('fortunedat.txt', 'r') as file_handler:
    options = file_handler.read()
    line = options.split("%")
    line_position = random.randint(0, len(line)-1)
    print(line[line_position])

