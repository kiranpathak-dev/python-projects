#Write a virtual coin toss program. It will randomly tell the user "Heads" or "Tails"
import random

toss_result = random.randint(0,1)

if toss_result == 1:
    print("Heads")
else:
    print("Tails")