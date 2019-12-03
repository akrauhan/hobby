with open("nimet.txt","r") as f:#Tiedosto
    x = f.readlines()
x=[i.strip() for i in x]
print(x)
