import turtle
import random

score = 0
lives = 3

wn=turtle.Screen()
wn.title('falling objects')
wn.bgcolor('green')
wn.setup(width=800,height=600)
wn.tracer(0)

player=turtle.Turtle()
player.speed(0)
player.shape('square')
player.color('white')
player.penup()
player.goto(0,-225)
player.direction ='stop'

#create list of good guys
players =[ ]

for _ in range(20):	
	player2=turtle.Turtle()
	player2.speed(0)
	player2.shape('circle')
	player2.color('blue')
	player2.penup()
	player2.goto(-100,250)
	player2.speed = random.randint(2,5)
	players.append(player2)

#create list of good guys
playerss=[ ]

for _ in range(10):	
	player3=turtle.Turtle()
	player3.speed(0)
	player3.shape('circle')
	player3.color('red')
	player3.penup()
	player3.goto(100,250)
	player3.speed = random.randint(2,5)
	playerss.append(player3)

#make pen
pen=turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.shape('square')
pen.color('white')
pen.penup()
pen.goto(0,260)
font=('courier',9,'normal')
pen.write('score : {} lives:{}'.format(score,lives),align='center',font=font)

#functions
def go_left():
	player.direction = 'left'

def go_right():
	player.direction = 'right'

#keyboard binding
wn.listen()
wn.onkeypress(go_left,'Left')
wn.onkeypress(go_right,'Right')

while True:
	wn.update()	
	if player.direction == 'left':
		x = player.xcor()
		x-=3
		player.setx(x)
		
	if player.direction == 'right':
		x = player.xcor()
		x+=3
		player.setx(x)
			
	for player2 in players:
		y=player2.ycor()
		y-=player2.speed
		player2.sety(y)
	
		if y<-300:
			x=random.randint(-380,380)
			y = random.randint(300,400)
			player2.goto(x,y)
		
	#check collision
		if player2.distance(player)<30:
			x=random.randint(-380,380)
			y = random.randint(300,400)
			player2.goto(x,y)
			score += 20
			pen.clear()
			pen.write('score : {} lives:{}'.format(score,lives),align='center',font=font)
		
	for player3 in playerss:
		y=player3.ycor()
		y-=player3.speed
		player3.sety(y)
	
		if y<-300:
			x=random.randint(-380,380)
			y = random.randint(300,400)
			player3.goto(x,y)
		
	#check collision
		if player3.distance(player)<20:
			x=random.randint(-380,380)
			y = random.randint(300,400)
			player3.goto(x,y)
			score -=9
			lives -= 1
			pen.clear()
			pen.write('score : {} lives:{}'.format(score,lives),align='center',font=font)

wn.mainloop()