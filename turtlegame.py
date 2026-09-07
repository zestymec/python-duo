from turtle import Turtle, Screen
import random

is_race_on = False
Screen = Screen()
Screen.setup(width=500, height=400)
decision = Screen.textinput(
    title="Make your decision", prompt="Which trutle will win the race? Enter a code :"
)
colors = ["red","blue","pink","green","purple","orange"]
yaxis = 200
all_turtles = []
for turtle in range(0,6):
    turtle = Turtle(shape="turtle")
    color = random.choice(colors)
    turtle.color(color)
    turtle.penup()
    turtle.goto (x=-250 , y=yaxis)
    yaxis -= 40
    all_turtles.append(turtle)


if decision:
    is_race_on = True
while  is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 100:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == decision:
                print(f"You've won ! The {winning_color} turtle is the winner !")
            else:
                print(f"You've lost ! The {winning_color} turtle is the winner !")
        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)




Screen.exitonclick()
