# Normal

items = (1, 2)

print(items)

# Unpacking

a, b = (1, 2)

print(a)
print(b)

c, _ = (6, 7)

print(c)

d, e = (4, 5)

print(d)

m, n, *o = (11, 12, 13, 14, 15)

print(m)
print(n)
print(o)

# *_ instead of *o - then there is no need to use it, i can ignore it

m, n, *o, p = (11, 12, 13, 14, 15)
print(m)
print(n)
print(o)
print(p)