def factoriel(n):
    if n==0:
        return 1
    else:
        print(n)
        return n*factoriel(n-1)
    
def main():
    n = int(input("Entrez un entier: "))
    print("Le factoriel de", n, "est", factoriel(n))

if __name__ == "__main__":
    main()