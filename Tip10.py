nums = [3, 2, 4, 5]
print(nums)

print("\nMin, max, sum")
print(sum(nums))
print(min(nums))
print(max(nums))

print("\nlen")
print(len(nums))

print("\nnums[x]")
print(nums[0])
print(nums[0:2])
print(nums[:2])
print(nums[2:])
print(nums[-1])
print(nums[-3])

print("\nx.index('x') - or (x) if int/float")
print(nums.index(5))

print('\nis 4 in nums')
print(4 in nums)

print("\nenumerate(nums, start=42)")
for index, number in enumerate(nums, start=42):
    print(index, number)
#slicing

print("\nremove and pop")
print(nums)
remd = nums.remove(3)
poppy = nums.pop()
poppy1 = nums.pop(0)
print(remd)
print(poppy, poppy1)
print(nums)


print("\nextend, append, insert")
courses_2 = [1, 7]
nums.extend(courses_2)
nums.append(9)
nums.insert(0, 0)
# courses_3 = ['Astronomy', 'Karate']
# courses.insert(1, courses_3)
# ['Horse-riding', ['Astronomy', 'Karate'], 'History', 'Math', 'Physics', 'CompSci', 'Art', 'Music', 'Ethic']
# Causes problem:
# TypeError: '<' not supported between instances of 'list' and 'str'
print(nums)
print()

print("x.sort()")
nums.sort()
print(nums)

print("x.sort(reverse=True) takes x (doesn't look at effects of other methods)")
nums.sort(reverse=True)
print(nums)

print()
print("x.reverse() -------> is changing each time")
nums.reverse()
print(nums)
print("x.reverse() -------> is changing each time")
nums.reverse()
print(nums)
print()

print("x.sort(reverse=True) ---------------------> You see? :) it doesn't care about rests")
nums.sort(reverse=True)
print(nums)

print("x.sort(reverse=True) ---------------------> You see? :) it doesn't care about rests")
nums.sort(reverse=True)
print(nums)

print("x.reverse() -------> is changing each time")
nums.reverse()
print(nums)

print("x.sort(reverse=False)")
nums.sort(reverse=False)
print(nums)

print("x.sort(reverse=True)")
nums.sort(reverse=True)
print(nums)


print("x.reverse() -------> is changing each time")
nums.reverse()
print(nums)

print("sorted_courses = sorted(courses)")
sorted_courses = sorted(nums)
print(sorted_courses)
