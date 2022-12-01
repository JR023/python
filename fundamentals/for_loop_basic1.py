#basic
for x in range(0, 150, 1) :
    print (x)
#multiples of 5
for x in range(5, 1000 ,5):
    print (x)
#counting the dojo way
x=100
for x in range(1,x+1,1):
    if (x%10 ==0):
        print ("Coding Dojo")
    elif (x%5 == 0):
        print ("Coding")
    else:
        print (x)
#it's so huge
x=500000
sum=0
for x in  range (1,x+1,1):
    if x%2!=0:
        sum += x
print (sum)
#countdown by four
x=2018
while x>0:
    print (x)
    x=x-4
#flexible counter
lownum=2
highnum=9
mult=3
for x in range (lownum, highnum+1, 1):
    if (x%mult==0):
        print (x)
