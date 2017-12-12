def my_func():
    print("Printing Hello")

what_i_got = my_func()
print(what_i_got)


#if i get some modify

print("none default print form here")
def my( x = None):
    if x:
       return x*x
    else:
        return 0
print (my())
print (my(5))
    
