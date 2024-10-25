# age = int(input("How old are you : "))
# if age > 18:
#     print("you can drive at {age}.")

# age = string input not working this problem config 

try:
    age = int(input("How old are you : "))

except ValueError:
    print("You have typed in a an invalid number. Please try again with numeric number.")
    age = int(input("How old are you : "))
        
if age > 18:
    print(f"you can drive at {age}.")

