mon_an=["trung", "com", "ca", "ga", "lon"]
new_item=input("nhap mon ban muon them vao day")
mon_an.append(new_item)
mon_an.pop(5)
mon_an.append("thit meo")
# i=mon_an[1]
# mon_an[1]=mon_an[2]
# mon_an[2]=i
# i=input("nhap vao mon ma ban muon doi")
# mon_an[0]=i
# new_item=input("nhap mon ban muon them vao day")
# mon_an.append(new_item)
for i in range(len(mon_an)):
    print(i+1, mon_an[i])



