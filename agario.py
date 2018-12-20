import turtle, time, random
from turtle import *
from ball import Ball

turtle.tracer(0,0) #if there's an error change it to (0,0)

RUNNING=True
SLEEP=0.0077
SCREEN_WIDTH=turtle.getcanvas().winfo_width()/2
SCREEN_HEIGHT=turtle.getcanvas().winfo_height()/2

my_ball=Ball(0,0,1,1,20,"green")

NUMBER_OF_BALLS = 5
MINIMUM_BALL_RADIUS = 10
MAXIMUM_BALL_RADIUS = 100
MINIMUM_BALL_DX = -5
MAXIMUM_BALL_DX = 5
MINIMUM_BALL_DY = -5
MAXIMUM_BALL_DY = 5

BALLS = []

for ball in range(NUMBER_OF_BALLS):
	x = random.randint((-SCREEN_WIDTH/2+MAXIMUM_BALL_RADIUS),(SCREEN_WIDTH/2-MAXIMUM_BALL_RADIUS))
	y = random.randint((-SCREEN_HEIGHT/2+MAXIMUM_BALL_RADIUS),(SCREEN_HEIGHT/2-MAXIMUM_BALL_RADIUS))
	dx = random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
	dy = random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
	r = random.randint(MINIMUM_BALL_RADIUS,MAXIMUM_BALL_RADIUS)
	(random.randint(0,255),random.randint(0,255),random.randint(0,255))
	new_ball = Ball(x,y,dx,dy,r,"black")
	BALLS.append(new_ball)
	new_ball.move(SCREEN_WIDTH,SCREEN_HEIGHT)



turtle.mainloop()