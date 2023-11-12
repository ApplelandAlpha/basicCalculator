import math
import time
#Version v1.0.1
#Program that will help in mathematics
print(
  "Hello, I am a basic mathematical problem solver. You can give me math problems to solve in mutliple branches in math like arithmetic and geometry. \nTo see all the things I can do after I ask \"What can I do for you?\", type \"all questions\"."
)

#arithmetic functions
def addition(num1, num2):
  print("The result is: ")
  print(int(num1) + int(num2))

def subtraction(num1, num2):
  print("The result is: ")
  print(int(num1) - int(num2))

def division(num1, num2):
  print("The result is: ")
  print(int(num1) / int(num2))

def multiplication(num1, num2):
  print("The result is: ")
  print(int(num1) * int(num2))

#geometry functions
def circArea(rad):
  area = math.pi * rad**2
  print("The area of the circle is " + str(area))

def squareArea(side1, side2):
  area = side1 * side2
  print("The area of the square/rectangle is " + str(area))

def triangleArea(height, base):
  step1 = base * height
  area = step1 / 2
  print("The area of the triangle is " + str(area))

def trapezoidArea (height, base1, base2):
  step1 = base1 + base2
  step2 = step1 / 2
  area = step2 * height
  print("The area of the trapezoid is " + str(area))

  
time.sleep(1)
#chatbot questions
question = input("\nSo, what can I do for you?: ")
question = question.lower()

#introducing itself
if question == "all questions":
  print("\"What can you do?\"\n\"Math\"")
elif question == "what can you do?":
  print("As of now, I am only able to solve problems on arithmetic (elementary math) and 2D geometry for some shapes.")

#mathematical commands
elif question == "math":
  mathBranch = input("\nOk, would you like me to solve an arithemtic, geometry question?: ")
  mathBranch = mathBranch.lower()
  if mathBranch == "arithmetic":
    oprtn = input("\nSure, do you want to add, subtract, multiply, or divide?: ")
    oprtn = oprtn.lower()
    if oprtn == "add":
      numAdd1 = input("What is your first number?: ")
      numAdd2 = input("What is your second number?: ")
      addition(numAdd1, numAdd2)
    elif oprtn == "subtract" or oprtn == "sub":
      numSub1 = input("What is your first number?: ")
      numSub2 = input("What is your second number?: ")
      subtraction(numSub1, numSub2)
    elif oprtn == "divide" or oprtn == "div":
      numDiv1 = input("What is your first number?: ")
      numDiv2 = input("What is your second number?: ")
      division(numDiv1, numDiv2)
    elif oprtn == "multiply" or oprtn == "mult":
      numMult1 = input("What is your first number?: ")
      numMult2 = input("What is your second number?: ")
      multiplication(numMult1, numMult2)
      
  elif mathBranch == "geometry":
    mathProblem = input("\nOk, here's what I can do:\n•Solve the area of a circle \n•Solve the area of a rectangle or square \n•Solve the area of a triangle \n•Solve the area of a trapezoid \n What shape would you like me to solve the area for?: ")
    if mathProblem == "circle":
      radius = float(input("\nWhat is the radius of the circle?: "))
      circArea(radius)
    if mathProblem == "square" or mathProblem == "rectangle":
      sideLen1 = float(input("\nWhat is the length of the first side?: "))
      sideLen2 = float(input("What is the length of the second side?: "))
      squareArea(sideLen1, sideLen2)
    if mathProblem == "triangle":
      height = float(input("\nWhat is the height of the triangle?: "))
      base = float(input("\nWhat is the base of the triangle?: "))
      triangleArea(height, base)
    if mathProblem == "trapezoid":
      h = float(input("\nWhat is the height of the trapezoid?: "))
      b1 = float(input("\nWhat is the length of the first base?: "))
      b2 = float(input("\nWhat is the length of the second base?: "))
      trapezoidArea(h, b1, b2)

#End of program code