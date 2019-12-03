x = []
with open("data.txt","r") as f:#Tiedosto
    x = f.readlines()
x = [int(i.strip()) for i in x]
print(sum(x))