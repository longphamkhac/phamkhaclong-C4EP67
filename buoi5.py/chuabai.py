teen_code={"vk": "vo", "ck": "chong", "hok": "khong", "hoy": "thooi", "clgt": "cu lac gion tan"}
loop=True
while loop:
    word=input("Nhap tu teencode ban muon tra")
    if word in teen_code:
        print(word, "co nghia la", teen_code[word])
    else:
        ans=input("tu tren khong co trong tu dien, ban co muon bo xung khong?(y/n)").lower()# chu y hoa hay chu y thuong
        if ans=="y":
            new_word=input("moi ban nhap nghia cua tu moi")
            teen_code[word]=new_word
        elif ans=="n":
            print("bye bye")    
            loop=False