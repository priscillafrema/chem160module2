from random import choices
nrolls=10000
total=0
ndice=30
for i in range(nrolls):
    dice=choices(range(1,7),k=ndice)
    dice.sort(reverse=True)
    total=total+dice[0]+dice[1]
print("Average roll=",total/nrolls)

#increasing the ndice from 2 to 3, increases the average sum from 6.9899 to 8.4476.
#No, I believe it would not be a fair game if my friend allowed me to add one to my sum for just 2 dice.