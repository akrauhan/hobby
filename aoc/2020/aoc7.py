import helpFunctions as hf

input = hf.txt2Array("aoc7.txt")
input = [x.replace("\n", "") for x in input]
print(input)


def initBags(rulelist):
    bagdict = {}
    for rule in rulelist:
        bag = rule.split("bags contain")[0]
        allowedbags = rule.split("bags contain")[1].replace(".", ",").replace("bags", "bag").split("bag,")
        append_value(bagdict, bag, allowedbags)

    return bagdict

def append_value(dict_obj, key, value):
    # Check if key exist in dict or not
    key = key.strip()
    if key in dict_obj:
        # Key exist in dict.
        # Check if type of value of key is list or not
        if not isinstance(dict_obj[key], list):
            # If type is not list then make it list
            dict_obj[key] = [dict_obj[key]]
        # Append the value in list
        dict_obj[key].append(value)
    else:
        # As key is not in dict,
        # so, add key-value pair
        dict_obj[key] = value



bagrules = initBags(input)
print(bagrules)


def bagsThatContain(bag):
    c = 0
    for key in bagrules:
        bagrule = bagrules[key]


        for possbag in bagrule:
            possbag = possbag.strip()
            if possbag == "no other": 
                return 0

            possbag = possbag[1:].strip()
            if possbag == bag:
                return 1
            c += bagsThatContain(possbag)
    return c

def bagCanContain(container, bag):
    
    for possbag in bagrules[container]:
        possbag = possbag.strip()
        if possbag == "no other":
            return False
        possbag = possbag[1:].strip()
        if possbag == bag: 
            return True

    for possbag in bagrules[container]:
        possbag = possbag.strip()
        possbag = possbag[1:].strip()
        return bagCanContain(possbag, bag)

    return False
    
c = 0
for bag in bagrules:
    if bagCanContain(bag, "shiny gold"):
        c += 1
print(c)
print(bagCanContain("bright white", "shiny gold"))
print(bagCanContain("faded blue", "shiny gold"))
