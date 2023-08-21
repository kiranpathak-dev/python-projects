# Reeborg's world: https://reeborg.ca/
# Hurdle 3: http://bitly.ws/SFr3
# Reeborg has entered a hurdle race. Make him run the course, following the path shown.
# The position and number of hurdles changes each time this world is reloaded.

def turn_right():
  turn_left()
  turn_left()
  turn_left()
    
def jump():
  turn_left()
  move()
  turn_right()
  move()
  turn_right()
  move()
  turn_left()
  

while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()
