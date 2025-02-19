import turtle, math


def draw_partial_ellipse(pen, a, b, c, d, start_angle=0, end_angle=360, clockwise=True):
    """
    画椭圆
    参数:
    pen: 画笔
    a, b: 椭圆的水平、垂直方向的宽度的一半
    c, d: 椭圆的圆心x, y坐标
    start_angle, end_angle: 起始、结束角度
    clockwise: 是否顺时针绘制
    """
    pen.speed(0)
    pen.penup()

    if clockwise:
        if start_angle < end_angle:
            end_angle, start_angle = start_angle, end_angle
    else:
        if start_angle > end_angle:
            end_angle, start_angle = start_angle, end_angle

    start_radian = math.radians(start_angle)  
    x_start = a * math.cos(start_radian)
    y_start = b * math.sin(start_radian)
    pen.goto(x_start+c, y_start+d)  
    pen.pendown()  

    if clockwise:
        for theta in range(start_angle, end_angle - 1, -1):
            radian = math.radians(theta) 
            x = a * math.cos(radian)
            y = b * math.sin(radian)
            pen.goto(x+c, y+d)
    else:
        # 逆时针方向
        for theta in range(start_angle, end_angle + 1, 1):
            radian = math.radians(theta)
            x = a * math.cos(radian)
            y = b * math.sin(radian)
            pen.goto(x+c, y+d)


def draw_python(pen, direction):
    pen.speed(0)
    pen.penup()
    if direction == -1:
        pen.lt(180)
    d = 0 if direction == 1 else 180
    pen.goto(-25*direction, -15*direction)
    pen.pendown()
    pen.speed(1)
    pen.fd(70)
    pen.speed(0)
    pen.lt(90)
    draw_partial_ellipse(pen, 50, 50, pen.position()[0], pen.position()[1]+50*direction, -90+d, 0+d, False)
    pen.speed(1)
    pen.fd(20)
    draw_partial_ellipse(pen, 40, 60, pen.position()[0], pen.position()[1]-60*direction, 90+d, -90+d, True)
    pen.speed(0)
    pen.lt(90)
    pen.speed(1)
    pen.fd(100)
    draw_partial_ellipse(pen, 15, 15, pen.position()[0], pen.position()[1]-15*direction, 90+d, 270+d, False)
    pen.lt(180)
    pen.speed(1)
    pen.fd(60)
    pen.speed(0)
    pen.rt(90)
    pen.speed(1)
    pen.fd(20)
    draw_partial_ellipse(pen, 20, 20, pen.position()[0]-20*direction, pen.position()[1], 0+d, 360+d, True)
    draw_partial_ellipse(pen, 60, 30, pen.position()[0]-60*direction, pen.position()[1], 180+d, 360+d, True)
    pen.lt(180)
    pen.speed(1)
    pen.fd(60)
    draw_partial_ellipse(pen, 40, 40, pen.position()[0]+40*direction, pen.position()[1], 90+d, 180+d, True)
    pen.hideturtle()


def draw_text(pen):
    pen.speed(0)
    pen.penup()
    pen.goto(0, 250)
    pen.write(
        "2025",
        align="center",
        font=("Microsoft Yahei ul", 50, "bold"),
    )
    pen.goto(0, -250)
    pen.write(
        "祝大家蛇年大吉，万事如意",
        align="center",
        font=("Microsoft Yahei ul", 36, "bold"),
    )
    pen.goto(0, -300)
    pen.write(
        "「巳巳如意·生生不息」",
        align="center",
        font=("Microsoft Yahei ul", 36, "bold"),
    )
    pen.hideturtle()


if __name__ == "__main__":
    screen = turtle.Screen()
    screen.title("2025蛇年快乐")
    screen.bgcolor("darkred")

    a = turtle.Turtle()
    a.pencolor("yellow")
    a.pensize(20)
    draw_python(a, 1)

    b = turtle.Turtle()
    b.pencolor("yellow")
    b.pensize(20)
    draw_python(b, -1)

    c = turtle.Turtle()
    c.pencolor("yellow")
    draw_text(c)

    screen.mainloop()
