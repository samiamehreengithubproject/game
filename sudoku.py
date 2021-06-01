#Set window color grey
import turtle
import random 
import turtle  
turtle.bgcolor("grey")

# --------------- Made this function to arrange our coordinates and environment whenever we play ------------- #

#arranging this function in the coordinates(x axis and y axis )
def setWorld():
    turtle.setworldcoordinates(-110, -110, 110, 110)
    turtle.hideturtle()
    turtle.pensize(10)
    turtle.speed(0)
    turtle.pu()
    turtle.goto(-75, -75)


# ------------ A function to draw the outer large square ------------- #
#drawing the outer large square(grid) for this function to place the number 
def drawGrid():
    for i in range(2):
        turtle.fd(150)
        turtle.lt(90)
        turtle.fd(150)
        turtle.lt(90)


# ------------ A function to draw small squares boxes within the outer large square grid 
def drawSquare():
    for i in range(2):
        turtle.fd(36)
        turtle.lt(90)
        turtle.fd(36)
        turtle.lt(90)


# ------------- A function to keep drawing squares and moving forward until it reaches a specific x-coordinate --------#
def move_turtle():
    turtle.pd()
    while not (turtle.xcor() >= 75):
        drawSquare()
        turtle.setx(turtle.xcor() + 37.5)


# ---------------- 'move_turtle()' draws squares in one row.  ---------------------- #
def make_box():
    row_boxes = 0
    turtle.sety(-37.5)
    while row_boxes != 4:
        move_turtle()
        turtle.setx(-75)
  # making square boxes from the left for each row
        turtle.sety(
            turtle.ycor() + 37.5)  
# Once boxes are filled in one row, move y coordinate up. E.g (Makes boxes along row 'D', now  move up
        row_boxes += 1  
#Do this until all the four rows are completed with boxes
    turtle.pu()


# ------------- A function to label the row and column
def labelGrid():
    rows = ['1', '2', '3', '4']
    cols = ['A', 'B', 'C', 'D']

    for row_name in rows:
        turtle.write(row_name, move=False, align='left', font=(' Arial ', 40, 'normal'))
        turtle.sety(turtle.ycor() - 40)

    turtle.goto(-65, 75)
    for col_name in cols:
        turtle.write(col_name, move=False, align='left', font=(' Arial ', 40, 'normal'))
        turtle.setx(turtle.xcor() + 40)


# --------------- A function that uses the turtle class as an eraser ---------- #
def eraseEntry(puzzle):
    '''
    Takes in the puzzle
    Asks the user if they want to erase the entry before hand
    '''
    eraser = turtle.Turtle()
    eraser.hideturtle()
    eraser.speed(0)
    eraser.pu()

    ask_user = turtle.textinput('', 'Do you want to erase the previous entry? (y/n)')
    if ask_user in ['y', 'YES', 'yes']:
        eraser.goto(turtle.xcor() + 5,
                    turtle.ycor())  
# I had to adjust where the eraser goes accordingly. By trial and error I just had to move it a bit
        eraser.pd() 
 # to the right.
        eraser.color('white', 'white')
        eraser.begin_fill()
        eraser.circle(10)  # Using a white circle to be my eraser
        eraser.end_fill()


def take_input(puzzle):
    grid_rows = ['1', '2', '3', '4']
    grid_cols = ['A', 'B', 'C', 'D']

    col_increment_size = [-60, -30, 10, 50]
    row_increment_size = [50, 10, -30, -60]

    user_input = turtle.textinput('', 'Enter Row and Column (e.g 4B)')

    x_cor = 0
    y_cor = 0

    for r in range(0, len(grid_rows)):
        if grid_rows[r] == user_input[0]:  
# First 'element' of the user's input will be the row. E.g: 1B
            y_cor = row_increment_size[r]

    for c in range(0, len(grid_cols)):
        if grid_cols[c] == user_input[1]:  
# Second 'element' of the user's input will be the column.
            x_cor = col_increment_size[c]

    turtle.goto(x_cor, y_cor)

    # Attached the puzzle which is a nested list

    get_input = turtle.textinput('', 'Enter a number and make your move!')

    for i in range(0, len(grid_rows)):
        if user_input[0] == grid_rows[i]:
            for j in range(0, len(grid_cols)):
                if user_input[1] == grid_cols[j]:
                    if puzzle[i][j] != 0:  
# Call the eraseEntry function and ask
                        eraseEntry(puzzle)
#Asking the users wheather they want to erase the number where there isn’t a zero 
                    puzzle[i][j] = int(get_input)
                    make_move = turtle.write(get_input, move=False, align='center', font=(' Arial ', 35, 'normal'))

    return puzzle


def populatePuzzle(puzzle):
    '''
  This function in a puzzle (which is a nested list)  will return the grid with the same initial number inside the grid '''

    col_increment_size = [-60, -30, 10, 50] 
 # Starts at A1 (-60,50), A2 (-30,50), A3 (10,50) .... D4 (50,-60)
    row_increment_size = [50, 10, -30, -60]

    for row in range(0, len(puzzle)):  
# Enables the user to enter the row
        for col in range(0, len(puzzle[row])):  
# Enter the the row and which column the element belongs to
            if puzzle[row][col] != 0:  # If the initial base is not 0, populate the grid
                turtle.goto(col_increment_size[col], row_increment_size[row])
                turtle.write(puzzle[row][col], move=False, align='center', font=(' Arial', 35, 'normal'))


