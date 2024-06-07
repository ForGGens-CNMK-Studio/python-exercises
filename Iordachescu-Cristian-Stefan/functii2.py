# functie in care pasam un vector si returneaza un vector cu elementele impare din vectorul initial
def impare(v):
    w = []
    for i in v:
        if i % 2 == 1:
            w.append(i)
    return w


# testam
v = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(impare(v))  # [1, 3, 5, 7, 9]


# Functie in care pasam un vector si il modifica astfel incat sa contina doar elementele impare
def impare2(v):
    i = 0
    while i < len(v):
        if v[i] % 2 == 0:
            v.pop(i)
        else:
            i += 1


# testam
v = [1, 2, 3, 4, 5, 6, 7, 8, 9]
impare2(v)
print(v)  # [1, 3, 5, 7, 9]


# Functie cu *args
def suma(*args):
    s = 0
    for i in args:
        s += i
    return s


# testam
print(suma(1, 2, 3, 4, 5))  # 15


# functie cu mai multe argumente si apelare prin nume
def f(a, b, c):
    return a + b + c


# testam
print(f(1, 2, 3))  # 6
print(f(a=1, b=2, c=3))  # 6
print(f(c=3, a=1, b=2))  # 6
print(f(1, c=3, b=2))  # 6


# Funtie cu valori default
def f(a=1, b=2, c=3):
    return a + b + c


# testam
print(f())  # 6
print(f(4))  # 9
print(f(4, 5))  # 12
print(f(4, 5, 6))  # 15

print(f(c=6))  # 9
print(f(c=6, b=5))  # 10


# Functie cu **kwargs
def f(**kwargs):
    for k, v in kwargs.items():
        print(k, v)


# testam
f(a=1, b=2, c=3)  # a 1 b 2 c 3
f(x=4, y=5, z=6)  # x 4 y 5 z 6
