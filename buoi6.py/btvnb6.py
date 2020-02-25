# bai 1:
def hello():
    print("Hello world")
hello()
hello()
hello()

# bai 2:
def add(a, b):
    print(a+b)
add(2, 1)

# bai 9:
def get_even_number(l=[]):
    l=[1,4,5,6,3,7]
    Value=[]
    for i in l:
        if i%2==0:
            Value.append(i)
    return Value
print(get_even_number())    

# bai 10:
def get_even_list(l=()):
    Value=[]
    l=set([1, 2, 5, -10, 9, 6])
    for i in l:
        if i%2==0:
            Value.append(i)
    return Value
print(get_even_list())


# bai 3:
from turtle import *
def draw_square(length, square_color):
    shape("turtle")
    color(square_color)
    for i in range(4):
        forward(length)
        left(90)
    mainloop()
draw_square(200, "red")

# bai 4:
from turtle import *
def draw_star(x, y, length, switch):
    penup()
    setx(x)
    sety(y)
    pendown()
    for i in ["red","blue", "orange", "yellow", "purple"]:
        color(i)
        forward(length)
        left(switch)
    mainloop()

draw_star(100, 100, 200, 144)

# bai 5:
def draw_star(x,y,length):
    penup()
    forward(x)
    left(90)
    forward(y)
    right(90)
    pendown()
    for i in range(5):
        right(144)
        forward(int(length))


# bai 6:
speed(0)
color('blue')
for i in range(100):
    import random
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    length = random.randint(3,10)
    draw_star(x,y,length)

# bai 7:
def remove_dollar_sign(s):
    s = s.replace('$','')
    print(s)
    return(s)

# bai 8:
string_with_no_dollars = remove_dollar_sign("$80% percent of $life is showing up")
if string_with_no_dollars == "80% percent of life is showing up":
    print("Your function is correct")
else:
    print("Oops, there's a bug")

# bai 11:
def is_inside(point,regtangle):
    if point[0] > regtangle[0] and point[1] > regtangle[1]:
        if regtangle[2] > (point[0]-regtangle[0]) and regtangle [3] > (point[1]-regtangle[1]):
            result = True
        else:
            result = False
    else:
        result = False
    print(result)
    return(result, point, regtangle)

# bai 12:
inside = bool(is_inside([200,120],[140,60,100,200]))
if inside == True:
    print("Your function is correct")
else:
    print("Bugs detected")
is_inside([200,120],[140,60,100,200])



        












