x = []
with open("data.txt","r") as f:#Tiedosto
    x = f.readlines()
x = [int(i.strip()) for i in x]
taajuus=0
taajuudet = {}
jatka = True
while jatka:
    for k in x:
        if taajuus in taajuudet:
            print(taajuus)
            jatka=False
            break
        taajuudet[taajuus]=1
        taajuus += k