def invertdict(dict1):
    dict2 = {}
    print(locals())
    for key , value in dict1.items():
        dict2[value]=key
    print(dict2)

dict1 = {'x': 1, 'y': 2, 'z': 3}
invertdict(dict1)

print(globals())

