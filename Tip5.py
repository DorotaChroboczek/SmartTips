names = ['Peter Parker', 'Clark Kent', 'Wade Wilson', 'Bruce Wayne']
heroes = ['Spiderman', 'Superman', 'Deadpool', 'Batman']
universes = ['Marvel', 'DC', 'Marvel', 'DC']
for index, name in enumerate(names):
    hero = heroes[index]
    print(f'{name} is actually {hero}')

print()

for name, hero in zip(names, heroes):       # better option
    print(f'{name} is actually {hero}')

print()

for name, hero, universe in zip(names, heroes, universes):       # better option
    print(f'{name} is actually {hero} from {universe}')

print()

for value in zip(names, heroes, universes):
    print(value)