# at first pick a random number and it will continue untill find the random number , if provide numbe is
# more than random number show too high and less show too low
import random

cpu =random.randint(1,100)
print(cpu)

player = int(input("Enter a numbr between 1-100: "))

while player != cpu:
    if player > cpu:
        print("Too high")
    else:
        print("Too low")
    player= int(input("enter a nrumber between 1-100: "))
else:
    print("well done !")
