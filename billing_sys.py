# while True:
#     name= input("enter customer's name: ")
#     total=0

#     while True:
#         print("enter the amount and quantity")
#         amount=float(input("enter amount:"))
#         quantity= float(input("enter quantity: "))
#         total+= amount* quantity
#         repeat=input("do you want to add more items?(yes/no) ")
#         if repeat=="no" or repeat=="NO":
#             break

#     print("-"*40)
#     print("Name:",name)
#     print("Amount to be paid: ",total)
#     print("-"*40)
#     print("************ Happy Shopping *********")


#     repeat1= input("do you want to go to next customer?(yes/no):")
#     if repeat1=="no" or repeat1=="NO":
#         break

# l=[2,3,4,5]
# # square=[x**2 for x in l]
# # print(square)
# square=[]
# for i in l:
#     square.append(i**2)
# print(square)

# fibonacci
# a=0
# b=1

# n=int(input("enter a number:"))
# if n == 1:
#     print(1)
# elif n==0:
#     print(0)
# else:
#     print(a)
#     print(b)
#     for i in range (2,n):
#      c=a+b
#      a=b
#      b=c
#      print(c)

# a=0
# b=1

# print(a)
# print(b)

# for i in range(0,11):
#     c=a+b
#     a=b
#     b=c
#     print(c)

# a=0
# b=1
# n=int(input("enter the number: "))
# if n==1:
#     print(1)
# elif n==0:
#     print(0)
# else:
#     print(a)
#     print(b)
#     for i in range(2,n):
#         c=a+b
#         a=b
#         b=c
#         print(c)

# l=[2,3,4,5]
# a=[]
# for i in l:
#     a.append(i**2)
# print(a)

num=int(input("enter a number :"))

if num<=1:
    print("its not a prime number")
else:
    for i in range(2,num):
        if num%i==0:
            print("number ")

