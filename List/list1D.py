food=["Pizzza",5,55.22,"Akash"]
print(food)
print(food[0]) #idx no []
print(food[2:])
food[1]="Mahesh"
print(food)
for i in food:
    print(i)
food.append("ice cream")
food.remove(55.22)
food.pop()
food.insert(3,"Jalebi")
food.sort()
print(food)
food.clear()
