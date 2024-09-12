import random

#random number with interger= randint

random_interger=random.randint(1,10)
print(random_interger)

random_number_0_1 = random.random()
print(random_number_0_1)

#float number=unifrom

random_float = random.uniform(1,10)
print(random_float)


random_Head_Tails=random.randint(0,1)
if random_Head_Tails == 0:
    print("Heads")

else:
    print("Tails")