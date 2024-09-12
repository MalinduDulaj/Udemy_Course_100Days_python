Capitals = {
    "France" : "Paris",
    "German" : "Berlin",
}

#Nested List IN Dictionaries

travel_log = {
    "France" : ["paris","little","mons"],
    "German" : ["stargut","Berlin"]
}

print(travel_log["France"][1])

nested_List=["A","B",["C","D"],["E","F","J"]]
print(nested_List[2])  #['C', 'D']
print(nested_List[2][0]) #c
print(nested_List[2][1]) #D
print(nested_List[3][2]) #J
print(nested_List[3])  #['E', 'F', 'J']