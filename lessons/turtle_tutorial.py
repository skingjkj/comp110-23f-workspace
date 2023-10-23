from turtle import Turtle, colormode, done
leo: Turtle = Turtle()
colormode(255)

leo.forward(50)
leo.left(30)
leo.right(40)

leo.color("blue")

leo.color(99,204,250)
leo.penup()
leo.goto(45,60)
leo.pendown()

i=0
while i < 3 :
    leo.forward(300)
    leo.left(120)
    i += 1

leo.begin_fill()
# code for shape to be filled
leo.end_fill

leo.speed(50)
leo.hideturtle()

bob: Turtle = Turtle()
bob.color(204,204,250)
bob.penup()
bob.goto(45,60)
bob.pendown()
bob.speed(100)

side_length: int = 300
 
i: int = 0
while (i < 3):
    side_length = side_length * 0.75
    bob.forward(side_length)
    bob.left(121)
    i = i + 1

done()