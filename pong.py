# Hello lad

import turtle
import random


turtle.colormode(255)

R = random.randint(0,255)
G = random.randint(0,255)
B = random.randint(0,255)
color = (R,G,B)

t=turtle

wn = t.Screen()
wn.title("Pong")
wn.bgcolor(color)
wn.setup(width=800,height=600)
wn.tracer(0)


# Score
score_a = 0
score_b = 0

# Paddle A
paddle_a= t.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-370,0)


# Paddle B
paddle_b= t.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(370,0)

# Ball
ball= t.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 0.2
ball.dy = -0.2


# Pen
pen = t.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write(" \n Player A can use 'W' and 'S' and for Player B Arrow UP and Down. \n ~VIJAY BIRADAR", align="center", font=("Courier",14,"normal"))

# Function

def paddle_a_up():
    y = paddle_a.ycor()
    y+= 20
    paddle_a.sety(y)
    
def paddle_a_down():
    y = paddle_a.ycor()
    y-= 20
    paddle_a.sety(y)
    
def paddle_b_up():
    y = paddle_b.ycor()
    y+= 20
    paddle_b.sety(y)
    
def paddle_b_down():
    y = paddle_b.ycor()
    y-= 20
    paddle_b.sety(y)   
    
    
    
# Keyboard INput

wn.listen()
wn.onkeypress(paddle_a_up,"w")
wn.onkeypress(paddle_a_down,"s")
wn.onkeypress(paddle_b_up,"Up")
wn.onkeypress(paddle_b_down,"Down")



    

# Main game loop
while True:
    wn.update()
    
    
    # Move a ball
    ball.setx(ball.xcor() + ball.dx) 
    ball.sety(ball.ycor() + ball.dy) 
    
    
    # Border checking
    if ball.ycor()>290:
        ball.sety(290)
        ball.dy *= -1
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
    if ball.xcor()>390:
        ball.goto(0,0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {} || Player B: {}".format(score_a, score_b), align="center", font=("Courier",20,"normal"))
        wn.bgcolor(color)
        R = random.randint(1,255)
        G  = random.randint(1,255)
        B = random.randint(1,255)
        color = (R,G,B)
        
        
    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        score_b +=1
        pen.clear()
        pen.write("Player A: {} || Player B: {}".format(score_a, score_b), align="center", font=("Courier",20,"normal"))
        wn.bgcolor(color)
        R = random.randint(1,255)
        G  = random.randint(1,255)
        B = random.randint(1,255)
        color = (R,G,B)
        
        
        
        
    # Collision
    if (ball.xcor()  > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
        
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
    
