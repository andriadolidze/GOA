from turtle import*

width(3)
speed(30)

#ვიწყებ კვადრატის შენებას
begin_fill()
color("grey")
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
end_fill()
left(90)
forward(70)
#დავასრულე კვადრატის შენება

#კარის შენებას ვიწყებ
begin_fill()
color("yellow")
left(90)
forward(100)
right(90)
forward(60)
right(90)
forward(100)
end_fill()
#დავასრულე კარის შენება

penup()
goto(200,200)
pendown()

#ვიწყებ სახურავის შენებას
begin_fill()
color("brown")
right(150)
forward(200)
left(120)
forward(200)
end_fill()


#ვიწყებ ფანჯრების გაკეთებას
penup()
goto(20,120)
pendown()
begin_fill()
color("blue")
left(120)
forward(40)
left(90)
forward(50)
left(90)
forward(40)
left(90)
forward(50)
end_fill()

penup()
goto(180,170)
pendown()
begin_fill()
color("blue")
right(90)
forward(40)
left(90)
forward(50)
left(90)
forward(40)
left(90)
forward(50)
end_fill()
#მოვრჩი ფანჯრების გაკეთებას


#ვიწყებ კვადრატის შენებას
penup()
goto(-50,0)
pendown()

begin_fill()
color("red")
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(180)
forward(70)
right(90)
forward(100)
left(90)
forward(60)
left(90)
forward(100)
end_fill()

penup()
goto(250,0)
pendown()



begin_fill()
color("blue")
left(180)
forward(200)
right(90)
forward(200)
right(90)
forward(200)
right(90)
forward(200)
right(180)
forward(70)
end_fill()

begin_fill()
color("brown")
left(90)
forward(100)
right(90)
forward(60)
right(90)
forward(100)
end_fill()

penup()
goto(450,200)
pendown()

begin_fill()
color("orange")
right(150)
forward(200)
left(120)
forward(200)
end_fill()

penup()
goto(260,120)
pendown()
#აქ დავუწყე ფანჯარა
begin_fill()
color("sky blue")
left(120)
forward(40)
left(90)
forward(50)
left(90)
forward(40)
left(90)
forward(50)
end_fill()

penup()
goto(400,170)
pendown()
begin_fill()
color("sky blue")
forward(50)
left(90)
forward(40)
left(90)
forward(50)
left(90)
forward(40)
end_fill()

penup()
goto(-50,200)
pendown()

begin_fill()
color("green")
right(60)
forward(200)
left(120)
forward(200)
end_fill()

penup()
goto(-240,170)
pendown()

begin_fill()
color('dark blue')
left(120)
forward(40)
right(90)
forward(50)
right(90)
forward(40)
right(90)
forward(50)
end_fill()

penup()
goto(-100,170)
pendown()

begin_fill()
color("dark blue")
right(90)
forward(40)
right(90)
forward(50)
right(90)
forward(40)
right(90)
forward(50)
end_fill()

penup()
goto(290,320)
pendown()

color('yellow')
begin_fill()
circle(50)
end_fill()

penup()
goto(-500,-250)
pendown()
begin_fill()
color("brown")

forward(320)
left(180)
forward(320)
left(90)
forward(55)
left(90)
forward(320)
left(90)
forward(55)
end_fill()
begin_fill()
color("dark green")
penup()
goto(-470,200)
pendown()
circle(100)
end_fill()











































exitonclick()
