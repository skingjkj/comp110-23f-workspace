"""Ex05: A person standing on the edge of a cliff at night!"""
__author__ = "730665331"

from turtle import Turtle, colormode, done, tracer, update
from random import randint
import turtle

colormode(255)
MAX_SPEED: int = 0


def main() -> None:
    """The entrypoint of my scene."""
    tracer(0, 0)
    story: Turtle = Turtle()
    story.speed(MAX_SPEED)
    # Set background color to black to represent night sky and defining size.
    turtle.Screen().screensize(-500, 500, "black")
    story.hideturtle()
    idx1: int = 0
    idx2: int = 0
    x_position: int = -150
    y_position: int = -150

    # Draws the ocean.
    while idx1 < 6: 
        ocean_background(story, x_position, y_position, 500)
        x_position += 250
        idx1 += 1

    # Drawing 25 randomly sized stars.
    while idx2 < 25:
        random_stars(story, randint(-1000, 400), randint(20, 450), randint(3, 13))
        idx2 += 1

    # Drawing the base of the cliff.
    square_cliff(story, -500, 0, 650)

    # Drawing the tip of the cliff.
    triangle_cliff(story, -400, 0, 250)

    # Drawing a moon.
    moon(story, 700, 300, 50)

    # Draws the head of the character.
    character1(story, -420, 100, 15)

    # Draws the body of the character.
    character2(story, -400, 100, 42)

    # Draws the first leg of the character.
    character3(story, -407, 60, 30)

    # Draws the second leg of the character.
    character4(story, -405, 60, 30)

    update()
    done()


def random_stars(star: Turtle, x: float, y: float, length: float) -> None:
    """Draws a star in white."""
    star.penup()
    star.goto(x, y)
    star.setheading(0.0)
    star.pendown()

    # Setting the outline and fill color to ivory
    star.pencolor(255, 255, 240)
    star.fillcolor(255, 255, 240)

    star.begin_fill()
    star_sides: int = 0

    # Drawing a star.
    while star_sides < 5:
        star.right(145)
        star.forward(length)
        star_sides += 1
    star.end_fill()


def ocean_background(ocean: Turtle, x: float, y: float, length: float) -> None:
    """Makes a blue square that will become part of the ocean."""
    ocean.penup()
    ocean.goto(x, y)
    ocean.setheading(0.0)
    ocean.pendown()

    # Setting the outline and fill color to blue to create ocean.
    ocean.pencolor(0, 0, 139)
    ocean.fillcolor(0, 0, 139)

    ocean.begin_fill()
    rectangle_sides: int = 0

    # Drawing a rectangle.
    while rectangle_sides < 4:
        ocean.right(90)
        ocean.forward(length)
        rectangle_sides += 1
    ocean.end_fill()


def square_cliff(cliff1: Turtle, x: float, y: float, length: float) -> None:
    """Makes the base of the cliff."""
    cliff1.penup()
    cliff1.goto(x, y)
    cliff1.setheading(0.0)
    cliff1.pendown()

    # Setting the outline and fill color to grey to create base of cliff.
    cliff1.pencolor(113, 130, 126)
    cliff1.fillcolor(113, 130, 126)
    cliff1.begin_fill()
    rectangle_sides: int = 0

    # Drawing a square.
    while rectangle_sides < 4:
        cliff1.right(90)
        cliff1.forward(length)
        rectangle_sides += 1
    cliff1.end_fill()


def triangle_cliff(cliff2: Turtle, x: float, y: float, length: float) -> None:
    """Makes the tip of the cliff."""
    cliff2.penup()
    cliff2.goto(x, y)
    cliff2.setheading(0.0)
    cliff2.pendown()

    # Setting the outline and fill color to grey to create tip of cliff.
    cliff2.pencolor(113, 130, 126)
    cliff2.fillcolor(113, 130, 126)
    cliff2.begin_fill()
    triangle_sides: int = 0

    # Drawing a triangle.
    while triangle_sides < 3:
        cliff2.right(120)
        cliff2.forward(length)
        triangle_sides += 1
    cliff2.end_fill()


def moon(moon_shape: Turtle, x: float, y: float, radius: float) -> None:
    """Makes the moon."""
    moon_shape.penup()
    moon_shape.goto(x, y)
    moon_shape.setheading(0.0)
    moon_shape.pendown()

    # Setting the outline and fill color to yellow-ish white to create the color of moon.
    moon_shape.pencolor(246, 241, 213)
    moon_shape.fillcolor(246, 241, 213)

    moon_shape.begin_fill()
    moon_shape.circle(radius)
    moon_shape.end_fill()


def character1(head: Turtle, x: float, y: float, radius: float) -> None:
    """Makes the head of the character."""
    head.penup()
    head.goto(x, y)
    head.setheading(0.0)
    head.pendown()

    # Setting the outline and fill color to white to make the character standout from the background.
    head.pencolor(255, 255, 255)
    head.fillcolor(255, 255, 255)

    head.begin_fill()
    head.circle(radius)
    head.end_fill()


def character2(body: Turtle, x: float, y: float, length: float) -> None:
    """Makes the body of the character."""
    body.penup()
    body.goto(x, y)
    body.setheading(0.0)
    body.pendown()

    # Setting the outline and fill color to unc blue to make the character standout from the background.
    body.pencolor(123, 175, 212)
    body.fillcolor(123, 175, 212)

    body.begin_fill()
    rectangle_sides: int = 0

    # Drawing a square.
    while rectangle_sides < 4:
        body.right(90)
        body.forward(length)
        rectangle_sides += 1
    body.end_fill()


def character3(leg1: Turtle, x: float, y: float, length: float) -> None:
    """Makes the first leg of the character."""
    leg1.penup()
    leg1.goto(x, y)
    leg1.setheading(0.0)
    leg1.pendown()

    # Setting the outline and fill color to unc blue to make the character standout from the background.
    leg1.pencolor(123, 175, 212)
    leg1.fillcolor(123, 175, 212)

    leg1.begin_fill()
    rectangle_sides: int = 0

    # Drawing a rectangle.
    while rectangle_sides < 2:
        leg1.right(90)
        leg1.forward(length * 2)
        leg1.right(90)
        leg1.forward(length)
        rectangle_sides += 1
    leg1.end_fill()


def character4(leg2: Turtle, x: float, y: float, length: float) -> None:
    """Makes the second leg of the character."""
    leg2.penup()
    leg2.goto(x, y)
    leg2.setheading(0.0)
    leg2.pendown()

    # Setting the outline and fill color to unc blue to make the character standout from the background.
    leg2.pencolor(123, 175, 212)
    leg2.fillcolor(123, 175, 212)

    leg2.begin_fill()
    rectangle_sides: int = 0

    # Drawing a rectangle.
    while rectangle_sides < 2:
        leg2.right(90)
        leg2.forward(length * 2)
        leg2.right(90)
        leg2.forward(length)
        rectangle_sides += 1
    leg2.end_fill()


if __name__ == "__main__":
    main() 