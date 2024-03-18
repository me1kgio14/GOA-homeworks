#1
print("პირველი დავალება")

for i in range(1,50):
    if i%5==0 and i%3==0:
        print("fizzbuzz")
    elif i%3==0:
        print("fizz")
    elif i%5==0:
        print("buzz")
    else:
        print (i)


#2
print("მეორე დავალება")

num=int(input("enter number:"))
if num>0:
    print("your number is positive")
elif num<0:
    print("your number is negative")
else:
    print("your number is zero")


#3
print("მესამე დავალება")

for i in range(1,100):
    if i%2==0:
        print(i)


#4
print("მეოთხე დავალება")

result=0
number=100

while number>0:
    result=result+number
    number-=1
print(result)


#5
print("მეხუთე დავალება")

days=int(input("enter any number (from 1 to 7):"))
if days==1:
    print("ორშაბათი")
elif days==2:
    print("სამშაბათი")
elif days==3:
    print("ოთხშაბათი")
elif days==4:
    print("ხუთშაბათი")
elif days==5:
    print("პარასკევი")
elif days==6:
    print("შაბათი")
elif days==7:
    print("კვირა")
else:
    print("you entered wrong number")



#6
print("მეექვსე დავალება")

user_num=int(input("enter any number:"))
if   user_num!=0 and user_num%2==0:
    print("your number is even")
elif user_num!=0 and user_num%2>=1:
    print ("your number is odd")
else:
    print("your number is zero")