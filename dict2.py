dict1 = {
    'a':None,
    'b':456,
    'c':789
}

dict1.setdefault('a',852)
print(dict1.get('c'))
dict1.setdefault('d',741)
print(dict1)

