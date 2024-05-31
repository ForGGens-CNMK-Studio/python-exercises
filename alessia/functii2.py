#Functie pentru produs la un numar variabil de argumente

def produs(*args):
    p=1
    for i in args:
        p*=i
    return p

print(produs(1,2,3,4,5))

#Functie pentru a afisa o lista de numere
def numere(v):
    for i in range(9):
        v.append(i)
    return v
v=[]
print(numere(v))


#Functie pentru a afisa o lista de dictionare

print("dictionar roman-englez")
print("dictionar explicativ al limbii romane")
print("dictionar roman-francez")



def f(people):
    for k, v in people.items():
        print(k,v)

people=[
   {"name":"saulea","age":"69", "city":"braila"},]
print(people)