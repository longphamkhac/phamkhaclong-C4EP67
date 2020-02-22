import decimal
print(decimal.Decimal(0.1))
print(decimal.Decimal(1.1+2.2))

from decimal import Decimal
print(Decimal("1.1")+Decimal("2.2"))
print(Decimal("4.0")*Decimal("2.5"))
import fractions
print(fractions.Fraction(4.5))
print(fractions.Fraction(5.12))
print(fractions.Fraction(2.5))
print(fractions.Fraction(3.5))
# from fractions import Fraction as F
# import math
# print(math.pi)
# print(math.factorial(8))
# print(math.log2(4))
# from fractions import Fraction as F
# import math
# n=int(input("nhap 1 so tu nhien bat ki"))
# print(math.factorial(n))

# n=int(input("nhập 1 số tự nhiên n"))
# tong=0
# for i in range(1, n+1):
#     tong=tong+i
# print("Tổng của n số hạng liên tiếp là", tong)

# n=int(input("nhập 1 số chẵn n"))
# tong=0
# for i in range(2, n+1, 2):
#     tong=tong+i
# print("Tổng của n số chẵn liên tiếp là", tong)

# n=int(input("nhập 1 số tự nhiên n"))
# tich_giaithua=1
# if n==1 or n==0:
#     print("kết quả của bạn là", tich_giaithua)
# else:
#     for i in range(2, n+1):
#         tich_giaithua=tich_giaithua*i
#     print("Kết quả của bạn là", tich_giaithua)

# n=int(input("nhập 1 số tự nhiên n"))
# for i in range(0, n-1):
#     r1=range(0, n-1)
#     print(*r1)

# n=int(input("nhập 1 số tự nhiên n"))
# r1=range(0, n-1)
# print(*r1)


