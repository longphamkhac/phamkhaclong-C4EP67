# import random
# a=random.randint(0,9)
# b=random.randint(0,9)
# d=random.randint(0,3)
# s=a+b
# ketqua=s+d
# print()
# if s==ketqua:
#     print("Dung")
# else:
#     print("Sai")
# score=0
# for i in range():
#     if 

from random import randint, choice
from calc import calc
# n=calc(1,2,"+")
# print(n)
a=randint(0,9)
b=randint(0,9)
operators_poll=["+","-","*","/"]
operator=choice(operators_poll)
result=calc(a,b,operator)
random_num=randint(-1,1)
display_result=result+random_num
print(f'{a}{operator}{b}={display_result}')
choice=input("T/F").upper()
if random_num==0:
    if choice=="T":
        print("Yeah")
    if choice=="F":
        print("Sai cmnr")
if random_num!=0:
    if choice=="F":
        print("Yeah")
    if choice=="T":
        print("Sai cmnr")

print("")











