import turtle
import random
import time
import os
screen = turtle.Screen()
screen.bgcolor('black')
screen.setup(600,600)
screen.tracer(False)

screen.register_shape("strawberry.gif")

score = 0
if os.path.exists("snake_score.txt"):
    f = open("snake_score.txt", "r")
    highscore = int(f.read())
else:
    highscore = 0
 


def create_turtle(s, c):
    my_turtle = turtle.Turtle()
    my_turtle.shape(s)
    my_turtle.color(c)
    my_turtle.penup()
    return my_turtle

def change_position():
    x = random.randint(-270, 270)
    y = random.randint(-270, 230)
    snake_food.goto(x,y)
def move():
    if snake_head.direction == "up":
        ypos = snake_head.ycor()
        ypos += 20
        snake_head.sety(ypos)

    if snake_head.direction == "down":
        ypos = snake_head.ycor()
        ypos -= 20
        snake_head.sety(ypos)

    if snake_head.direction == "right":
        xpos = snake_head.xcor()
        xpos += 20
        snake_head.setx(xpos)
    if snake_head.direction == "left":
        xpos = snake_head.xcor()
        xpos -= 20
        snake_head.setx(xpos)   


def go_up():
    snake_head.direction = "up" 
        
def go_down():
    snake_head.direction = "down"

def go_right():
    snake_head.direction = "right"

def go_left():
    snake_head.direction = "left"



snake_head = create_turtle("square", "darkgreen")
snake_head.direction = ""
snake_food = create_turtle("circle", "red")
change_position()

scoreboard = create_turtle("square", "white")
scoreboard.goto(0,260)
scoreboard.ht()
scoreboard.color("cyan")


screen.listen()
screen.onkeypress(go_up,"Up")
screen.onkeypress(go_down,"Down")
screen.onkeypress(go_right,"Right")
screen.onkeypress(go_left,"Left")


def please_close_the_window():
    f = open("snake_score.txt", "w")
    f.write(str(highscore))
    f.close()
    global running
    running = False

root_window = screen._root
root_window.protocol("WM_DELETE_WINDOW", please_close_the_window)

all_tails = []
running = True
while running:
    screen.update()
    scoreboard.clear()
    scoreboard.write(f"Score: {score}, HighScore:{highscore}", font=("arial", 26,"bold"), align="center")

    if snake_head.distance(snake_food) < 20:
        change_position()
        score += 1
        if score > highscore:
            highscore = score
        new_tail = create_turtle("square", "darkgreen")
        all_tails.append(new_tail)



    for i in range(len(all_tails)-1, 0, -1):
        x = all_tails[i - 1].xcor()
        y = all_tails[i - 1].ycor()
        all_tails[i].goto(x,y)
    if len(all_tails) > 0:
        all_tails[0].goto(snake_head.xcor(), snake_head.ycor())

    if snake_head.xcor() > 290 or snake_head.xcor() < -290:
        snake_head.setx(-1 * snake_head.xcor())
    if snake_head.ycor() < -290:
        snake_head.sety(240)
    if snake_head.ycor() > 240:
        snake_head.sety(-290)
    
    move()
    time.sleep(0.2)


# TODO اضافه کردن highscore