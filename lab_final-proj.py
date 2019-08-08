import turtle
import random
import time
turtle.bgpic("final_background.gif")
SIZE_X=600
SIZE_Y=500
turtle.setup(SIZE_X,SIZE_Y)
turtle.hideturtle()
bowl = turtle.clone()
turtle.write("CATCHER IN THE RYEN", align = "center", font = ("arial", 35, "normal"))
time.sleep(3)
turtle.clear()
turtle.write("How to play?" ,align = "center",font = ("airal", 25, "normal"))
time.sleep(1.5)
turtle.clear()
turtle.write("Catch the blue waterdrops and avoid the black ones", align = "center", font = ("arial",17, "normal"))
time.sleep(3)
turtle.clear()
turtle.write("and be careful from the edges", align = "center", font = ("arial", 17, "normal"))
time.sleep(3)
turtle.clear()
turtle.write("GOOD LUCK!", align = "center", font = ("arial", 30, "normal"))
time.sleep(1.5)
turtle.clear()

turtle.clear()
y_cord = 250

turtle.listen()

turtle.tracer(1,0)

SQ=10

RIGHT_EDGE=280
LEFT_EDGE=-280


turtle.write("0",align = "center", font = 20)
bowl=turtle.Turtle()
bowl.penup()
bowl.goto(0,-230)

turtle.register_shape('final_bowl.gif')
turtle.register_shape("final_drop.gif")
turtle.register_shape('final_poison.gif')

bowl.shape('final_bowl.gif')



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
list = []
for i in range(14, 200):
    list.append(i/2)

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
        turtle.clear()
        hide()
        turtle.write("Your bowl just broke. All the water you collected have gone to waste!", align = "center", font = ("arial", 13, "normal"))
        quit()
    elif new_x_pos<=LEFT_EDGE:
        turtle.clear()
        hide()
        turtle.write("Your bowl just broke. All the water you collected have gone to waste!", align = "center", font = ("arial", 13, "normal"))
        quit()
        
rain = turtle.clone()

    
def move_rain():
    rain.goto(rain.xcor(),rain.ycor()-list[0])
    if (rain.pos()[0] - bowl.pos()[0] < 12 and rain.pos()[0] - bowl.pos()[0] > -12) and (rain.pos()[1] - bowl.pos()[1] < 12 and rain.pos()[1] - bowl.pos()[1] > -12):
        rain.hideturtle()
        x_cord = random.randint(LEFT_EDGE, RIGHT_EDGE)
        y_cord = 250
        rain.goto(x_cord, y_cord)
        rain.showturtle()
        list.pop(0)
        turtle.clear()
        turtle.write(int((list[0]-7)*2), align = "center", font = 20)
        
    if rain.ycor()<-250:
        turtle.clear()
        hide()
        turtle.write("You just saved the lives of " + str(int((list[0]-7)*2)) + " of the 2300 people that die every day due to lack of water!", align = "center", font = ("arial", 11, "normal"))
        quit()

    turtle.ontimer(move_rain,50)

    
    
rain.shape("final_drop.gif")
rain.hideturtle()
x_cord = random.randint(LEFT_EDGE+20, RIGHT_EDGE-20)
rain.penup()
rain.goto(x_cord, y_cord)
rain.showturtle()
move_rain()

y_poi = 250
def hide():
    rain.hideturtle()
    bowl.hideturtle()
    poison.hideturtle()

poison = turtle.Turtle()

def move_poison():
    peoper = "people"
    poison.goto(poison.xcor(),poison.ycor()-10)
    if (poison.pos()[0] - bowl.pos()[0] < 12 and poison.pos()[0] - bowl.pos()[0] > -12) and (poison.pos()[1] - bowl.pos()[1] < 12 and poison.pos()[1] - bowl.pos()[1] > -12):
        turtle.clear()
        hide()
        if int((list[0]-7)*2) == 1:
            peoper = "person"
        turtle.write(str(int((list[0]-7)*2))+ " " + peoper + " just died due to water poisoning!", align = "center", font = ("arial", 13, "normal"))
        quit()
    turtle.ontimer(move_poison,50)
    if poison.ycor() < -250:
        y_cord = 250
        x_poi = random.randint(LEFT_EDGE+20, RIGHT_EDGE-20)
        poison.hideturtle()

        poison.goto(x_poi, y_poi)
        poison.showturtle()
    
poison.shape("final_poison.gif")
poison.hideturtle()
x_cord = random.randint(LEFT_EDGE+20, RIGHT_EDGE-20)
poison.penup()
poison.goto(x_cord, y_cord)
poison.showturtle()
move_poison()

       
turtle.mainloop()
