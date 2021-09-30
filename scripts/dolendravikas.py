import os
import time

def animate_Rocket():
  distanceFromTop = 20
  while True:
    print("\n" * distanceFromTop)
    print("------------")
    print("Hello World")
    print("------------")
    time.sleep(0.2)
    os.system('clear')  
    distanceFromTop -= 1
    if distanceFromTop <0:
      distanceFromTop = 20

animate_Rocket()
