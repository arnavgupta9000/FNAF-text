import random
import time

class player(object):
  def __init__(self,control,time,power,rightLight,lightLeft,rightDoor, leftDoor, camera, powerOut, day):
    self.control = control
    self.time = time
    self.power = power
    self.rightLight = rightLight
    self.lightLeft = lightLeft
    self.rightDoor = rightDoor
    self.leftDoor = leftDoor
    self.camera = camera
    self.powerOut = powerOut
    self.day = day
  # for time
  # every action we'll add 1 to control and every time control = 10, reset to 1 and add 1 hour to time
  def convert(self):
    if self.control >= (15 - self.day):
      self.time +=1
      self.control = 0 

  # power management
  def powerClass(self):
    # were gonna use 1 light system to subtract power from both left light and right light
    if self.light:
      self.power = self.power - 1 
    if self.camera:
      self.power = self.power - 1
      # cant have 1 system for doors as that would break the game
    if self.rightDoor == "close":
      self.power = self.power -2
    if self.leftDoor == "close":
      self.power = self.power - 2
    
    if self.power <= 0:
      print("you can no longer use lights or doors")
      self.powerOut = True

class animatronic(object):
  def __init__(self,door,area, seeAnimatronic,timer,seeAnimatronicLeft,leftDoor):
    self.door = door
    self.area = area
    self.seeAnimatronic = seeAnimatronic
    self.timer = timer
    self.seeAnimatronicLeft = seeAnimatronicLeft
    self.leftDoor = leftDoor

  def move(self):
    location = self.area
    if player1.control + 1:
      # the higher the day, the more chance the animatronic moves givng it harder difficulty
      rollOdds = random.randint(1, (6 - player1.day))
      if rollOdds == 1 and self.area != 6 and self.area != 7:
        global holder
        self.seeAnimatronic = False
        rollOddsCams = random.randint(1,5)
        # determine where the anamatronic will go
        self.area = rollOddsCams
        print(self.area) 
    
        if self.area == location:
          self.area +=1
          if self.area >= 6:
            self.area = 1
            # 1 if for left side and 2 is for right side
      if self.area == 1 or self.area == 2:
        print("animatronic outside door")
        if self.area == 1:
          self.area = 6
        elif self.area == 2:
          self.area = 7
        if player1.day <=3:
          holder = 4
        elif player1.day >3 and player1.day <=4:
          holder = 3
        else:
          holder = 2
        
      if self.area == 6: 
        if player1.control + 1:
          self.timer +=0.5
        if self.timer >= holder and player1.rightDoor == "open":
            self.door = True
            # self.seeAnimatronic = True
            print("you have been jumpscared and survived until ", player1.time)
            restart()
        elif self.timer <= holder and player1.rightDoor == "close":
          self.door = False
          self.seeAnimatronic = False
          self.area = 3 or 4 or 5
          holder = 0
          self.timer = 0

        elif self.timer <= holder and player1.rightDoor == "open":
         self.door = False
         self.seeAnimatronic = True

        else:
          self.door = False
          self.seeAnimatronic = False
          self.area = 3 or 4 or 5
          holder = 0 
          self.timer = 0
          
        # same thing for the opposite side
      if self.area == 7: 
          if player1.control + 1:
            self.timer +=0.5
          if self.timer >= holder and player1.leftDoor == "open":
              self.leftDoor = True
              # self.seeAnimatronic = True
              print("you have been jumpscared and survived until ", player1.time)
              restart()
          elif self.timer <= holder and player1.leftDoor == "close":
            self.leftDoor = False
            self.seeAnimatronicLeft = False
            self.area = 3 or 4 or 5
            holder = 0
            self.timer = 0
  
          elif self.timer <= holder and player1.leftDoor == "open":
           self.leftDoor = False
           self.seeAnimatronicLeft = True
  
          else:
            self.leftDoor = False
            self.seeAnimatronicLeft = False
            self.area = 3 or 4 or 5
            holder = 0 
            self.timer = 0

class foxy(object):
  def __init__(self,area,timer,secondTimer):
    self.area = area
    self.timer = timer
    self.secondTimer = secondTimer
  
  def move(self):
    if player1.control + 1:
      self.timer +=1
    if self.timer > 35 - (player1.day * 5):
      self.area = 1
      if player1.control +1:
        self.secondTimer +=1
    if self.area == 1:
      if self.secondTimer >= 11 - (2 * player1.day) and player1.leftDoor == "open":
        print("Foxy has jumpscared you, you survived until", player1.time)
        restart()
      elif self.secondTimer < 11 -(2 * player1.day) and player1.leftDoor == "close":
        self.area = 5
        self.timer = 0
        self.secondTimer = 0
      else:
        self.area = 5
        self.timer = 0
        self.secondTimer = 0

class jj(object):
  def __init__(self,var):
    self.var = var
  def badRoll(self):
    unlucky = random.randint(1,100)
    if unlucky == 1:
      print("jj has appeared")
      print("DONT TYPE ANYTHING")
      time.sleep(5)
      chance = random.randint(0,2)
      if chance == 1 and self.var == False:
        print("JJ has added another anamatronic")
        global animatronic2
        animatronic2 = animatronic(False, 4, False,0,False,False)
        # so we can remove anamtronic at the end of the night and to move the anamtronic while avoiding error
        self.var = True
      else:
        player1.power -= 5
        print("JJ has just taken 5% power")

def controlFunction ():
  player1.control +=1
  player1.convert()
  player1.powerClass()
  animatronic1.move()
  jj1.badRoll()
  foxy1.move()

  if jj1.var == True:
    animatronic2.move()

# whenever the player dies, we can just reset everything
def restart():
  player1.time = 0
  player1.power = 100
  player1.control = 0
  player1.rightDoor = "open"
  player1.leftDoor = "open"
  player1.rightLight = False
  player1.lightLeft = False
  animatronic1.area = 4
  animatronic1.timer = 0
  animatronic1.door = False
  animatronic1.seeAnimatronic = False
  foxy1.area = 5
  foxy1.timer = 0
  foxy1.secondTimer = 0
  jj1.var = False
  main()




def customGame():
  print(f"contrgrats on making it do {player1.day}, now you can customize the anamtronic")
  print("congrats you won the game")
  
      
player1 = player(0,0,100, False, False, "open", "open", False, False,1)
animatronic1 = animatronic(False, 4, False,0,False,False)
jj1 = jj(False)
foxy1 = foxy(5,0,0)

def main():
  menuLoop = True
  while menuLoop == True:
    if player1.day == 1:
      # customGame()
      pass
    print("1. The day you can play right now is ", player1.day, "\n2. reset")

    menuInput = input("What would you like to do? ").lower()

    if menuInput == "1":
      menuLoop = False

    if menuInput == "2":
      x = input("are you sure you want to restart? type restart to reset your days ").lower()
      if x == "restart":
        player1.day = 1
      else:
        continue

    if menuInput not in ["1" ,"2"]:
      print("not an option")
      continue
  loop = True
  while loop == True:
    
      camList = ["1a,1b,2a,2b"]
      newLoop = True
      while newLoop == True:
        inputMain = input("what would you like to do? ").lower()
        player1.light = False

        if player1.powerOut == False:

          # cam list interactions
          if inputMain == "camlist" or inputMain == "c":
            print(camList)
            camListLoop = True
            while camListLoop:
              inputCamlist = input("which cam would you like to check?").lower()
              player1.camera = False
              if inputCamlist == "1a":
                if animatronic1.area == 2:
                  print("you see the animatronic")
                else:
                  print("you see nothing")
                player1.camera = True
                controlFunction()

              elif inputCamlist == "1b":
                if animatronic1.area == 3:
                  print("you see the animatronic")
                else:
                  print("you see nothing")
                player1.camera = True
                controlFunction()

              elif inputCamlist == "2a":
                if animatronic1.area == 4:
                  print("you see the animatronic")
                else:
                  print("you see nothing")
                player1.camera = True
                controlFunction()

              elif inputCamlist == "2b":
                foxy1.timer = 0
                if foxy1.area == 5:
                  print("foxy can be seen on the stage there")
                else:
                  print("foxy is gone")
                player1.camera = True
                controlFunction()

              if inputCamlist == "quit" or inputCamlist == "q":
                camListLoop = False
          
          # main control areas
          if inputMain == "lightright" or inputMain == "lr" and animatronic1.door == False and animatronic1.seeAnimatronic == False:

            print("you see nothing")
            player1.light = True
            controlFunction()

          if inputMain == "lightright" or inputMain == "lr" and animatronic1.door == False and animatronic1.seeAnimatronic == True:
            print("the animatronic can be seen")
            player1.light = True
            controlFunction()
          if inputMain == "lightright" or inputMain == "lr" and animatronic1.door == True:
            print("You have been jumpscared, you survived until", player1.time)
            restart()

          if inputMain == "doorright" or inputMain == "dr":
            # if open, close
            if player1.rightDoor == "open":
              player1.rightDoor = "close"
              print("you have closed the RIGHT door")
              controlFunction()
            # if closed, open
            elif player1.rightDoor == "close":
              player1.rightDoor = "open"
              print("you have opened the RIGHT door")
              controlFunction()
          
          if inputMain == "lightleft" or inputMain == "ll" and animatronic1.leftDoor == False and animatronic1.seeAnimatronicLeft == False:

            print("you see nothing")
            player1.light = True
            controlFunction()

          if inputMain == "lightleft" or inputMain == "ll" and animatronic1.leftDoor == False and animatronic1.seeAnimatronicLeft == True:
            print("the animatronic can be seen")
            player1.light = True
            controlFunction()
          if inputMain == "lightleft" or inputMain == "ll" and animatronic1.leftDoor == True:
            print("You have been jumpscared, you survived until", player1.time)
            restart()

          if inputMain == "doorleft" or inputMain == "dl":
            # if open, close
            if player1.leftDoor == "open":
              player1.leftDoor = "close"
              print("you have closed the LEFT door")
              controlFunction()
            # if closed, open
            elif player1.leftDoor == "close":
              player1.leftDoor = "open"
              print("you have opened the LEFT door")
              controlFunction()
        
        else:
          print("you have no power")
          player1.rightDoor = "open"
          player1.leftDoor = "open"
          # controlFunction()
          
          if player1.time == 5 and player1.control >= 7:
            print("you survived night" , player1.day,"advancing to ", player1.day + 1) 
            player1.day+=1
            restart()
          else:
            print("you have been jumpscared")
            restart()
        
        if inputMain == "time" or inputMain == "t":
          print("the time is ", player1.time, "am")
          print("no action used")

        if inputMain == "power" or inputMain == "p":
          print(player1.power)
          print("no action used")
        
        if inputMain == "control":
          print(player1.control)
          print("no action used")
        if inputMain == "wait" or inputMain =="w":
          print("time has passed")
          controlFunction()
          # testing only
        if inputMain == "h" or inputMain == "help":
          print("you win this game by survivng to 6 am. Every time you do something an action will be used unless something says no action used. You can use ll, to use the light and see outside of your office and vice versa for lr. You can use dl or dr to close the left/right door respectively. Everytime an action is used animatronic can move around. Be sure to keep an eye on cam 2b for time to time. Acess cams by typing 'camlist'")
        if inputMain == "[":
         print("you survived night" , player1.day, "advancing to ", player1.day + 1) 
         player1.day+=1
         restart()

        if player1.time == 6:
         print("you survived night" , player1.day, "advancing to ", player1.day + 1) 
         player1.day+=1
         restart()

if __name__ == "__main__":
  main()
