# for y in range(1,10):
#     for x in range(1,10):
#         if y*x > 9:
#             print(y * x,end=' ')
#         if y*x <=9:
#             print(y * x,end='  ')   
#     print() 
           

# for i in range(21):
#     if i%2==0:
#         print(1,end=' ')   
#     else:
#         print(0,end=' ')  

# n=int(input("điền 1 số tự nhiên n"))
# for n in range(0,20):
#     if n%2==0:
#         print(1,end=' ')
#     else:
#         print(0,end=' ')

# n=int(input("nhap 1 so tu nhien n"))
# for y in range(1,n):
#     for x in range(1,n):
#         if y*x>10:
#             print(y*x,end=' ')
#         if y*x<10:
#             print(y*x,end='  ')    
#     print()  
# 
# for i in range(9):
#     for x in range(9):
#         if i%2==0:
#             if x%2==0:
#                 print(1,end='  ')
#             if x%2!=0:
#                 print(0,end='  ')
#         if i%2!=0:
#             if x%2==0:
#                 print(0,end='  ')
#             if x%2!=0:
#                 print(1,end='  ')
#     print() 

# list_so=[5,1,8,92,7,30]
# J=[]
# for i in list_so:
#     if i%2==0:
#         J.append(i)
# print(*J, sep=',')

# n=input("nhập các số cần tìm vào đây").split()
# J=[]
# for i in n:
#     i=int(i)
#     if i%2==0:
#         J.append(i)
# print(*J, sep=', ')


# n=input("nhập các số cần tìm vào đây").split()
# a=int(n)
# sum(a)

# n=input("nhập các số cần tìm vào đây").split()
# tong_cacso=0
# for i in n:
#     i=int(i)
#     tong_cacso=tong_cacso+i
# print(tong_cacso)

# def tong_cacso():
#     for i in n:
#         i=int(i)
#         tong_cacso=tong_cacso+i
#         return tong_cacso
# print(tong_cacso)
# J=[]
# for i in n:
#     i=int(i)
#     J.append(i)
#     a=sum(J)
# print(a)

# fruitList = ["apple", "apricot", "banana","coconut", "lemen", "pear", "plum"]
# for fruit in fruitList:
#     print("fruit:", fruit.title())
# print(fruitList)
# print(fruitList)
# print("element at".title(), len(fruitList))
# # for i in range(0, len(fruitList)):
# #     print("element".title(), i+1, fruitList[i])
# subList=fruitList[1:4]
# # # print("subList".title(),"=", subList)
# # print("fruitList[-1]".title(), ":", fruitList[-1])
# # print("fruitList[-3]".title(), ":", fruitList[-3])
# print("\n")
# subList1 = fruitList[-4:]
# print ("Sub List fruitList[-4: ] ")
# print (*subList1, sep=", ")
# print("\n")
# subList2=fruitList[-2:]
# print("SubList fruitList[-2:]")
# print(*subList2, sep=", ")
# fruitList[1:6]=["orange", "grape"]
# print(fruitList)
# del fruitList[6]
# del fruitList[5]
# fruitList.pop(2)
# fruitList.remove("apple")
# fruitList.remove("coconut")
# numbers=[111, 334, 456, 4546, 43535]
# max_number=max(numbers)
# print(max_number)
# min_number=min(numbers)
# print(min_number)
# a=numbers.count(111)
# print(a)
# tuplea=(2001, 2003, 2007)
# a=numbers.extend(tuplea)
# print(a)

# tup=( i for i in range(10) if i%2==0)
# a=tuple(tup)
# print(a)

# import array as arr
# a=arr.array("d", [1.1, 3.5, 4.5])
# print(a)

# import array as arr 
# a = arr.array('i', [2, 4, 6, 8])   
# print("Phần tử đầu tiên:", a[0])
# print("Phần tử thứ 2:", a[1])
# print("Phần tử cuối cùng:", a[-1])

# import array as arr 
# numbers_list = [5, 85, 65, 15, 95, 52, 36, 25]
# numbers_array = arr.array('i', numbers_list)
# print(numbers_array[2:5])
# print(numbers_array[:-5])
# print(numbers_array[5:])
# print(numbers_array[:])

# letters=["a", "b", "c", "d"]
# for num in range(0,10):
# #Lặp trên các thừa số của một số trong dãy
#  for i in range(2,num): 
# #Xác định thừa số đầu tiên (phép chia có số dư bằng 0)
#       if num%i == 0: 
#          j=num/i #Ước lượng thừa số thứ 2
#          print ('%d bằng %d * %d' % (num,i,j))
#          break
#       else: # Phần else trong vòng lặp
#         print (num, 'là số nguyên tố')   

        #Lặp dãy từ 0 đến 10
# for num in range(0,10):
# #Lặp trên các thừa số của một số trong dãy
#  for i in range(2,num): 
# #Xác định thừa số đầu tiên (phép chia có số dư bằng 0)
#       if num%i == 0: 
#         #  j=num/i #Ước lượng thừa số thứ 2
#          print("Không phải số nguyên tố")
#          break #Dừng vòng for hiện tại, chuyển đến số tiếp theo trong vòng for đầu tiên
#       else: # Phần else trong vòng 
#         print (num, 'là số nguyên tố')


# list_dientich=[11743, 9224, 4335, 1204, 996, 1009]

# print("Hello, my name is Hiep and these are my sheep sizes")
# num=[5, 7, 300, 90, 24, 50,75]
# # print(num)
# for i in num:
#   print(i,end=' ')
# print()
# a=max(num)
# print("Now my biggest sheep has size", a, "let's shear it")
# print("After shearing, here is my flock")
# num.pop(3)
# for i in num:
#   print(i,end=' ')
# print()
# print("Month", 1)
# print("One month I has passed, now here is my flock")
# num1=[55, 57, 58, 140, 100, 74, 125]
# for i in num1:
#   print(i, end=' ')
# print()
# b=max(num1)
# print("Now my biggest sheep has size", b, "let's shear it")
# print("After shearing, here is my flock")
# num1.pop(3)
# for i in num1:
#   print(i,end=' ')
# print()
# print("Month", 2)
# print("One month I has passed, now here is my flock")
# num2=[105, 107, 108, 58, 124, 150, 175]
# for i in num2:
#   print(i, end=' ')
# print()
# c=max(num2)
# print("Now my biggest sheep has size", c, "let's shear it")
# print("After shearing, here is my flock")
# num2.pop(6)
# for i in num2:
#   print(i, end=' ')
# print()
# print("Month", 3)
# print("One month I has passed, now here is my flock")
# num3=[155, 157, 158, 108, 174, 200, 58]
# n=sum(num3)
# print("My flock has size in total:", n)
# print("I would get", 1010 * 2)


# list_danso=[150300, 247100, 333300, 266800, 420900, 318000]
# list_quan=["ST", "BD", "BTL", "CG", "DD", "HBT"]
# print(max(list_danso))
# print(min(list_danso))
# print("Quận có dân số đông nhất là," "HBT")
# print("Quận có dân số ít nhất là," "ST")
# list_dientich=[11743, 9224, 4335, 1204, 996, 1009]
# list_matdo=[]
# for i in range(6):
#   a=list_danso[i]/list_dientich[i]
#   list_matdo.append(a)
# print("Mật độ lần lượt của các quận là:", list_matdo) 
# a1=sum(list_matdo)
# print("Tổng mật độ dân cư là:", a1)
# a2=len(list_quan)
# print("Tổng số quận là:", a2)
# a3=a1/a2
# print("Mật độ trung bình của các quận là:", a3)


# print("Welcome to our shop, what do you want (C, R, U, D)")
# a=input("Choose your letter")
# C=["T-Shirt", "Sweater"]
# for i in C:
#   print(i, end=' ')
# print()
# a=input("Enter new item")
# our_items.append(a)
# for i in our_items:
#   print(i, end=' ')
# print()
# b=int(input("Update position"))
# our_items[b]=input("Enter new item")
# for i in our_items:
#   print(i, end=' ')
# print()
# c=int(input("Delete position"))
# our_items.pop(c)
# for i in our_items:
#   print(i, end=' ')


# num=["long", 1, 2, 3]
# print(num)
# tup=(1,2,3,4,5)
# print(tup)
# item=(1,2,3,4,5)
# print(item)
# a=tuple("Kteam")
# print(a)
# for i in a:
#         print(i, end=" ")




         






