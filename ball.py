from turtle import *
										
class Ball(Turtle):
	def __init__(self,x,y,dx,dy,r,color):
		Turtle.__init__(self)																																																																																																																																																												
		self.dx=dx
		self.dy=dy
		self.r=r
		self.pu()
		self.goto(x,y)
		self.shape("circle")
		self.shapesize(r*r)
		self.color(color)
		print(self.xcor())
		print(self.ycor())
	
	def move(self,screen_width,screen_height):
		current_x = self.xcor()
		new_x = current_x + self.dx

		current_y = self.ycor()
		new_y = current_y + self.dy

		right_side_ball = new_x + self.r
		left_side_ball = new_x - self.r
		top_side_ball = new_y + self.r
		bottom_side_ball = new_y - self.r

		self.goto(new_x,new_y)

		if (current_x >= screen_width/2):
			self.dx = -self.dx
		elif(current_x <= (-screen_width/2)):
			self.dx = -self.dx

		if(current_y >= screen_height/2):
			self.dy = -self.dy
		elif(current_y <= (-screen_height/2)):
			self.dy = -self.dy



