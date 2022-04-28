# slicing | indexing = create a substring by extracting element from another string
name = "Jug Jug Jiyo" 
print(len(name))
name1= name[0:3] #first inclusive second exclusive
print(name1)
name2 = name[0:12:2] #[start :stop:step/incremented by indx]
print(name2)
reverseString = name[::-1]
print(reverseString)
website = "http://www.googlecom"
print(len(website))
slice = slice(7,-3)
print(website[slice])
