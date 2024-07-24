import random
print("Welcome to the heads or tails random generator, Call your Side let's see will you win!")
random_int = random.randint(0,1)

if random_int == 1:
    print("You have won the toss")
else:
    print("You lost the toss")