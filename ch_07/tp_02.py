
def main():
    # f = open("le_fichier.txt",'w')
    # f.close()

    # Ecriture
    with open("le_fichier.txt",'w') as f:
        for i in range(10):
            # f.write(f'Hello {i}')
            print(f'Hello {i}',file=f)
    # Lecture
    with open("le_fichier.txt",'r') as f:
        # content = f.read()
        # print(content)
        # content = f.readlines()
        # print(content)
        for line in f:
            print(line.strip())


if __name__=='__main__':
    main()
