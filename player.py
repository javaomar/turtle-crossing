from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.go_to_start()
        self.setheading(90)
        self.move_distance = MOVE_DISTANCE

    def go_up(self):
        # Move the player turtle up
        self.forward(self.move_distance)

    def go_left(self):
        # Move the player turtle left
        new_x = self.xcor() - self.move_distance
        self.goto(new_x, self.ycor())
    
    def go_right(self):
        # Move the player turtle right
        new_x = self.xcor() + self.move_distance
        self.goto(new_x, self.ycor())

    def go_to_start(self):
        # Reset player's position to the starting line
        self.goto(STARTING_POSITION)

    def is_at_finish_line(self):
        # Check if the player has reached the finish line
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False
    def increase_speed(self):
        # Increase the player's speed when called
        self.move_distance += 2  # You can adjust the amount of increase