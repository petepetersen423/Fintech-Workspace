"""
CIS 122 Spring 2022 Project 3-2
Author(s): Peter Petersen, Areyan Rastawan
Credit: CIS 122 Resources only
Description: Intro to Python Turtle Graphics
"""
import turtle

# from turtle import *


def poly(num_sides, side_len, pcolor):

    """
    aux function draws a polygon with given of sides with its side length
    num_sides = number of sides in polygon
    side_len = desired length of sides in polygon
    pcolor = color of shape
    >>>poly(4,200,'red')
    [draws a red sqaure with side length of 200]
    """

    fillcolor(pcolor)
    begin_fill()
    for i in range(num_sides):
        fd(side_len)
        lt(360 / num_sides)
    turtle.end_fill()


def house():

    """
    function that draws a house
    """

    poly(4, 200, "green")
    jump(0, 200)
    poly(3, 200, "black")
    jump(85, 0)
    poly(4, 65, "black")


def art_show_main():
    """
    function that draws a garage next to house
    """
    jump(200, 0)
    poly(4, 100, "green")
    jump(200, 100)
    poly(3, 100, "black")
    jump(215, 0)
    poly(4, 60, "black")


def jump(x, y):
    """aux function sets turtle position
    without leaving pen trail
    >>> jump(100, 100)
    [turtle positioned at 100, 100]
    """
    penup()
    setposition(x, y)
    pendown()
    return


# jump(100, 100)
def main():
    """driver for code to draw a house"""
    # set up turtle environment
    # reset()
    title("A Very Fine House")
    speed(0)
    hideturtle()
    # draw the house
    house()
    art_show_main()

    return


main()
