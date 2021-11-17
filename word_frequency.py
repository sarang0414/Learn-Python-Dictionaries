import sys

def word_frequency(data):
    freq = {}
    for i in data:
        freq[i] = freq.get(i,0)+1
    print(freq)

word_frequency(['abhk','b','c','c','b','b'])

f = open('file1.txt')
dt = f.read().split()
word_frequency(dt)
f.close()
print(sys.argv, len(sys.argv))