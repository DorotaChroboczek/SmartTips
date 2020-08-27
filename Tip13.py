student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}

print(student)
print(student['name'])
print(student.get('phone', 'Not Found'))
print(student.get('name', 'Abracadabra'))

student['phone'] = '555-555-555'
student['name'] = 'Jane'
print(student)

student.update({'name': 'Ginny', 'age': 24, 'courses': ['Astronomy', 'Robotics'], 'hobby': 'photography'})
del student['phone']
print(student)
age = student.pop('age')
print(age)
print(student)

print(len(student))
print(student.keys())
print(student.values())
print(student.items())

for key, value in student.items():
    print(key, value)