import turtle

myTurtle = turtle.Turtle()
drawing_area = turtle.Screen()
drawing_area.bgcolor('green')
drawing_area.setup(width=650, height=650)
myTurtle.goto(0, 0)

# def vonKoch(self,l,n):
#     return [self.forward(l) , self.left(45)]
def koch(a, order):
    if order > 0:
        for t in [60, -120, 60, 0]:
            koch(a/3, order-1)
            myTurtle.left(t)
    else:
        myTurtle.forward(a)
# # Make it fast
# myTurtle._tracer(100)
# myTurtle.hideturtle()
# Three Koch curves
for i in range(3):
    koch(100, -2)
    myTurtle.right(120)


turtle.done()
