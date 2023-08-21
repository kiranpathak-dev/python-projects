# Reeborg's world: https://reeborg.ca/
# Hurdle 1: http://bitly.ws/SCCw
#Reeborg has entered a hurdles race. Make him run the course, following the path shown.
# A robot located at (x, y) = (1, 1) carries no objects.
# Goal to achieve: The final position of the robot must be (x, y) = (13, 1)

def turn_right():
  turn_left()
  turn_left()
  turn_left()
    
def jump():
  move()
  turn_left()
  move()
  turn_right()
  move()
  turn_right()
  move()
  turn_left()
    
for step in range(0,6):
    jump()