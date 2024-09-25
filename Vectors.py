import gc
import math

class Point:
  x=0
  y=0

  def __init__(self, _x, _y) -> None:
    self.x = _x
    self.y = _y

  def isEqual(self, point) -> bool:
    return self.x == point.x and self.y == point.y
  # def x() -> float:
  #   return x
  # def y() -> float:
  #   return y

  # function to cast point to string

  # function to compare this point with other point
  # def isEquals(self, pointToCompare) -> bool:



class Vector:
  startPointX = 0
  startPointY = 0
  endPointX = 0
  endPointY = 0
  areaSizeX = 0
  areaSizeY = 0
  timeMilliseconds = 0
  invertAxisY = False
  points = []
  speed = 0
  nextPointOffset = Point(0, 0)
  initialAngle = 0
  actualAngle = 0
  flag_A = " "
  flag_B = " "
  flag_C = " "
  flag_D = " "
  flag_E = " "
  flag_F = " "
  flag_G = " "
  flag_H = " "
  flag_I = " "
  flag_J = " "

  def calcNextPoint(self) -> Point:
    if ((self.points[-1].x + self.nextPointOffset.x) <= self.areaSizeX):
      if ((self.points[-1].x + self.nextPointOffset.x) >= 0):
        if ((self.points[-1].y + self.nextPointOffset.y) <= self.areaSizeY):
          if ((self.points[-1].y + self.nextPointOffset.y) >= 0):
            # Normal DONE
            self.actualAngle = (math.atan((float(self.points[-1].y) - float(self.points[-2].y)) / (float(self.points[-1].x) - float(self.points[-2].x))) / math.pi) * float(180)
            self.flag_A = 1
            return Point(self.points[-1].x + self.nextPointOffset.x, self.points[-1].y + self.nextPointOffset.y)
          else:
            # Colition Top DONE
            self.nextPointOffset = Point(self.nextPointOffset.x, self.nextPointOffset.y * -1)
            self.actualAngle = (math.atan((float(self.points[-1].y) - float(self.points[-2].y)) / (float(self.points[-1].x) - float(self.points[-2].x))) / math.pi) * float(180)
            self.flag_B = 1
            return Point(self.points[-1].x + self.nextPointOffset.x, (self.points[-1].y + (self.nextPointOffset.y * -1)) * -1)
        else:
          # Colition Bottom DONE
          self.nextPointOffset = Point(self.nextPointOffset.x, self.nextPointOffset.y * -1)
          self.actualAngle = (math.atan((float(self.points[-1].y) - float(self.points[-2].y)) / (float(self.points[-1].x) - float(self.points[-2].x))) / math.pi) * float(180)
          self.flag_C = 1
          return Point(self.points[-1].x + self.nextPointOffset.x, self.areaSizeY - ((self.points[-1].y + (self.nextPointOffset.y * -1)) - self.areaSizeY))
      else:
        if ((self.points[-1].y + self.nextPointOffset.y) <= self.areaSizeY):
          if ((self.points[-1].y + self.nextPointOffset.y) >= 0):
            # Colition Left Done
            self.nextPointOffset = Point(self.nextPointOffset.x * -1, self.nextPointOffset.y)
            self.actualAngle = (math.atan((float(self.points[-1].y) - float(self.points[-2].y)) / (float(self.points[-1].x) - float(self.points[-2].x))) / math.pi) * float(180)
            self.flag_D = 1
            return Point((self.points[-1].x + (self.nextPointOffset.x * -1)) * -1, self.points[-1].y + self.nextPointOffset.y)
          else:
            # Colition Top Left DONE
            self.nextPointOffset = Point(self.nextPointOffset.x * -1, self.nextPointOffset.y * -1)
            self.actualAngle = (math.atan((float(self.points[-1].y) - float(self.points[-2].y)) / (float(self.points[-1].x) - float(self.points[-2].x))) / math.pi) * float(180)
            self.flag_E = 1
            return Point((self.points[-1].x + (self.nextPointOffset.x * -1)) * -1, (self.points[-1].y + (self.nextPointOffset.y * -1)) * -1)
        else:
          # Colition Bottom Left DEBUG
          self.nextPointOffset = Point(self.nextPointOffset.x * -1, self.nextPointOffset.y * -1)
          self.actualAngle = (math.atan((float(self.points[-1].y) - float(self.points[-2].y)) / (float(self.points[-1].x) - float(self.points[-2].x))) / math.pi) * float(180)
          self.flag_F = 1
          return Point((self.points[-1].x + (self.nextPointOffset.x * -1)) * -1, self.areaSizeY - ((self.points[-1].y + (self.nextPointOffset.y * -1)) - self.areaSizeY))
    else:
      if ((self.points[-1].x + self.nextPointOffset.x) >= 0):
        if ((self.points[-1].y + self.nextPointOffset.y) <= self.areaSizeY):
          if ((self.points[-1].y + self.nextPointOffset.y) >= 0):
            # Colition Right DONE
            self.nextPointOffset = Point(self.nextPointOffset.x * -1, self.nextPointOffset.y)
            self.actualAngle = (math.atan((float(self.points[-1].y) - float(self.points[-2].y)) / (float(self.points[-1].x) - float(self.points[-2].x))) / math.pi) * float(180)
            self.flag_G = 1
            return Point(self.areaSizeX - ((self.points[-1].x + (self.nextPointOffset.x * -1)) - self.areaSizeX), self.points[-1].y + self.nextPointOffset.y)
          else:
            # Colition Top Right DEBUG
            self.nextPointOffset = Point(self.nextPointOffset.x * -1, self.nextPointOffset.y * -1)
            self.actualAngle = (math.atan((float(self.points[-1].y) - float(self.points[-2].y)) / (float(self.points[-1].x) - float(self.points[-2].x))) / math.pi) * float(180)
            self.flag_H = 1
            return Point(self.areaSizeX - ((self.points[-1].x + (self.nextPointOffset.x * -1)) - self.areaSizeX), (self.points[-1].y + (self.nextPointOffset.y * -1)) * -1)
        else:
          # Colition Bottom Right TODO
          self.nextPointOffset = Point(self.nextPointOffset.x * -1, self.nextPointOffset.y * -1)
          self.actualAngle = (math.atan((float(self.points[-1].y) - float(self.points[-2].y)) / (float(self.points[-1].x) - float(self.points[-2].x))) / math.pi) * float(180)
          self.flag_I = 1
          return Point(self.areaSizeX - ((self.points[-1].x + (self.nextPointOffset.x * -1)) - self.areaSizeX), self.areaSizeY - ((self.points[-1].y + (self.nextPointOffset.y * -1)) - self.areaSizeY))
    self.flag_J = 1
    return Point(0, 0)


   # function to calculate new point
  def calcAndAddNextPoint(self) -> Point:
    if ((self.points[-1].x + self.nextPointOffset.x) <= self.areaSizeX):
      if ((self.points[-1].x + self.nextPointOffset.x) >= 0):
        if ((self.points[-1].y + self.nextPointOffset.y) <= self.areaSizeY):
          if ((self.points[-1].y + self.nextPointOffset.y) >= 0):
            # Normal DONE
            self.points.append(Point(self.points[-1].x + self.nextPointOffset.x, self.points[-1].y + self.nextPointOffset.y))
            self.actualAngle = (math.atan((float(self.points[-1].y) - float(self.points[-2].y)) / (float(self.points[-1].x) - float(self.points[-2].x))) / math.pi) * float(180)
            self.flag_A = 1
            return self.points[-1]
          else:
            # Colition Top DONE
            self.nextPointOffset = Point(self.nextPointOffset.x, self.nextPointOffset.y * -1)
            self.points.append(Point(self.points[-1].x + self.nextPointOffset.x, (self.points[-1].y + (self.nextPointOffset.y * -1)) * -1))
            self.actualAngle = (math.atan((float(self.points[-1].y) - float(self.points[-2].y)) / (float(self.points[-1].x) - float(self.points[-2].x))) / math.pi) * float(180)
            self.flag_B = 1
            return self.points[-1]
        else:
          # Colition Bottom DONE
          self.nextPointOffset = Point(self.nextPointOffset.x, self.nextPointOffset.y * -1)
          self.points.append(Point(self.points[-1].x + self.nextPointOffset.x, self.areaSizeY - ((self.points[-1].y + (self.nextPointOffset.y * -1)) - self.areaSizeY)))
          self.actualAngle = (math.atan((float(self.points[-1].y) - float(self.points[-2].y)) / (float(self.points[-1].x) - float(self.points[-2].x))) / math.pi) * float(180)
          self.flag_C = 1
          return self.points[-1]
      else:
        if ((self.points[-1].y + self.nextPointOffset.y) <= self.areaSizeY):
          if ((self.points[-1].y + self.nextPointOffset.y) >= 0):
            # Colition Left Done
            self.nextPointOffset = Point(self.nextPointOffset.x * -1, self.nextPointOffset.y)
            self.points.append(Point((self.points[-1].x + (self.nextPointOffset.x * -1)) * -1, self.points[-1].y + self.nextPointOffset.y))
            self.actualAngle = (math.atan((float(self.points[-1].y) - float(self.points[-2].y)) / (float(self.points[-1].x) - float(self.points[-2].x))) / math.pi) * float(180)
            self.flag_D = 1
            return self.points[-1]
          else:
            # Colition Top Left DONE
            self.nextPointOffset = Point(self.nextPointOffset.x * -1, self.nextPointOffset.y * -1)
            self.points.append(Point((self.points[-1].x + (self.nextPointOffset.x * -1)) * -1, (self.points[-1].y + (self.nextPointOffset.y * -1)) * -1))
            self.actualAngle = (math.atan((float(self.points[-1].y) - float(self.points[-2].y)) / (float(self.points[-1].x) - float(self.points[-2].x))) / math.pi) * float(180)
            self.flag_E = 1
            return self.points[-1]
        else:
          # Colition Bottom Left DEBUG
          self.nextPointOffset = Point(self.nextPointOffset.x * -1, self.nextPointOffset.y * -1)
          self.points.append(Point((self.points[-1].x + (self.nextPointOffset.x * -1)) * -1, self.areaSizeY - ((self.points[-1].y + (self.nextPointOffset.y * -1)) - self.areaSizeY)))
          self.actualAngle = (math.atan((float(self.points[-1].y) - float(self.points[-2].y)) / (float(self.points[-1].x) - float(self.points[-2].x))) / math.pi) * float(180)
          self.flag_F = 1
          return self.points[-1]
    else:
      if ((self.points[-1].x + self.nextPointOffset.x) >= 0):
        if ((self.points[-1].y + self.nextPointOffset.y) <= self.areaSizeY):
          if ((self.points[-1].y + self.nextPointOffset.y) >= 0):
            # Colition Right DONE
            self.nextPointOffset = Point(self.nextPointOffset.x * -1, self.nextPointOffset.y)
            self.points.append(Point(self.areaSizeX - ((self.points[-1].x + (self.nextPointOffset.x * -1)) - self.areaSizeX), self.points[-1].y + self.nextPointOffset.y))
            self.actualAngle = (math.atan((float(self.points[-1].y) - float(self.points[-2].y)) / (float(self.points[-1].x) - float(self.points[-2].x))) / math.pi) * float(180)
            self.flag_G = 1
            return self.points[-1]
          else:
            # Colition Top Right DEBUG
            self.nextPointOffset = Point(self.nextPointOffset.x * -1, self.nextPointOffset.y * -1)
            self.points.append(Point(self.areaSizeX - ((self.points[-1].x + (self.nextPointOffset.x * -1)) - self.areaSizeX), (self.points[-1].y + (self.nextPointOffset.y * -1)) * -1))
            self.actualAngle = (math.atan((float(self.points[-1].y) - float(self.points[-2].y)) / (float(self.points[-1].x) - float(self.points[-2].x))) / math.pi) * float(180)
            self.flag_H = 1
            return self.points[-1]
        else:
          # Colition Bottom Right TODO
          self.nextPointOffset = Point(self.nextPointOffset.x * -1, self.nextPointOffset.y * -1)
          self.points.append(Point(self.areaSizeX - ((self.points[-1].x + (self.nextPointOffset.x * -1)) - self.areaSizeX), self.areaSizeY - ((self.points[-1].y + (self.nextPointOffset.y * -1)) - self.areaSizeY)))
          self.actualAngle = (math.atan((float(self.points[-1].y) - float(self.points[-2].y)) / (float(self.points[-1].x) - float(self.points[-2].x))) / math.pi) * float(180)
          self.flag_I = 1
          return self.points[-1]
    self.flag_J = 1
    return Point(0, 0)

  def calcAndAddNextPoints(self, pointsToCalc) -> Point:
    result = Point(0, 0)
    for i in range(pointsToCalc):
      result = self.calcAndAddNextPoint()
    return result
  
  def printFlags(self) -> None:
    print("__________")
    print(str(self.flag_A) + str(self.flag_B) + str(self.flag_C) + str(self.flag_D) + str(self.flag_E) + str(self.flag_F) + str(self.flag_G) + str(self.flag_H) + str(self.flag_I) + str(self.flag_J))
    print("¯¯¯¯¯¯¯¯¯¯")

  def __init__(self, startPointX, startPointY, endPointX, endPointY, areaSizeX, areaSizeY, timeMilliseconds, invertAxisY) -> None:
    self.startPointX = startPointX
    self.startPointY = startPointY
    self.endPointX = endPointX
    self.endPointY = endPointY
    self.areaSizeX = areaSizeX
    self.areaSizeY = areaSizeY
    self.timeMilliseconds = timeMilliseconds

    self.initialAngle = (math.atan((float(endPointY) - float(startPointY)) / (float(endPointX) - float(startPointX))) / math.pi) * float(180)

    if (startPointX > endPointX):
      self.initialAngle += 180
    elif (startPointY > endPointY and startPointX <= endPointX):
      self.initialAngle += 360

    self.actualAngle = self.initialAngle
    
    self.speed = math.sqrt(math.pow(abs(startPointX) - abs(endPointX), 2) + math.pow(abs(startPointY) - abs(endPointY), 2)) / timeMilliseconds

    self.points = [Point(endPointX, endPointY)]

    self.nextPointOffset = Point(endPointX - startPointX, endPointY - startPointY)
    print("Next Point Offset: [X=" + str(self.nextPointOffset.x) + " ,Y=" + str(self.nextPointOffset.y) + "]")
    self.nextPointOffset = Point(self.nextPointOffset.x / self.speed, self.nextPointOffset.y / self.speed)
    print("Next Point Offset: [X=" + str(self.nextPointOffset.x) + " ,Y=" + str(self.nextPointOffset.y) + "]")

  def print(self) -> None:
    print("Area: [X=" + str(self.areaSizeX) + " ,Y=" + str(self.areaSizeY) + "]")
    print("Time Milliseconds: " + str(self.timeMilliseconds))
    print("Speed: " + str(self.speed))
    print("Initial Angle: " + str(self.initialAngle))
    print("Actual Angle: " + str(self.actualAngle))
    print("Points Count: " + str(len(self.points)))
    if len(self.points) > 6:
      i = len(self.points)
      print(" Point[" + str(0) + "]: [X=" + str(self.points[0].x) + " ,Y=" + str(self.points[0].y) + "]")
      print(" Point[" + str(1) + "]: [X=" + str(self.points[1].x) + " ,Y=" + str(self.points[2].y) + "]")
      print(" Point[" + str(2) + "]: [X=" + str(self.points[2].x) + " ,Y=" + str(self.points[3].y) + "]")
      print(" ...")
      print(" Point[" + str(i-3) + "]: [X=" + str(self.points[i-3].x) + " ,Y=" + str(self.points[i-3].y) + "]")
      print(" Point[" + str(i-2) + "]: [X=" + str(self.points[i-2].x) + " ,Y=" + str(self.points[i-2].y) + "]")
      print(" Point[" + str(i-1) + "]: [X=" + str(self.points[i-1].x) + " ,Y=" + str(self.points[i-1].y) + "]")
    else:
      for i in range(len(self.points)):
        print(" Point[" + str(i) + "]: [X=" + str(self.points[i].x) + " ,Y=" + str(self.points[i].y) + "]")
    print()

  def printAllPoints(self) -> None:
    print("Area: [X=" + str(self.areaSizeX) + " ,Y=" + str(self.areaSizeY) + "]")
    print("Time Milliseconds: " + str(self.timeMilliseconds))
    print("Speed: " + str(self.speed))
    print("Initial Angle: " + str(self.initialAngle))
    print("Actual Angle: " + str(self.actualAngle))
    print("Points Count: " + str(len(self.points)))
    for i in range(len(self.points)):
        print(" Point[" + str(i) + "]: [X=" + str(self.points[i].x) + " ,Y=" + str(self.points[i].y) + "]")
    print()

  # To Do
  def testQuality(self):
    gc.enable()
    equal_point = True
    i = 3
    self.points = [self.points[0]]
    self.calcAndAddNextPoint()
    self.calcAndAddNextPoint()
    while (equal_point):
      self.points[2] = self.calcAndAddNextPoint()
      i = i +1
      equal_point = not (self.points[1].isEqual(self.points[2]) and self.initialAngle == self.actualAngle)
      if (i % 1000000 == 0):
        print("Test Quality Vector Progress: " + str(i))
        
    print("Test Quality Done!")


# StartPoint = [X=159, Y=72]
# EndPoint = [X=258, Y=135]
# Area = [X=1906, Y=977]
# TimeMilliseconds = 126.61

# InitialAngle = 32.4711922908485
# Speed = 0.926827606773933

# ActualAngle = 32.4711922908485
# ActualPoint = [X=258, Y=135]

# NextPount = [X=106.815980961762, Y=67.9738060665759]

# FAIL TEST
# v2 = Vector(159, 72, 258, 135, 1906, 977, 126.61, False)
# v2.calcAndAddNextPoints(500)
# v2.print()

# FAIL TEST
# v2 = Vector(190, 214, 233, 181, 1906, 977, 230.1746, False)
# v2.calcAndAddNextPoints(4)
# v2.print()


# v2 = Vector(284, 174, 428, 213, 1906, 977, 1209.7877, False)
# v2.calcAndAddNextPoints(4)
# v2.print()


# {
# StartP={X=843, Y=142}, 
# EndP={X=653, Y=147}, 
# ActualP={X=653, Y=147}, 
# NextPO={X=-493.320712142316, Y=12.9821240037451}, 
# Width=1906, 
# Height=977, 
# TimeMS=493.4915 
# InitialAngle=178.492564241225, 
# Speed=0.38514498849014}
# v2 = Vector(843, 142, 653, 147, 1906, 977, 493.4915, False)
# v2.calcAndAddNextPoint()
# v2.print()

v2 = Vector(0, 0, 2, 2, 10, 20, 1.4142135623730951, False)
# v2.calcAndAddNextPoints(30)
# v2.printAllPoints()

# v2 = Vector(0, 0, 1.3, 0.7, 10, 20, 1, False)
# v2 = Vector(843, 142, 653, 147, 1906, 977, 493.4915, False)
# v2.calcAndAddNextPoints(3000)
# v2.printFlags()

# StartP={X=123, Y=71}
# EndP={X=171, Y=127}
# ActualP={X=171, Y=127}
# NextPO={X=289.744033707319, Y=338.034705991873}
# Width=1906, Height=977
# TimeMS=445.218
# InitialAngle=49.3987053549955
# Speed=0.165663462973966}
# v2 = Vector(123, 71, 171, 127, 1906, 977, 445.218, False)
# v2.calcAndAddNextPoints(5)
v2.testQuality()
v2.print()
# v2.printFlags()