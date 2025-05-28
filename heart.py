import turtle

def draw_heart(turtle_obj, size, color):
    turtle_obj.begin_fill()
    turtle_obj.color(color)
    turtle_obj.left(140)
    turtle_obj.forward(size)


    turtle_obj.circle(-size // 2, 200)


    turtle_obj.left(120)
    turtle_obj.circle(-size // 2, 200)


    turtle_obj.forward(size)
    turtle_obj.end_fill()
    turtle_obj.setheading(0)

pen = turtle.Turtle()
def draw_hearts():
    screen = turtle.Screen()
    screen.bgcolor('lightpink')
    pen.speed(3)
    pen.width(3)

    sizes = [250, 200,150, 100, 50]
    colors = ['#E57852', '#E793A2', '#DC87BB', '#E47381', '#E793A2']

    for size, color in zip(sizes, colors) :
        pen.penup()
        pen.goto(0, -size // 2)
        pen.pendown()
        draw_heart (pen, size, color)

draw_hearts()
turtle.done()