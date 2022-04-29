from multiprocessing.sharedctypes import Value


capitals={
    'usa':'dc','India':'New Delhi'
}
print(capitals['India'])
print(capitals.get('germany'))
print(capitals.keys())
print(capitals.values())
print(capitals.items())

for key,value in capitals.items():
    print(key,value)
