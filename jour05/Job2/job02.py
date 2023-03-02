def exponent(x, n):
    if n == 0:
        return 1
    else:
        return x * exponent(x, n - 1)
    
def main():
    x = int(input("Entrez un entier: "))
    n = int(input("Entrez un entier: "))
    print("Le résultat de", x, "puissance", n, "est", exponent(x, n))

if __name__ == "__main__":
    main()