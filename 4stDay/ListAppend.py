name=["kmal","nimal","sunil"]
print(name[1])  #nimal
print(name)    #['kmal', 'nimal', 'sunil']

name.append("mali")
print(name)   #['kmal', 'nimal', 'sunil', 'mali']

name.extend(["bina","nima"])
print(name) #['kmal', 'nimal', 'sunil', 'mali', 'bina', 'nima']

# name.append("vije","suje")      //[append note use both items add to list] *its extend use
# print(name)

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
fruits[-1] = "Melons"   # "Pears"  remove to the list, AND add to list "Melons"
fruits.append("Lemons")
print(fruits)    #['Strawberries', 'Nectarines', 'Apples', 'Grapes', 'Peaches', 'Cherries', 'Melons', 'Lemons']