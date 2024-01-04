#
# Program to draw how much the UK political parties care
# JCA and bard.google.com
# January 2024
#also https://docs.google.com/spreadsheets/d/161Df7tQFZrKhVPAy4vCT19RoDXl2dAsqOWRdOkNInp4/edit#gid=0
import turtle

# Define colors for each party
reformUKcolor = "#40E0D0"
toryBlue = "#0087dc"
labourRed = "#d50000"
libDemOrange = "#FDBB30"
greensGreen = "#008066"

# Create turtle screen and set up pen
screen = turtle.Screen()
screen.setup(600, 600)
pen = turtle.Turtle()
pen.speed(0)  # Set fastest drawing speed

# Define function to draw and label a circle
def draw_circle(x, y, radius, color, label):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.fillcolor(color)
    pen.begin_fill()
    pen.circle(radius)
    pen.end_fill()
    # Calculate label position near top of circle
    label_x = x
    label_y = y + 2*radius - 50    # Adjust for label placement
    pen.penup()
    pen.goto(label_x, label_y)
    pen.pendown()
    pen.color("black")
    pen.write(label, align="center", font=("Courier", 10))

# Draw concentric circles with labels (Green as largest)
xinc = 30
rinc = 45
draw_circle(0, -230, 80+4*rinc, greensGreen, "Greens - \nThe actual world")
draw_circle(0, -230+xinc, 80+3*rinc, libDemOrange, "Liberal -\nWorld citizens")
draw_circle(0, -230+2*xinc, 80+2*rinc, labourRed, "Labour -\nUK citizens")
draw_circle(0, -230+3*xinc, 80+rinc, toryBlue, "Conservative -\nTheir cronies")
draw_circle(0, -230+4*xinc, 80, reformUKcolor, "Reform -\nThemselves")
pen.penup()
pen.goto(-250, 250)
pen.pendown()
pen.write("Who cares for\nwho....", align="left", font=("Courier", 12))
# Hide the turtle
pen.hideturtle()

# Keep the window open until closed manually
turtle.done()
