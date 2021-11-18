data = ['eat', 'ate', 'done', 'tea', 'soup', 'node']
dict1 = {}
list1 = []
for i in data:
    list1.append(sorted(i))
print(list1)
list2 = []
for i in list1:
    list2.append(''.join(i))
print(list2)
sub =[]
res = []
for i in data:
    for j in list2:
        if ''.join(sorted(i))==j:
            sub.append(i)
            res.append(sub)
            sub = []
print(res)