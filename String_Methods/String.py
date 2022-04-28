from dataclasses import replace
from operator import length_hint


name = "Mahesh G"
print(len(name))
print(name.find("a"))
print(name.capitalize())
print(name.upper())
print(name.lower())
print(name.isdigit())
print(name.isalpha())
print(name.count("a"))
print(name.replace("G","K"))
print(name*3)
