def print_even(s=1,e=10):
    for i in range(s,e+1):
        if i%2==0:
            print(str(i)+",", end=" ")
    print()
print ("The series is:")
print_even()
print ("The series is:")
print_even(0)
print ("The series is:")
print_even(10,100)
print ("The series is:")
print_even(e=100)
