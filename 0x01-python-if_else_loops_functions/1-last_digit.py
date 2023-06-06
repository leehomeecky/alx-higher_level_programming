#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastNo = abs(number) % 10
if number < 0:
    lastNo *= -1
print("Last lastNo of {} is {} and is ".format(number, lastNo), end="")
if lastNo > 5:
    print("greater than 5")
elif lastNo == 0:
    print("0")
else:
    print("less than 6 and not 0")
