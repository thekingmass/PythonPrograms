def calc_sum(a,b,countnegative=False):
    if(a>0 and b>0):
        countnegative=True
    if (countnegative):
        return a+b
    else:
        return ("A negative value found without count negative value allowed! -- skipping calculation")
a=int(input("Please input the first number\n"))
b=int(input("Please input the second number\n"))
print ("The sum of", a,"and", b ,"is:", calc_sum(a,b,countnegative=False)) # Printing Outpput without allowing countnegative number
print ("The sum of", a,"and", b ,"is:", calc_sum(a,b,countnegative=True))  # Printing Outpput with allowing countnegative number
