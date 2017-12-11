#break
i = 0

while i>=0:
    print(i)

    i=i+1
    if i>=2:
        print("your targeting value is 2")
        break
print("ok finished")

#continue

i = 1

while i>=1:
    print(i)
    i=i+1

    if i == 3:
        print("the value is 3")
        continue
    if i==5:
        print("you r get riched u target")
        print(i)
        break
    
    
print("finsidhed")
