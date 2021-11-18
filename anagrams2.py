def anagrams(data):
    data1 = [''.join(sorted(i)) for i in data]
    print(data1)
    dict1 = {}
    for i , dt in enumerate(data1):
        dict1.setdefault(dt,[]).append(i)
    print(dict1)
    list2 = []
    res  = []
    for index in dict1.values():
        list2 =[data[i] for i in index]
        res.append(list2)
    print(res)

anagrams(['eat', 'ate', 'done', 'tea', 'soup', 'node'])