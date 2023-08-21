# Reeborg's world: https://reeborg.ca/
# Hurdle 2: http://bitly.ws/SF9t
#Reeborg has entered a hurdle race, but he does not know in advance how long the race is. 
#Make him run the course, following a path similar to the one shown, but stopping at the only flag that will be shown after the race has started.

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
  
while not at_goal():
    jump()

#2nd method
# while at_goal() != True:
#     jump()