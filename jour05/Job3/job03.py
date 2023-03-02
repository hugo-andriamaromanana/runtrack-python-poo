def find_len(word,count):
    if word=='':
        return count
    else:
        count+=1
        word=word[:-1]
        return find_len(word,count)
    
def main():
    count=0
    word=input("Entrez un mot: ")
    print("Le mot", word, "contient", find_len(word,count), "caractères")

if __name__ == "__main__":
    main()