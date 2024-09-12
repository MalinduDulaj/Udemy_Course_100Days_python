def my_function(a):
    if a < 40:
        return                # output=None
        print("Terrible")
    if a < 80:
        return "Pass"
    else:
        return "Great"
print(my_function(25))



#-----------------------------------------------------------------------------
def my_function(a):
    if a < 40:

        print("Terrible")
    if a < 80:
        return "Pass"
    else:
        return "Great"
print(my_function(25))   # output = Terrible
                         #          Pass