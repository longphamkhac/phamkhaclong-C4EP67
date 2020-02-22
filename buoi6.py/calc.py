def calc(a,b,operator):
    if operator == "+":
        result=a+b
    elif operator == "-":
        result=a-b
    elif operator == "*":
        result=a*b
    elif operator == "/":
        result=a/b
    else:
        print("May dua tao a?")
    return result
if __name__=="__main__":
    a=calc(5,3,"+")
    print(a)







