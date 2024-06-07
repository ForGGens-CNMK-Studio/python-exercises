# O clasa simple cu o functie de hello
class A:
    def hello(self):
        print("Hello, world!")


# testam
a = A()

a.hello()  # Hello, world!


# O clasa cu o functie care primeste un argument
class B:
    def hello(self, name):
        print(f"Hello, {name}!")


# testam
b = B()

b.hello("Cristi")  # Hello, Cristi!


# O clasa cu o functie care primeste un argument si un atribut
class C:
    def __init__(self, name):
        self.name = name

    def hello(self):
        print(f"Hello, {self.name}!")


# testam
c = C("Cristi")

c.hello()  # Hello, Cristi!


# clasa persoana
class Persoana:
    def __init__(self, nume, prenume, varsta):
        self.nume = nume
        self.prenume = prenume
        self.varsta = varsta

    def __str__(self):
        return f"{self.nume} {self.prenume} are {self.varsta} ani."


# testam
p = Persoana("Iordachescu", "Cristian", 22)

print(p)  # Iordachescu Cristian are 22 ani.

p1 = Persoana("Popescu", "Ion", 33)

print(p1)  # Popescu Ion are 33 ani.


# clasa angajat
class Angajat(Persoana):
    def __init__(self, nume, prenume, varsta, salariu):
        super().__init__(nume, prenume, varsta)
        self.salariu = salariu

    def __str__(self):
        return f"{self.nume} {self.prenume} are {self.varsta} ani si un salariu de {self.salariu}."

    def marire_salariu(self, procent):
        self.salariu += self.salariu * procent / 100


# testam
a = Angajat("Iordachescu", "Cristian", 22, 1000)

print(a)  # Iordachescu Cristian are 22 ani si un salariu de 1000.

a.marire_salariu(10)

print(a)  # Iordachescu Cristian are 22 ani si un salariu de 1100.


#  clasa cu atribute private
class D:
    def __init__(self):
        self.__x = 10

    def get_x(self):
        return self.__x

    def set_x(self, x):
        self.__x = x


# testam
d = D()

print(d.get_x())  # 10

d.set_x(20)

print(d.get_x())  # 20

# d.__x = 30  # AttributeError: 'D' object has no attribute '__x'
