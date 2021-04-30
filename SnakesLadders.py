import random
rand1 = 0
rand2 = 0
sum1 = 0
sum2 = 0

while (sum1 < 50 and sum2 < 50):
    sum1 += random.randint(2,12)
    sum2 += random.randint(2,12)

    if sum1 == 32:
        sum1 += 7
        print("Player 1 found a ladder! Plus 7")
    if sum2 == 32:
        sum2 += 7
        print("Player 2 found a ladder! Plus 7")
        
print("Player 1: ", sum1)
print("Player 2: ", sum2)
if sum1 > sum2:
    print("Player 1 wins")

else:
    print("Player 2 wins")
