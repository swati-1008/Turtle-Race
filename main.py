from turtle import Turtle, Screen
import random

screen = Screen()

is_game_on = False
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make a bet!", prompt="Which turtle is likely to win the race?"
                                                        "Enter a colour: ")

colours = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []
y = -100

if user_bet:
    is_game_on = True

for colour in colours:
    timmy_the_turtle = Turtle("turtle")
    timmy_the_turtle.penup()
    timmy_the_turtle.goto(x=-230, y=y)
    y += 50
    timmy_the_turtle.color(colour)
    turtles.append(timmy_the_turtle)


while is_game_on:
    for turtle in turtles:
        if not is_game_on:
            break
        if turtle.xcor() > 230:         # turtle is by default 40 x 40, so (250 - 40 / 2) = 230
            is_game_on = False
            winning_colour = turtle.pencolor()
            if winning_colour == user_bet:
                print(f"You've won! The {winning_colour} turtle is the winner.")
            else:
                print(f"You've lost! The {winning_colour} turtle is the winner.")
        else:
            turtle.forward(random.randint(0, 10))

screen.exitonclick()
