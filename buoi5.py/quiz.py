quizzes=[
    {
        "question": "con nhen co may chan",
        "choices":["3 chan", "5 chan", "8 chan", "6 chan"],
        "right_awnser":3
    },

    {   "question": "con cho co may chan",
        "choices":["2 chan", "5 chan", "8 chan", "6 chan"],
        "right_awnser":0
    },
    {
        "question": "con bo co may chan",
        "choices":["3 chan", "5 chan", "8 chan", "4 chan"],
        "right_awnser":3
    }
]
for quiz in quizzes:
    print(quiz["question"])
    choices=quiz["choices"]
    for i in range(len(choices)):
        print(str(i)+"."+choices[i])# chuyen i thanh dang chu
    user_choice=int(input("Nhap dap an cua ban"))
    if user_choice==quiz["right_awnser"]:
        print("Ban gioi vl")
    else:
        print("Ban ga qua")
    

    # print(i["question2"])
    # choices2=i["choices2"]
    # for i in range(len(choices2)):
    #     print(str(i)+"."+choices2[i])# chuyen i thanh dang chu
    # user_choice=int(input("Nhap dap an cua ban"))
    # if user_choice==i["right_awnser"]:
    #     print("Ban gioi vl")
    # else:
    #     print("Ban ga qua")