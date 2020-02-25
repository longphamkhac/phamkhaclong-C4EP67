
# i = 2
# while(i < 100):
#    j = 2
#    while(j <= (i/j)):
#       if i%j==0: break
#       j = j + 1
#    if (j > i/j) : print (i, " la so nguyen to")
#    i = i + 1

# print ("Good bye!")


# i=1
# while i<10:
#     print(i)
#     i=i+1

# i=1
# while i<10:
#     if i%2==0:
#         print(i, "la so chan")
#     else:
#         print(i, "khong phai la so chan")   
#     i=i+1

# k_number=0
# while k_number<10:
#     k_number=k_number+1
#     if k_number%2==0:
#         continue
#     print(k_number, "la so le")

# five_even_numbers=[]
# k_number=0
# while k_number<10:
#     k_number=k_number+1
#     if k_number%2!=0:
#         continue
#     five_even_numbers.append(k_number)
# print(five_even_numbers, sep=", ")


# a=0
# while a<5:
#    print("Value of a is", a)
#    a=a+1
#    if a>3:
#       print("a is greater than 3")
#       break


# five_numbers=[]
# k_number=0
# while k_number<11:
#    if k_number%2==0:
#       five_numbers.append(k_number)
#       if k_number==5:
#          break
#    k_number=k_number+1
# print(five_numbers)
      
# a=["Con ga", "Con cho", "Con heo", "Con bo"]
# for idx, dong_vat in enumerate(a, 1):
#    print(idx,".",dong_vat)

# def kteam():
   # print('Hello Kteam')
   # print('Free education')

# def kteam(text, age=20):
#    print(text)
#    print(age)
# kteam("Long")

# def hteam(a, b):
#    print(a, b)
# hteam(b=3, a="free education")

# k_number=1
# while k_number<10:
#    if k_number%2==0:
#       k_number=k_number+1
#       continue
#    else:
#       print(k_number, "la so le")
#       k_number=k_number+1

         
# def kteam(text):
#    print("Xin chao", text, "!")
# kteam("Day la 1 ham de truyen vao dung de xin chao luc moi quen nhau")

# def giatrituyetdoi(so):
#    print("Day la ham tra ve gia tri tuyet doi")
#    # print(so)
#    if so>=0:
#       return so
#    if so<=0:
#       return -so
# print(giatrituyetdoi(-4))
# # giatrituyetdoi(-2)
# print(giatrituyetdoi(-3))

# n=int(input("Nhap 1 so tu nhien n vao day"))
# d=dict()
# for i in range(1, 1+n):
#    d[i]=i*i
# print(d)

# lines = []
# while True:
#    s = input()
#    if s:
#       lines.append(s.upper())
#    else:
#       break;
# # Bài Python 12, Code by Quantrimang.com
# for sentence in lines:
#     print (sentence)

# n=input("Nhap cac so nhi phan duoc ngan cach boi dau phay")
# value=[]
# items=[x for x in n.split(",")]
# for i in items:
#    if int(i)%5==0:
#       value.append(i),
# print(*value, sep=",")


# def kteam(a,b,c,d):
#    print(a,b,c,d)
# kteam(3,"free edcucation", d=1, c=4)

# def teo(a, b=2, c=3, d=4):
#    f=(a+b)*(c+d)
#    print(f)
# teo(1, b=2)

# def kteam(k,t,e,r="kter"):
#    print(k)
#    print(t, e)
#    print("end", r)
# lst=[123,"kteam",69.96]
# # kteam(lst[0],lst[1],lst[2],lst[3])
# kteam(*lst)

# def kteam(*args):
#    print(args)
# kteam(*(i for i in range(7)))

# def kteam(name, member):
#    print("name:", name)
#    print("member:", member)
# dic={"name": "kter", "member": 69}
# kteam(**dic)

# def kteam(*kwargs):
#    for key, value in dic.items():
#       print(key,":",value)
# dic={"name": "kter", "member": 69}
# kteam(*dic)

# a=input("Nhap cac chu so duoc ngan cach bang dau phay vao day")
# b=[int(c) for c in a.split(",")]
# value=[]
# for i in b:
#    if int(i)%2!=0:
#       value.append(i)
# print(value)

# a=input("Nhap cau tra loi cua ban vao day: ")
# dic={"DIGITS": 0, "LETTERS": 0}
# for i in a:
#    if i.isdigit():
#       dic["DIGITS"]+=1
#    if i.isalpha():
#       dic["LETTERS"]+=1
#    else:
#       pass
# print(dic["DIGITS"])
# print(dic["LETTERS"])


# s = input("Nhập câu của bạn: ")
# # Bài tập Python 16, Code by Quantrimang.com
# d={"DIGITS":0, "LETTERS":0}
# for c in s:
#  if c.isdigit():
#    d["DIGITS"]+=1
#  elif c.isalpha():
#    d["LETTERS"]+=1
#  else:
#    pass
# print ("Số chữ cái là:", d["LETTERS"])
# print ("Số chữ số là:", d["DIGITS"])


# a=input("Nhap 1 cum tu ma ban muon nhap vao day: ")
# dic={"CHU_CAI_THUONG": 0, "CHU_CAI_HOA": 0}
# for c in a:
#    if c.islower():
#       dic["CHU_CAI_THUONG"]+=1
#    if c.isupper():
#       dic["CHU_CAI_HOA"]+=1
# print("CHU_CAI_HOA LA", dic["CHU_CAI_HOA"])
# print("CHU_CAI_THUONG LA", dic["CHU_CAI_THUONG"])

# while True:
#    a=int(input("Nhap 1 so tu nhien a: "))
#    b=11*a
#    c=111*a
#    d=1111*a
#    so_cantim=a+b+c+d
#    print("So nguoi dung can tim la", so_cantim)

# net_amount=0
# while True:
#     n=input("Nhập lịch sử giao dịch, lưu ý phải có dấu cách giữa chữ và số: ")
#     if not n:
#         break
#     value=n.split(" ")
#     operator=value[0]
#     amounts=int(value[1])
#     if operator=="D":
#         net_amount+=amounts
#     if operator=="W":
#         net_amount-=amounts
# print(net_amount)


# import re
# while True:
#     print("Luu y khi nhap xong mat khau ban muon dang ki thi hay nhan enter de den buoc tiep theo")
    # matkhau_ngdung=input("Nhap mat khau ban muon dang ki vao day: ")
#     if not matkhau_ngdung:
#         break
#     value=[]
    # items=[a for a in matkhau_ngdung.split(" ")]
#     for i in items:
#         if len(i)<6 or len(i)>12:
#             print("Hay nhap mat khau lai tu dau")
#             continue
#         else:
#             pass
#         if not re.search("[a-z]", i):
#             print("Hay nhap mat khau lai tu dau")
#             continue
#         if not re.search("[0-9]", i):
#             print("Hay nhap mat khau lai tu dau")
#             continue
#         if not re.search("[A-Z]", i):
#             print("Hay nhap mat khau lai tu dau")
#             continue
#         if not re.search("[$#@]",i):
#             print("Hay nhap mat khau lai tu dau")
#             continue
#         else:
#             pass
#     break
# value.append(i)
# for c in value:
#     print("Ban da dang ki thanh cong mat khau: ", c, end="")

# matkhau_ngdung=input("Nhap mat khau ban muon dang ki vao day: ")
# items=(a for a in matkhau_ngdung.split())
# a=tuple(items)
# print(a)
# from operator import itemgetter, attrgetter
# items=[]
# while True:
#     nhap_dulieungdung=input("Nhap du lieu vao day")
#     if not nhap_dulieungdung:
#         break
#     values=(a for a in nhap_dulieungdung.split())
#     a=tuple(values)
#     items.append(a)
# print(sorted(items, key=itemgetter(0,1,2)))







    






























