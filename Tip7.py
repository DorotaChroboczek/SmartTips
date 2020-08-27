
class Person():
    pass

person = Person()

#erson.first = "Corey"
#person.last = "Schafer"

#print(person.first)
#print(person.last)


# 2nd idea:
#first_key = 'first'
#first_val = 'Corey'

#setattr(person, first_key, first_val)
#first = getattr(person, first_key)
#last = getattr(person, first_val)
#print(first)
#print(last)


person_info = {'first': 'Corey', 'last': 'Schafer'}

for key, value in person_info.items():
    setattr(person, key, value)

print(person.first)
print(person.last)

for key in person_info.keys():
    print(getattr(person, key))