def prim(n):
    ok=1 
    if n<1:
        ok=0
    else:
        for i in range (2, n//2 + 1):
            if n % i ==0 :
                ok = 0
    return ok



def prim_better(n):
    if n < 2:
        return False 
    if n==2:
        return False
    if n%2==0:
        return False
    for i in range (3, int(n**0.5)+1, 2):
        if n% i ==0:
            return False
    return True

def main():
    print (prim(7))
    print (prim(8))
    print (prim_better(7))
    print (prim_better(8))

if __name__ == "__main__":
    main()