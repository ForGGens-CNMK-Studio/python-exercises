x = 5

print(x)

x = "string"

print(x)

x = 35.5

print(x + 5)

if x == 35.4:
    print("x is 35.5")
else:
    print("x is not 35.5")

i = 5

while i > 0:
    print(i)
    i -= 1

for i in range(5):
    print(i)

for i in range(5, 0, -1):
    print(i)


v = [1, 2, 3, 4, 5]

for i in v:
    print(i)

for i in range(len(v)):
    print(v[i])

for i in reversed(v):
    print(i)

for i in range(len(v)):
    v[i] = v[i] * 2

print(v)

for i in range(10):
    v.append(i)

print(v)

for i in range(10):
    print(v.pop(), end=" ")

print(v)

t = (1, 2, 3, 4, 5)

for i in t:
    print(i)

for i in range(len(t)):
    print(t[i])

# t[1] = 5
print(t)

d: dict[str, int] = {"key1": 1, "key2": 2, "key3": 3}

print(d)
print(d["key1"])

for k in d:
    print(k, d[k])

for k, v in d.items():
    print(k, v)

d["key4"] = 4
print(d)

person = {"name": "John", "age": 35, "city": "New York"}
print(person)

people = [
    {"name": "John", "age": 35, "city": "New York"},
    {"name": "Jane", "age": 25, "city": "Los Angeles"},
    {"name": "Jim", "age": 45, "city": "Chicago"},
]
print(people)
for p in people:
    print(p)

# import pprint
from pprint import pprint

pprint(people)

# import math
# print(math.sqrt(16))
# print(math.pi)

from math import sqrt as sq, pi

print(sq(16))
print(pi)

print(1_000_000)
print(0b1010)
print(0o12)
print(0x0A)
print(1.5e2)
