names = ['Corey', 'Chris', 'Dave', 'Travis']

for index, name in enumerate(names):
    print(index, name)

print()

for index, name in enumerate(names, start=7):
    print(index, name)