def lol (n):

    if(n<=1):
        return False
    for i in range(2,int(n//2),1):
        if n % i==0:
            return False
    return True

def main():
    print(lol(43))

if __name__ == "__main__":
    main()