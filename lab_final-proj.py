import turtle
import random
turtle.hideturtle()
bowl = turtle.clone()


speed=5
y_cord = 250

turtle.listen()

turtle.tracer(1,0)
SIZE_X=800
SIZE_Y=500
turtle.setup(SIZE_X,SIZE_Y)
SQ=4

RIGHT_EDGE=400
LEFT_EDGE=-400



bowl=turtle.Turtle()
bowl.penup()
bowl.goto(0,-250)

turtle.register_shape('bowl.gif')

bowl.shape('bowl.gif')



turtle.hideturtle()

def right ():
    bowl.direction='Right'

    move()

def left ():
    bowl.direction='Left'
    move()




bowl.direction='Left'
turtle.onkeypress(right,'Right')
turtle.onkeypress(left,'Left')
turtle.listen()    


def move ():
    my_pos=bowl.pos()
    xpos=my_pos[0]
    ypos=my_pos[1]
    if bowl.direction=='Left':
        bowl.goto(xpos-SQ,ypos)
    elif bowl.direction=='Right':
        bowl.goto(xpos+SQ,ypos)

    new_pos=bowl.pos()
    new_x_pos=new_pos[0]

    if new_x_pos>=RIGHT_EDGE:
        print('You hit the right edge !Game over!')
        quit()
    elif new_x_pos<=LEFT_EDGE:
        print('You hit the left edge! Game over !')
        quit()
        
rain = turtle.clone()

def make_rain():
    turtle.register_shape("rain.gif")
    rain.shape("rain.gif")
    rain.hideturtle()
    x_cord = random.randint(-400, 400)
    rain.penup()
    rain.goto(x_cord, y_cord)
    rain.showturtle()
    move_rain()
def move_rain():
    rain.goto(rain.xcor(),rain.ycor()-speed)
    print(rain.pos())
    print(bowl.pos())
    if (rain.pos()[0] - bowl.pos()[0] < 12 and rain.pos()[0] - bowl.pos()[0] > -12) and (rain.pos()[1] - bowl.pos()[1] < 12 and rain.pos()[1] - bowl.pos()[1] > -12):
        rain.hideturtle()
        x_cord = random.randint(-400, 400)
        y_cord = 250
        rain.goto(x_cord, y_cord)
        rain.showturtle
    if rain.ycor()<-250:
        quit()
    turtle.ontimer(move_rain,)

make_rain()    

  	 
   	 
   	 
   	 
turtle.mainloop()
