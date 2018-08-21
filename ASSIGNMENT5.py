###################ASSIGNMENT- DECISION AND FLOW CONTROL####################

#Q.1- Take an input year from user and decide whether it is a leap year or not.

yr=int(input("Enter a year to check if its leap year"))
if(yr%4==0):
    if(yr%100==0):
        if(yr%400==0):
            print("LEAP YEAR")
        else:
            print("NOT LEAP YEAR")
    else:
        print("LEAP YEAR")
else:
    print("NOT LEAP YEAR")
    
#Q.2- Take length and breadth input from user and check whether the dimensions are of square or rectangle.
l=int(input("Enter length"))
b=int(input("Enter breadth"))
if(l==b):
    print("It is a square")
else:
    print("It is a rectangle")
#Q.3- Take the input age of 3 people and determine oldest and youngest among them.

x=int(input("Enter age of first person"))
y=int(input("Enter age of second person"))
z=int(input("Enter age of third person"))
if(x>=y and x>=z):
    print("First person is the oldest")
elif(y>=x and y>=z):
    print("Second person is the oldest")
else:
    print("Third person is the oldest")

if(x<=y and x<=z):
    print("First person is the youngest")
elif(y<=x and y<=z):
    print("Second person is the youngest")
else:
    print("Third person is the youngest")


#Ask user to enter age, sex ( M or F ), marital status ( Y or N ) and then using following rules print their place of service
age=int(input("Enter age"))
sex=input("Enter sex")
marital=input("Enter marital status")
if(sex=='F'):
    print("Work in Urban Areas")
else:
    if(age>=20 and age<=40):
        print("Can work anywhere")
    elif(age>=40 and age<=60):
        print("Work in urban areas")
    else:
        print("Error in input")


#Q.5- A shop will give discount of 10% if the cost of purchased quantity is more than 1000.Ask user for quantity Suppose, one unit will cost 100. Judge and print total cost for user.
q=int(input("Enter quantity"))
c=100*q
if(c>1000):
    c=c-(c*0.1)
    print("Total cost is =",c)
else:
    print("Total cost is =",c)



###################loops#####################

#Q.1- Take 10 integers from user and print it on screen.
lst=[]
for i in range(10):
    n=int(input("Enter a number"))
    lst.append(n)
print(lst)

#Q.2- Write an infinite loop.An infinite loop never ends. Condition is always true.
while True:
    print("*")

#Q.3- Create a list of integer elements by user input. Make a new list which will store square of elements of previous list.
lst=[]
lst1=[]
n=int(input("enter number of elements"))
for i in range(n):
    a=int(input("Enter number"))
    lst.append(a)
for i in lst:
    c=i*i
    lst1.append(c)
print(lst1)

#Q.4- From a list containing ints, strings and floats, make three lists to store them separately
lst1=[]
lst2=[]
lst3=[]
lst4=[]
a=int(input("Enter total number of inputs"))
for i in range(a):
    b=input("Enter elements of list")
    lst1.append(b)
for i in lst1:
    if(i.isdigit()):
        lst2.append(i)
    elif(i.isalpha()):
        lst3.append(i)
    else:
        lst4.append(i)
print(lst2)
print(lst3)
print(lst4)

#Q.5- Using range(1,101), make a list containing only prime numbers.
lst=[]
for i in range(1,101):
    if(i>1):
        c=False#c is flag here
        for j in range(2,i):
            if(i%j==0):
                c=True
        if not c:
            lst.append(i)
print(lst)

#Q.6- Print the following patterns:
for i in range(0,5):
    for j in range(i):
        print("*",end='')
    print()
#Q.7- Take inputs from user to make a list. Again take one input from user and search it in the list and delete that element, if found. Iterate over list using for loop.
lst=[]
n=int(input("Enter number of elements of list"))
for i in range(0,n):
    a=int(input("Enter element"))
    lst.append(a)
num=int(input("Enter the number you want to delete from list"))
v=lst.count(num)
for i in range(0,v):
    x=lst.index(num)
    del(lst[x])
print(lst)





