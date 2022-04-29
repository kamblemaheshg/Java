#break
while True:
    name = input("Enter Name : ")
    if name !="":
        break
#continue
phone_no = "987-654-321"
for i in  phone_no :
    if i =="-":
        continue
    print(i,end="")
    
print()
#pass
for i in phone_no:
    if i=="8":
        pass
    else:
        print(i,end="")
