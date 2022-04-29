import time
name =""
while len(name)==0:
    name=input("Enter name: ")
print("Name "+name)
for i in range(10):
    print(i)
for i in range(50,101):
    print(i)
for i in "Bro Code":
    print(i)
for seconds in range(10,0,-1): #(star , end , steps)
    print(seconds)
    time.sleep(1)
print("Happy New Year!")
