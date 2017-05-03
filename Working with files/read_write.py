#Read data from the file and add text to it
file_path = 'C:/RUSHIN/Github/Learning Python/Working with files/heroes.txt'
heroes_file = open(file_path,'r')
heroes = heroes_file.read()
new_path = 'C:/RUSHIN/Github/Learning Python/Working with files/new_heroes.txt'
new_heroes = open(new_path,'w')
title = 'Marvel Heroes\n'
new_heroes.write(title)
print(title)
new_heroes.write(heroes)
print(heroes)
heroes_file.close()
new_heroes.close()