#  NOT COMPLETED

data = ['eat', 'ate', 'done', 'tea', 'soup', 'node']
data1 = sorted(data,key=lambda x:len(x))
data2 = []
for i in data1:
    data2.append([i])
print(data2)



    # res = []
    # sub = []
    # i = 0
    # j = 1
    # while i<len(data1):
    #     if j < len(data1):
    #         if list(data1[i]).sort()==list(data1[i+j]).sort():
    #             sub.append(data1[j])
    #             j += 1
    #         res.append(sub)
    #         sub = []
    #         i += 1
    # print(res)
