"""A fun drawing program."""

__author__ = "730665100"

from turtle import Turtle, colormode, done
field: Turtle = Turtle()
colormode(255)
MAX_SPEED = 0
X_VAR = 400
Y_VAR = 475
# Draw the outline of the field


def main() -> None:
    """The function that calls all of the other functions to draw a field."""
    drawfield(field, X_VAR, Y_VAR)
    
    drawyardlines(yardlines, X_VAR, Y_VAR)
    
    drawhashes(hashmarks, X_VAR, Y_VAR)
    
    drawlilhashes()
    
    drawlogos(logos, X_VAR, Y_VAR)
    
    drawlogos(logos, X_VAR - 600, Y_VAR - 525)
    
    done()

       
def drawfield(field: Turtle, X_VAR: int, Y_VAR: int) -> None:
    """Draws the rectangle that is the field and colors it in."""
    field.speed(MAX_SPEED)
    field.begin_fill()
    field.penup()
    field.goto(-X_VAR, Y_VAR)
    field.pendown()
    field.goto(-400, -475)
    field.goto(400, -475)
    field.goto(400, 475)
    field.goto(-400, 475)

    field.fillcolor("darkgreen")
    field.end_fill()

    field.penup()
    field.goto(0, 400)
    field.pendown()
    field.color(75, 156, 211)
    field.write("TAR HEELS", align="center", font=("Bernard MT Condensed", 40, "normal"))

    field.penup()
    field.goto(0, -460)
    field.pendown()
    field.color(75, 156, 211)
    field.write("CAROLINA", align="center", font=("Bernard MT Condensed", 40, "normal"))
    field.hideturtle()
    # Draw the yard lines
    
 
yardlines: Turtle = Turtle()   


def drawyardlines(yardlines: Turtle, X_VAR: int, Y_VAR: int) -> None:
    """Draws the yardlines on the field."""
    yardlines.speed(MAX_SPEED)
    for i in range(-X_VAR, Y_VAR - 25, 100):
        yardlines.color("white")
        yardlines.penup()
        yardlines.goto(-400, i)
        yardlines.pendown()
        yardlines.goto(400, i)
        yardlines.hideturtle()       


# Draw the hash marks
hashmarks: Turtle = Turtle()


def drawhashes(hashmarks: Turtle, X_VAR: int, Y_VAR: int) -> None:
    """Draws the hashmarks for the field."""
    hashmarks.speed(MAX_SPEED)
    for i in range(-X_VAR, Y_VAR - 50, 50):
        hashmarks.color("white")
        hashmarks.penup()
        hashmarks.goto(-50, i)
        hashmarks.pendown()            
        hashmarks.goto(50, i)
        hashmarks.hideturtle()
    
    
def drawlilhashes() -> None:
    """Draws even smaller hashes that represent a single yard."""
    littlehashmarks: Turtle = Turtle()
    littlehashmarks.speed(MAX_SPEED)
    for i in range(-400, 400, 10):
        littlehashmarks.color("white")
        littlehashmarks.penup()
        littlehashmarks.goto(-175, i)            
        littlehashmarks.pendown()
        littlehashmarks.goto(-150, i)
        littlehashmarks.hideturtle()
        
        littlehashmarks.color("white")
        littlehashmarks.penup()
        littlehashmarks.goto(150, i)            
        littlehashmarks.pendown()
        littlehashmarks.goto(175, i)
        littlehashmarks.hideturtle()
    

logos: Turtle = Turtle() 


def drawlogos(logos: Turtle, X_VAR: int, Y_VAR: int) -> None:
    """Draws the ACC logo on the field."""
    logos.speed(MAX_SPEED)
    logos.penup()
    logos.goto(-X_VAR + 100, -Y_VAR + 175)
    logos.right(90)
    logos.pendown()
    logos.color("black")
    logos.write("ACC", align="center", font=("Bernard MT Condensed", 30, "italic"))


if __name__ == "__main__":
    main()