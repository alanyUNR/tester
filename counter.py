#wrote up a counter
# print('1 2 3')
# #write up a loop
# for x in range(10):
#     print(x)
#getting rid of the print 1
#adding a function that rolls a die
#fixed dice roller 10.19, now it returns a random value 1 - 6
import random
def rollDie():
    return random.randint(1, 6)

#testing
print(rollDie())


