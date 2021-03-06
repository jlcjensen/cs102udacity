import turtle

#draw triangle with left turns
def initial_triangle(turtle,dist,turn):
    i = 0
    while i < 3:
        
        turtle.forward(dist)
        turtle.left(turn)

        i += 1

#draw upside down triangle with left turns
def left_inner_triangles(turtle,dist,turn1,turn2):

    turtle.fill(True)
    turtle.left(turn1)
    turtle.forward(dist)
    turtle.left(turn2)
    turtle.forward(dist)
    turtle.left(turn2)
    turtle.forward(dist)
    turtle.fill(False)

#draw upside down triangles with right turns
def right_inner_triangles(turtle,dist,turn1,turn2):
    
    turtle.fill(True)
    turtle.right(turn1)
    turtle.forward(dist)
    turtle.right(turn2)
    turtle.forward(dist)
    turtle.right(turn2)
    turtle.forward(dist)
    turtle.fill(False)

#draw final triangles
def turtle_art():
    window = turtle.Screen()
    window.bgcolor("white")

    #create turtle
    hopper = turtle.Turtle()
    hopper.shape("turtle")
    hopper.color("darkgreen","green")
    hopper.fillcolor("green")
    hopper.speed(10)

    hopper.fill(True)
    initial_triangle(hopper,200,120)
    hopper.fill(False)

    hopper.fillcolor("white")

    hopper.forward(200)
    hopper.left(120)
    hopper.forward(100)
    
    left_inner_triangles(hopper,100,60,120)

    hopper.left(60)
    hopper.forward(50)

    left_inner_triangles(hopper,50,60,120)

    hopper.left(60)
    hopper.forward(25)

    left_inner_triangles(hopper,25,60,120)

    hopper.right(120)
    hopper.forward(50)

    right_inner_triangles(hopper,25,60,120)

    hopper.right(60)
    hopper.forward(25)
    hopper.right(120)
    hopper.forward(75)

    right_inner_triangles(hopper,25,60,120)

    hopper.right(120)
    hopper.forward(25)
    hopper.left(120)
    hopper.forward(75)

    left_inner_triangles(hopper,50,60,120)

    hopper.left(60)
    hopper.forward(25)

    left_inner_triangles(hopper,25,60,120)

    hopper.left(60)
    hopper.forward(25)
    hopper.left(120)
    hopper.forward(75)

    left_inner_triangles(hopper,25,60,120)

    hopper.left(120)
    hopper.forward(25)
    hopper.left(60)
    hopper.forward(50)

    left_inner_triangles(hopper,25,60,120)

    hopper.left(60)
    hopper.forward(25)
    hopper.right(120)
    hopper.forward(100)
    hopper.right(60)
    hopper.forward(50)

    right_inner_triangles(hopper,50,60,120)

    hopper.right(60)
    hopper.forward(25)

    right_inner_triangles(hopper,25,60,120)

    hopper.right(60)
    hopper.forward(25)
    hopper.right(120)
    hopper.forward(75)

    right_inner_triangles(hopper,25,60,120)

    hopper.right(120)
    hopper.forward(25)
    hopper.right(60)
    hopper.forward(50)

    right_inner_triangles(hopper,25,60,120)

    hopper.fillcolor("green")

    hopper.right(60)
    hopper.forward(25)
    hopper.left(60)
    hopper.forward(100)
    hopper.left(120)
    hopper.forward(200)
    hopper.left(120)
    hopper.forward(150)

    window.exitonclick()

turtle_art()
