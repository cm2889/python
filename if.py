if 10 > 5:
    print ("10 greater than 5") # এই স্টেটমেন্টটি if কন্ডিশনের এর আওতাভুক্ত
    print("IF scope finished")    # এই স্টেটমেন্টটিও if কন্ডিশনের এর আওতাভুক্ত
    
print("Programm ended")

#if and else both conditon are applied
x = 4
if x == 5:
    print("Its 5")
else:
    print("Its not 5")

#if else chain

num = 7
if num == 5:
    print("Number is 5")
else:
    if num == 11:
        print("Number is 11")
    else:
        if num == 7:
            print("Number is 7")
        else:
            print("Number isn't 5, 11 or 7")
#মজার ব্যাপার হচ্ছে এরকম if else if এর চেইনকে একটু সংক্ষেপে elif দিয়েও লেখা যায়। উপরের প্রোগ্রামটি নিচের মত করেও লেখা যায়,
num = 89
if num == 5:
    print("Number is 5")
elif num == 11:
    print("Number is 11")
elif num == 7:
    print("Number is 7")
else:
    print("Number isn't 5, 11 or 7")
