def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# Example inputs and expected outputs
num1 = 73
num2 = 75

# Checking if num1 is a prime number
print(f"{num1}: {is_prime(num1)}")  # Output: true

# Checking if num2 is a prime number
print(f"{num2}: {'true' if is_prime(num2) else 'lies'}")  # Output: lies

#-----------------------------------------------------------------------------------------------

# def is_prime(num):
#     if num == 2:
#         return True
#     if num == 1:
#         return False
 
#     # Loop through all the numbers between 2 and the number
#     for i in range(2, num):
#         # Check if the number (num) can be divided by the potential prime number
#         if num % i == 0:
#             return False
 
#     # this return is outside the for loop which will only run once the loop finishes and none of the numbers are divisible. Therefore it is prime.
#     return True