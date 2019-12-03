from collections import Counter

with open("data.txt","r") as f:#Tiedosto
    x = f.readlines()
x=[i.strip() for i in x]
kakkoset=0
kolmoset=0
for string in x:
    l = Counter(string).values()
    if 2 in l: kakkoset += 1
    if 3 in l: kolmoset += 1    
print(kakkoset*kolmoset)

print(2 in Counter(x[1]).values())