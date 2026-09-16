import turtle
import time
import random

# How lazy our little guy is feeling (smaller number = faster snake)
sluggishness = 0.1

# Let's set up the world for our snake to live in
game_window = turtle.Screen()
game_window.title("The Very Hungry (And Emotional) Snake")
game_window.bgcolor("black")
game_window.setup(width=600, height=600)
game_window.tracer(0) # Turns off screen updates so it doesn't flicker and give us a headache

# Here is our main character, Mr. Snake Head
mr_snake_head = turtle.Turtle()
mr_snake_head.speed(0)
mr_snake_head.shape("square")
mr_snake_head.color("green")
mr_snake_head.penup()
mr_snake_head.goto(0, 0)
mr_snake_head.current_mood = "chilling" # our custom direction variable

# And here is the snack he desperately wants to eat
yummy_snack = turtle.Turtle()
yummy_snack.speed(0)
yummy_snack.shape("circle")
yummy_snack.color("red")
yummy_snack.penup()
yummy_snack.goto(0, 100)

# As he eats, he gets a bigger tummy. We'll store those extra body parts here.
growing_tummy_parts = []

# --- Brain Functions (How the snake thinks about moving) ---

def decide_to_look_up():
    # You can't look up if you're already going down, you'd snap your neck!
    if mr_snake_head.current_mood != "going_down":
        mr_snake_head.current_mood = "going_up"

def decide_to_look_down():
    if mr_snake_head.current_mood != "going_up":
        mr_snake_head.current_mood = "going_down"

def decide_to_look_left():
    if mr_snake_head.current_mood != "going_right":
        mr_snake_head.current_mood = "going_left"

def decide_to_look_right():
    if mr_snake_head.current_mood != "going_left":
        mr_snake_head.current_mood = "going_right"

def actually_move_the_muscles():
    if mr_snake_head.current_mood == "going_up":
        current_y = mr_snake_head.ycor()
        mr_snake_head.sety(current_y + 20)

    if mr_snake_head.current_mood == "going_down":
        current_y = mr_snake_head.ycor()
        mr_snake_head.sety(current_y - 20)

    if mr_snake_head.current_mood == "going_left":
        current_x = mr_snake_head.xcor()
        mr_snake_head.setx(current_x - 20)

    if mr_snake_head.current_mood == "going_right":
        current_x = mr_snake_head.xcor()
        mr_snake_head.setx(current_x + 20)

# Listen to the keyboard commands (the voice of the gamer)
game_window.listen()
game_window.onkeypress(decide_to_look_up, "Up")
game_window.onkeypress(decide_to_look_down, "Down")
game_window.onkeypress(decide_to_look_left, "Left")
game_window.onkeypress(decide_to_look_right, "Right")

# --- The Circle of Life (Main Game Loop) ---
while True:
    game_window.update()

    # Did we smack our face into a wall?
    if mr_snake_head.xcor() > 290 or mr_snake_head.xcor() < -290 or mr_snake_head.ycor() > 290 or mr_snake_head.ycor() < -290:
        print("Ouch! I bumped my head on the wall! Restarting my life...")
        time.sleep(1)
        mr_snake_head.goto(0, 0)
        mr_snake_head.current_mood = "chilling"

        # Banish the old tummy parts off-screen so we don't see them anymore
        for body_part in growing_tummy_parts:
            body_part.goto(1000, 1000)
        
        # Go back to being a tiny snake
        growing_tummy_parts.clear()

    # Did we just eat the snack?
    if mr_snake_head.distance(yummy_snack) < 20:
        print("Yum! That was delicious.")
        
        # Throw the snack to a new random spot on the board
        new_x = random.randint(-14, 14) * 20
        new_y = random.randint(-14, 14) * 20
        yummy_snack.goto(new_x, new_y)

        # Grow a new belly segment because we ate
        new_belly_fat = turtle.Turtle()
        new_belly_fat.speed(0)
        new_belly_fat.shape("square")
        new_belly_fat.color("light green")
        new_belly_fat.penup()
        growing_tummy_parts.append(new_belly_fat)

    # Move the tummy parts in reverse order so they blindly follow the one in front of them
    total_parts = len(growing_tummy_parts)
    for index in range(total_parts - 1, 0, -1):
        x_where_front_guy_is = growing_tummy_parts[index - 1].xcor()
        y_where_front_guy_is = growing_tummy_parts[index - 1].ycor()
        growing_tummy_parts[index].goto(x_where_front_guy_is, y_where_front_guy_is)

    # Move the very first tummy part to where the head just was
    if total_parts > 0:
        x_where_head_is = mr_snake_head.xcor()
        y_where_head_is = mr_snake_head.ycor()
        growing_tummy_parts[0].goto(x_where_head_is, y_where_head_is)

    # Alright, time to actually slide forward
    actually_move_the_muscles()

    # Did we accidentally bite our own tail? (That hurts and is embarrassing)
    for body_part in growing_tummy_parts:
        if body_part.distance(mr_snake_head) < 20:
            print("Yeouch! I bit my own tail. I am not a smart snake.")
            time.sleep(1)
            mr_snake_head.goto(0, 0)
            mr_snake_head.current_mood = "chilling"

            # Hide the old tummy parts again
            for part in growing_tummy_parts:
                part.goto(1000, 1000)
            growing_tummy_parts.clear()

    # Take a tiny micro-nap so we don't travel at the speed of light
    time.sleep(sluggishness)

game_window.mainloop()