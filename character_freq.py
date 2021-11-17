import sys

def character_freq(data):
    freq = {}
    for ch in data:
        freq[ch] = freq.get(ch,0)+1
    print(freq)

f = open('file1.txt')
dt = f.read()
character_freq(dt)
f.close()

if '.py' in sys.argv[0]:
    print("Python File")
else:
    print("Not a Python File")