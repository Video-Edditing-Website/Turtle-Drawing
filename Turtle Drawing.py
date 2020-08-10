import turtle as t
from turtle import Screen

t.speed(0)


def on_screen_click(mousex, mousey):
    print("I have been teleported to ({},{})".format(mousex, mousey))
    t.ht()
    t.goto(mousex, mousey)
    global cleared
    cleared = False
    t.st()


cleared = True


def dragging(x, y):
    t.ondrag(None)
    t.setheading(t.towards(x, y))
    t.goto(x, y)
    t.ondrag(dragging)
    global cleared
    cleared = False


screen = Screen()

t.ondrag(dragging)


def many_circles():
    for i in range(50, 155, 5):
        the(i)


def flower():
    for i in range(8):
        many_circles()
        left()
    t.penup()


def the(radius):
    t.speed(0)
    t.circle(radius)
    global cleared
    cleared = False


def circle():
    radius = screen.textinput("A question", "What should the radius in pixels be? Please type it.")
    radius = int(radius)
    if radius is None:
        print("Canceled")
    else:
        t.speed(0)
        t.circle(radius)
        print("I have made a circle with the radius of {} pixels".format(radius))
        global cleared
        cleared = False
        t.listen()


def left():
    t.left(45)


def right():
    t.right(45)


def forward():
    global cleared
    t.forward(10)
    cleared = False


def backward():
    global cleared
    t.backward(10)
    cleared = False


def start_drawing():
    t.pendown()


def stop_drawing():
    t.penup()


def change_color_b():
    if t.pencolor() == "sky blue":
        print("You can't change a turtle's color to the color they already are!")
    else:
        answer = screen.textinput("Conformation", "Are you sure you want to change the color to blue? Yes or no?")
        answer = str(answer)
        answer = answer.strip().lower()
        if answer is None:
            print("Canceled")
        else:
            if (answer == "yes") or (answer == "Yes"):
                t.listen()
                print("Me back to blue")
                t.pencolor("sky blue")
                t.pensize(1)
            else:
                t.listen()
                print("Canceled")


def change_color_r():
    if t.pencolor() == "red":
        print("You can't change a turtle's color to the color they already are!")
    else:
        answer = screen.textinput("Conformation", "Are you sure you want to change the color to red? Yes or no?")
        answer = str(answer)
        answer = answer.strip().lower()
        if answer is None:
            print("Canceled")
        else:
            if (answer == "yes") or (answer == "Yes"):
                t.listen()
                print("Me red!")
                t.pencolor("red")
                t.pensize(1)
            else:
                t.listen()
                print("Canceled")


def change_color_o():
    if t.pencolor() == "orange":
        print("You can't change a turtle's color to the color they already are!")
    else:
        answer = screen.textinput("Conformation", "Are you sure you want to change the color to orange? Yes or no?")
        answer = str(answer)
        answer = answer.strip().lower()
        if answer is None:
            print("Canceled")
        else:
            if (answer == "yes") or (answer == "Yes"):
                t.listen()
                print("Me orange!")
                t.pencolor("orange")
                t.pensize(1)
            else:
                t.listen()
                print("Canceled")


def change_color_B():
    if t.pencolor() == "black":
        print("You can't change a turtle's color to the color they already are!")
    else:
        answer = screen.textinput("Conformation", "Are you sure you want to change the color to black? Yes or no?")
        answer = str(answer)
        answer = answer.strip().lower()
        if answer is None:
            print("Canceled")
        else:
            if (answer == "yes") or (answer == "Yes"):
                t.listen()
                print("Me Black!")
                t.pencolor("black")
                t.pensize(1)
            else:
                t.listen()
                print("Canceled")


def eraser():
    if t.pencolor() == "white":
        print("I am already in eraser mode.")
    else:
        answer = screen.textinput("Conformation", "Are you sure you want to change to eraser mode? Yes or no?")
        answer = str(answer)
        answer = answer.strip().lower()
        if answer is None:
            if (answer == "yes") or (answer == "Yes"):
                t.listen()
                print("Me an eraser!")
                t.pencolor("white")
                t.pensize(50)
            else:
                t.listen()
                print("Canceled")


def clear():
    global cleared
    if cleared:
        print("The screen is already cleared")
    else:
        answer = screen.textinput("Conformation", "Are you sure you want to clear the screen? Yes or no?")
        answer = str(answer)
        answer = answer.strip().lower()
        if answer is None:
            print("Canceled")
        else:
            if (answer == "yes") or (answer == "Yes"):
                print("Cleared")
                t.clear()
                cleared = True
                t.listen()
            else:
                print("Canceled")
                t.listen()


def text():
    color1 = t.pencolor()
    answer = screen.textinput("What text?", "What text do you want written on screen?")
    if answer is None:
        print("Canceled")
    else:
        font = screen.textinput("What Font?", "What font do you want?")
        size = screen.textinput("What size?", "What size do you want it to be?")
        size = int(size)
        color2 = screen.textinput("What color?", "What color do you want it to be?")
        t.pencolor(color2)
        t.write(answer, font=(font, size, "normal"))
        t.pencolor(color1)
        global cleared
        cleared = False
        t.listen()


def plot():
    color = t.pencolor()
    t.penup()
    XY.make_xy(-500, 500, 50, 'black')
    global cleared
    cleared = False
    t.penup()
    t.goto(0, 0)
    t.pencolor(color)
    t.pendown()


def rectangle1(x, y, w, h, color1):
    color2 = t.pencolor()
    t.pencolor(color1)
    t.up()
    t.goto(x, y)
    t.down()
    t.goto(x + w, y)
    t.goto(x + w, h + y)
    t.goto(x, h + y)
    t.goto(x, y)
    t.pencolor(color2)


def rectange():
    rec1 = screen.textinput("Coordinates", "What should the x coordinate be for one corner?")
    rec1 = int(rec1)
    if rec1 is None:
        print("Canceled")
    else:
        rec2 = screen.textinput("Coordinates", "What should the y coordinate be for the same corner?")
        rec2 = int(rec2)
        rec3 = screen.textinput("Coordinates", "What should the width be?")
        rec3 = int(rec3)
        rec4 = screen.textinput("Coordinates", "What should the height be?")
        rec4 = int(rec4)
        rec5 = screen.textinput("Color", "What the color be?")
        rec5 = str(rec5)
        rectangle1(x=rec1, y=rec2, w=rec3, h=rec4, color1=rec5)
        t.listen()


def center():
    if t.position() == (0, 0):
        print("I'm already at the center!")
    else:
        t.goto(0, 0)
        print("Centered!")
        global cleared
        cleared = False


def helper():
    help_string = """How to use turtle, capitalization matters:
    Arrow keys to move.
    b for color blue.
    r for color red.
    o for color orange.")
    B for color black.")
    y for pen up.")
    u for pen down.")
    c for clear.")
    e for eraser.
    t for text.
    x for a plot.
    p for a rectangle.
    C to go to center.
    f for a spiral.
    d for a circle.
    m for many circles in the shape of a shell.
    Click any place on the screen for turtle to teleport there.
    You can also drag turtle.
    If you need this help again, press h.
    After reading more stuff will come out in the output window after you press keys."""
    print(help_string)
t.pencolor("sky blue")
t.shape('turtle')
helper()
t.onkey(left, "Left")
t.onkey(right, "Right")
t.onkeypress(start_drawing, "u")
t.onkeypress(stop_drawing, "y")
t.onkeypress(forward, "Up")
t.onkeypress(backward, "Down")
t.onkeyrelease(change_color_r, "r")
t.onkeyrelease(change_color_b, "b")
t.onkeyrelease(change_color_o, "o")
t.onkeyrelease(change_color_B, "B")
t.onkey(clear, "c")
t.onkey(eraser, "e")
t.onscreenclick(on_screen_click, btn=1)
t.onkey(circle, "d")
t.onkey(many_circles, "m")
t.onkey(text, "t")
t.onkey(plot, "x")
t.onkey(rectange, "p")
t.onkey(center, "C")
t.onkey(flower, "f")
t.onkey(helper, "h")
t.goto(0, 0)
t.listen()
t.Screen().mainloop()
