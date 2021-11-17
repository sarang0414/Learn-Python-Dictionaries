def word_frequency(data):
    freq = {}
    for i in data:
        freq[i] = freq.get(i,0)+1
    print(freq)
    new_freq = []
    for i , j in freq.items():
        new_freq.append((j,i))
    new_freq = sorted(new_freq,reverse=True)
    print(new_freq)
    dict1 = dict(new_freq)
    dict2 = {}
    for k , v in dict1.items():
        dict2[v]=k
    print(dict2)

word_frequency(['abhk','b','c','c','b','b'])