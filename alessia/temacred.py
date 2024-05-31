def div(n):
    k=0
    for i in range (1,n+1):
        if n % i == 0:
            k=k+1
    return k    

print (div(12))
print (div(9))
print (div(18))
