import random

random_number = random.randint(1, 10)
print(random_number)
random_number = random.randint(1, 10)
print(random_number)

random_float= random.uniform(1, 10)
print(random_float)

random_heads_or_tails = random.randint(a=0, b=1)
if random_heads_or_tails == 0:
    print("heads")
else:
    print("tails")
