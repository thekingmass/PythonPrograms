C=0
def generateNext(d,num):
    return d+num

C=float(input("Please input the starting for your series\n"))
s=float(input("Please input the d for your series\n"))
print ("The series produced by this method is")
print(str(C),", ",end='')
for i in range(1,10):
	print(str(generateNext(s,C)),", ",end='')
	C += s
