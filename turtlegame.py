from turtle import Turtle, Screen
import random


def build_race_track(screen):
    finish_line = Turtle()
    finish_line.hideturtle()
    finish_line.penup()
    finish_line.goto(220, -140)
    finish_line.setheading(90)
    finish_line.pendown()
    finish_line.forward(280)

    start_line = Turtle()
    start_line.hideturtle()
    start_line.penup()
    start_line.goto(-220, -140)
    start_line.setheading(90)
    start_line.pendown()
    start_line.forward(280)

    screen.update()


def create_turtles():
    colors = ["red", "blue", "pink", "green", "purple", "orange"]
    turtles = []
    start_x = -210
    y_positions = [-120, -80, -40, 0, 40, 80]

    for color, y in zip(colors, y_positions):
        racer = Turtle(shape="turtle")
        racer.color(color)
        racer.penup()
        racer.goto(start_x, y)
        racer.speed("normal")
        turtles.append(racer)

    return turtles


screen = Screen()
screen.setup(width=600, height=400)
screen.bgcolor("lightgray")
screen.title("Turtle Race")

build_race_track(screen)

bet = screen.textinput(
    title="Make your choice",
    prompt="Which turtle color will win the race? Type a color: "
)

if bet is None:
    print("You cancelled the race.")
    screen.bye()
else:
    bet = bet.lower().strip()
    turtles = create_turtles()
    race_on = True

    while race_on:
        for racer in turtles:
            racer.forward(random.randint(0, 10))
            if racer.xcor() >= 210:
                winner = racer.pencolor()
                race_on = False

                if winner == bet:
                    print(f"You won! The {winner} turtle is the winner!")
                else:
                    print(f"You lost! The {winner} turtle is the winner!")
                break

    screen.exitonclick()
