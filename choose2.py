from random import choices
ntrials=1000000
limit=1000
count=0
for i in range(ntrials):
    rand=choices (range(1,limit+1) ,k=3)
    if rand[0] +rand[1]<=rand[2] :
        count=count+1
    print("Fraction=",count/ntrials)

#the probabilities are different because our import choices are random.
#Yes,increasing the ntrials from 10000 to 1000000 increased the time it took for the simulation to run.
#No, it did not really change the percentage by much.