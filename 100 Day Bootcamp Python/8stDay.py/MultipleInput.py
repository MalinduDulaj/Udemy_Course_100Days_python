def greet_with(name,location):
    print(f"Hello {name}. ")
    print(f"what is it like in {location}.")

greet_with("malindu","sweden") 
# Hello malindu. 
# what is it like in sweden.

greet_with("sweden","malindu")  #data swith
# Hello sweden. 
# what is it like in malindu.

greet_with(location="sweden",name="malindu") # arguments call
# Hello malindu. 
# what is it like in sweden.
