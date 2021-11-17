def valuesort(dict1):
    vals = sorted(dict1.keys())
    vals2 = []
    dict2 = {}
    i = 0
    while i<len(vals):
        dict2[vals[i]]=dict1[vals[i]]
        vals2.append(dict1[vals[i]])
        i += 1
    print(dict2)
    print(vals2)

dict1 = {'x': 1, 'y': 2, 'a': 3}

valuesort(dict1)