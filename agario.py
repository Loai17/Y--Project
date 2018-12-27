import turtle, time, random
from turtle import *
from ball import Ball
turtle.colormode(255)
# qturtle.speed(100)

RUNNING=True
SLEEP=0.0077
SCREEN_WIDTH=turtle.getcanvas().winfo_width()/2
SCREEN_HEIGHT=turtle.getcanvas().winfo_height()/2

my_ball=Ball(0,0,5,5,20,"green")

NUMBER_OF_BALLS = 5
MINIMUM_BALL_RADIUS = 10
MAXIMUM_BALL_RADIUS = 100
MINIMUM_BALL_DX = -5
MAXIMUM_BALL_DX = 5
MINIMUM_BALL_DY = -5
MAXIMUM_BALL_DY = 5

BALLS = []

for ball in range(NUMBER_OF_BALLS):
	x = random.randint((-SCREEN_WIDTH+MAXIMUM_BALL_RADIUS),(SCREEN_WIDTH-MAXIMUM_BALL_RADIUS))
	y = random.randint((-SCREEN_HEIGHT+MAXIMUM_BALL_RADIUS),(SCREEN_HEIGHT-MAXIMUM_BALL_RADIUS))
	dx = random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
	dy = random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
	r = random.randint(MINIMUM_BALL_RADIUS,MAXIMUM_BALL_RADIUS)
	color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
	new_ball = Ball(x,y,dx,dy,r,color)
	BALLS.append(new_ball)


def move_all_balls():
	for ball in BALLS:
		ball.move(SCREEN_WIDTH,SCREEN_HEIGHT)

def collide(ball1,ball2):
	if ball1==ball2:
		return False

	#Calculate distance between 2 balls
	#Continue part 2
	

def check_all_balls_collision():
	for ball1 in BALLS:
		for ball2 in BALLS:
			if(collide(ball1,ball2)):
				r1=ball1.r
				r2=ball2.r

move_all_balls()
turtle.mainloop()