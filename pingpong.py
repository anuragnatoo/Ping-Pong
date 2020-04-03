# -*- coding: utf-8 -*-
"""
Created on Thu Apr 3 2020

@author: Anurag Natoo
"""
import turtle
score_1=0
score_2=0
wind=turtle.Screen()
wind.title("Pong Game")
wind.bgcolor("black")
wind.setup(width=800,height=600)
wind.tracer(0) #Turns animation off
# tracer 0 also turns off the screen updates

# Paddles- Player 1 and Player 2
paddle_left=turtle.Turtle()
paddle_left.speed(0)    # Speed of animation-0
paddle_left.shape("square")
paddle_left.color("red")
paddle_left.shapesize(stretch_wid=5,stretch_len=1)
paddle_left.penup()
paddle_left.goto(-350,0)

paddle_right=turtle.Turtle()
paddle_right.speed(0)    # Speed of animation-0
paddle_right.shape("square")
paddle_right.color("red")
paddle_right.shapesize(stretch_wid=5,stretch_len=1)
paddle_right.penup()
paddle_right.goto(350,0)

# Ball
ball=turtle.Turtle()
ball.speed(0)    # Speed of animation-0
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)
# dx-- deltax change in xcor of ball
ball.dx=0.075
ball.dy=0.075

#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player 1 : "+ str(score_1) +"   Player 2 : "+ str(score_2),align="center",font=("Verdana",24,"normal"))



def paddle_left_up():
    posy=paddle_left.ycor()
    if posy<230:
        posy=posy+20
    paddle_left.sety(posy)

def paddle_left_down():
    posy=paddle_left.ycor()
    if posy>-230:
        posy=posy-20
    paddle_left.sety(posy)

def paddle_right_up():
    posy=paddle_right.ycor()
    if posy<230:
        posy=posy+20
    paddle_right.sety(posy)

def paddle_right_down():
    posy=paddle_right.ycor()
    if posy>-230:
        posy=posy-20
    paddle_right.sety(posy)

#Keyboard bindings
wind.listen()
wind.onkeypress(paddle_left_up,"w")
wind.onkeypress(paddle_left_down,"s")
wind.onkeypress(paddle_right_up,"Up")
wind.onkeypress(paddle_right_down,"Down")


# Main game loop
while True:
    wind.update()

    #Move the ball
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)
    if ball.ycor()>290:
        ball.sety(290)
        ball.dy*=-1
    if ball.ycor()<-290:
        ball.sety(-290)
        ball.dy*=-1
    if ball.xcor()>390:
        score_1 += 1
        #ball.setx(390)
        ball.goto(0,0)
        ball.dx*=-1
        pen.clear()
        pen.write("Player 1 : "+ str(score_1) +"  Player 2 : "+ str(score_2),align="center",font=("Verdana",24,"normal"))
    if ball.xcor()<-390:
        score_2+=1
        #ball.setx(-390)
        ball.goto(0,0)
        ball.dx*=-1
        pen.clear()
        pen.write("Player 1 : "+ str(score_1) +"  Player 2 : "+ str(score_2),align="center",font=("Verdana",24,"normal"))
    # Paddle and ball collision
    if (ball.xcor()>340 and ball.xcor()<350) and (ball.ycor()<paddle_right.ycor()+40 and ball.ycor()>paddle_right.ycor()-40):
        ball.setx(340)
        ball.dx*=-1
    if (ball.xcor()<-340 and ball.xcor()>-350) and (ball.ycor()<paddle_left.ycor()+40 and ball.ycor()>paddle_left.ycor()-40):
        ball.setx(-340)
        ball.dx*=-1
