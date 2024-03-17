#1

# budget=int(input("enter your budget:"))
# item=int(input("enter item price:"))
# if item<=budget:
#     print("you can buy this item")
# else:
#     print("sorry you dont have anough money")



#2

# user_pasword="yoygio12"
# user_input=input("enter user pasword:")
# while user_input!=user_pasword:
#     print("if you want to enter type user_pasword")
#     user_input=input("enter user pasword:")
# print("you have acces")



#3

# for i in range (int(input("enter num:")),int(input("enter num:")),int(input("enter num:"))):
#     print(i)



#4

# s1=int(input("triangle first sight:"))
# s2=int(input("triangle second sight:"))
# s3=int(input("triangle third sight:"))

# walid=(s1+s2 > s3) and (s1+s3 > s2) and (s2+s3 > s1)
# while walid!=True:
    
#     s1=int(input("reenter triangle first sight:"))
#     s2=int(input("reenter triangle second sight:"))
#     s3=int(input("reenter triangle third sight:"))
#     walid=(s1+s2 > s3) and (s1+s3 > s2) and (s2+s3 > s1)
    


#5
operation=input("enter (/,*,+,-):")
number1=int(input("enter number"))
num=int(input("enter number"))
if operation=="-":
    print(num-number1)
elif operation=="+":
    print(num+number1)
elif operation=="*":
    print(num*number1)
else:
    print(number1/num)













    g=int(input("enter your age"))
if g >= 18:
    print("you can chose something")
else:
    print("you can't chose")