with open("data.txt","r") as f:#Tiedosto
    x = f.readlines()
x = [i.strip().split()[-2:] for i in x]
s = []
for l in x:
    s.append((l[0].split(','),l[1].split('x')))
print(s)