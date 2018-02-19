import turtle

s = turtle.Screen()
s.bgcolor('#7EC0EE')
turtle.color('#FF3366')

pizza = turtle.Turtle()
pizza.color('#FF3366')

yoda = turtle.Turtle()
yoda.color('#6565AF')

def drawSquares(name, size, num, angle):

    for i in range(num):
        for x in range(4):
            pizza.forward(size)
            pizza.left(45)
        pizza.right(angle)

drawSquares(pizza, 125, 36, -10)

def drawSquares(name, size, num, angle):

    for i in range(num):
        for x in range(4):
            yoda.forward(size)
            yoda.left(90)
        yoda.right(angle)

drawSquares(yoda, 125, 36, -10)

s.exitonclick()

# turtle.forward(100)
# turtle.right(90)
# turtle.forward(100)
# turtle.right(90)
# turtle.forward(100)
# turtle.right(90)
# turtle.forward(100)
# turtle.right(90)
# turtle.right(-10)

# sun = turtle.Turtle()
# sun.color('#FFCC00')
# sun.circle(15)
