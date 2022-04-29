from symtable import Symbol


rows=int(input("Enter rows : "))
col = int(input("Enter Col : "))
Symbol=input("Enter Symbol")
for i in range(rows):
    for j in range(col):
        print(Symbol,end="")
    print("")
