for i in range (0,51,5):
     print(i)



for i in range(2,21,2):
     print(i)



num=1
for i in range(5,10):
     num=(num*i)
     print(num)


result=1
for i in range (1,int(input("enter number more then 1:"))+1):
    result=result*i                
print(result)



user_num=int(input("enter num"))
if user_num %2 ==0:
    user_num/=2
    print(user_num)
else:
    user_num=user_num*3+1
    print(user_num)


num0=10
while num0>1 :
    print(num0)
    num0-=1



user_name=input("enter your name,if you want quit type 'quit': ")
while user_name!="quit":
    print(input("enter your name.if you want quit type 'quit': "))
    user_name=input("enter your name,if you want quit type 'quit': ")
print("wow")



d=10
while d<21:
    print(d)
    d+=2



num8=int(input("enter num"))
while num8<0:
    print(int(input("enter num")))
    num8=int(input("enterh num"))


j=1
while j<11:
    print(j*j)
    j+=1