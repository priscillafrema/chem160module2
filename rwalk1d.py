from random import choice
trials=1000
steps=10000
gothome=0
for i in range(trials):
    point=0
    for step in range(steps):
        point+=choice((-1,1))
        if point==0:
            gothome+=1
            break
print("Fraction that got home=",gothome/trials)

#my result was o.99. Yes, the random walker does make it home.
#changing the number of trails from 100 to 1000 affected my initial result. It increases my the fraction from 0.99 to 0.994. Therefore, I believe increasing the number of trials does increase the fraction.