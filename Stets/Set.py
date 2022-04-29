utensils = {"fork","spoon","knife"}
dishes={"blow","table"}
utensils.add("napkin")
utensils.remove("fork")
print(utensils.difference(dishes))
print(utensils.intersection(dishes))
utensils.update(dishes)
for i in utensils:
    print(i)
