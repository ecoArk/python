# Let's try making a simple program to create random table/s of people

# Let's import random so we can use it to randomize the sample data
import random

# TO DO: create sample name
from typing import List

sample_name1: List[str] = ['Adi', 'Agus', 'Ade', 'Eka', 'Febi', 'Deni']
sample_name2: List[str] = ['Arifin', 'Suryantoro', 'Sumantoro', 'Supriyono',
                           'Ibrahim']
max_person = len(sample_name1) * len(sample_name2)
random_name = []

print('Input how many person do you want to create.')
print('Maximum is ' + str(len(sample_name1) * len(sample_name2)))
person: int = int(input('> '))

while person > max_person:
    print("Request is outside of available range. Maximum is " + str(max_person))
    person = int(input('> '))
else:
    while len(random_name) < person:
        creation = (sample_name1[random.randint(0, len(sample_name1) - 1)] + ' ' +
                    sample_name2[random.randint(0, len(sample_name2) - 1)])
        if creation not in random_name:
            random_name = random_name + [creation]
        else:
            continue
    print(str(person), 'person created successfully... \n')

# TO DO: export to some text file

# using open function, python is opening a file if there is not then it
# creates a file
file_open = open("tes_file.txt", 'w+')

# to insert something to the text file we can use the write function so
# that what we want to be in the file can be there
for i in sorted(random_name):
    file_open.write(i +'\n')

# using the close method is akin to saving the change we've made into the file
file_open.close()
