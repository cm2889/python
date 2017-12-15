import random

heads = 0
tails = 0

for i in range(0,100):
    flip = random.randint(0,1)
    #print(flip) show 0 and 1

    if flip == 0: #heads
        heads+= 1
    else:
        tails+=1
print ("heads counts %i." %heads)
print ("tails counts %i." %tails)
