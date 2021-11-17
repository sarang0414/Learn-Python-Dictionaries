print("Hello %(name)s Welcome. Your ID is %(id)d . Thank You" %{'name': 'User','id':29})

place = "Kalpetta"
id = 20

print("The id of place %(place)s is %(id)d" %{'id':id,'place':place})

dict1 = {
    'a':None,
    'b':456,
    'c':789
}

print("The data are %(data1)d and %(data2)d" %{'data1':dict1['b'],'data2':dict1.get('c')})