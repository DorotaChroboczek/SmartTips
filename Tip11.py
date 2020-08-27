courses = ['History', 'Math', 'Physics', 'CompSci']
print(courses)

course_str = ', '.join(courses)
print(course_str)

course_str = ' - '.join(courses)
print(course_str)

new_list = course_str.split(' - ')
print(new_list)

new_list[0] = 'Art'
print(new_list)

list2 = courses
bark = tuple(list2)
print(bark)

list3 = new_list
miau = tuple(list3)
print(miau)

# DOESN'T WORK :)
new_list[0] = 'Crazy'
print(miau)

print()

# SET don't care about order = no index, place is changing
# SET has no duplicates

first_set = set(courses)
print(first_set)
print('Math' in first_set)
second_set = {'History', 'Math', 'Art', 'Design'}
print(second_set)
print("\nfirst_set.intersection(second_set) --> CECHY WSPÓLNE")
print(first_set.intersection(second_set))
print("\nfirst_set.difference(second_set)")
print(first_set.difference(second_set))
print("\nsecond_set.difference(first_set)")
print(second_set.difference(first_set))
print("\nfirst_set.union(second_set)")
print(first_set.union(second_set))

print()

# EMPTY LISTS: 2 WAYS:
empty_list = []
empty_list2 = list()

# EMPTY TUPLE: 2 WAYS:
empty_tuple = ()
empty_tuple2 = tuple()

# EMPTY DICT:
empty_dict = {}

# EMPTY SET:
empty_set = set()