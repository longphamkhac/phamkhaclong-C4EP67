1. 
# may_tinh={"HP": 20, "DELL": 50, "MACBOOK": 12, "ASUS": 30}
# for i in range(100):
#     may_tinh["ALIENWARE"]=5
#     may_tinh["FUJITSU"]=15
#     may_tinh["MACBOOK"]=2
#     may_tinh["DELL"]=60
#     a=input("Nhap thong tin ban muon biet vao day").upper()
#     print(may_tinh[a])
#     may_tinh["TOSHIBA"]=10
#     b=input("Nhap so luong may moi vao day").upper()
#     may_tinh[a]=b
    
gia_maytinh={
    "HP": 600,
    "DELL": 650,
    "MACBOOK": 12000,
    "ASUS": 400,
    "ACER": 350,
    "TOSHIBA": 600,
    "FUJITSU": 900,
    "ALIENWARE": 1000
}
print(gia_maytinh["ASUS"])
a=input("Nhap thong tin may ma ban muon biet").upper()
if a in gia_maytinh:
    print(gia_maytinh[a])
else:
    print("Khong co thong tin cua san pham, ban co muon them thong tin vao khong?")
    b=input("YES or NO")
    if b=="YES":
        new_item=input("Moi ban nhap vao day").upper()
            gia_maytinh[a]=new_item
    if b=="NO":
        print("bye bye")
               

