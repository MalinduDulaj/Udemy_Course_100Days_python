# def is_leap(year):
#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 400 == 0:
#                 return True
#             else:
#                 return False
#         else:
#             return True
#     else:
#         return False


def is_leap(year):
    # Check if the year is divisible by 4
    if year % 4 == 0:
        # If it is divisible by 4, check if it is divisible by 100
        if year % 100 == 0:
            # If it is also divisible by 100, check if it is divisible by 400
            if year % 400 == 0:
                return True  # Divisible by 400, so it is a leap year
            else:
                return False  # Divisible by 100 but not 400, not a leap year
        else:
            return True  # Divisible by 4 but not 100, so it is a leap year
    else:
        return False  # Not divisible by 4, not a leap year

