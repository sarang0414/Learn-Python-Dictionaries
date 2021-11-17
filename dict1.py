dict1 = {
    'a':123,
    'b':456,
    'c':789
}

for i in dict1:
    print(i)

for k , v in dict1.items():
    print(k,v)
for k in dict1.keys():
    print(k)
for v in dict1.values():
    print(v)

print('a' in dict1)
print('z' in dict1)

# Note : has_key is removed in python 3.x
