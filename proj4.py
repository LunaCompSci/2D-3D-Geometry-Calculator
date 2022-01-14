#Christina Nguyen, 1/30/21,does geometic calculations based on side and radius
import math
import p4geom

global DASH_NUM, LABEL_FMT, NUM_FMT
DASH_NUM = 44
LABEL_FMT = "15s"
NUM_FMT = ".2f" 

def main():
   size, unit = getInput()
   displaySquareResults(size, unit)
   displayCubeResults(size, unit)
   displayCircleResults(size, unit)
   displaySphereResults(size, unit)
    
def getInput():
    size = float(input("Enter size for side and radius: ")) 
    unit = input("Enter unit of measure, e.g inches: ")
    return size, unit

def displaySquareResults(size, unit):
    print("-" * DASH_NUM, "\nSquare Calculations\n", "-" * DASH_NUM, sep = '')
    squarePerimResult = p4geom.squarePerim(size)
    print(format("Perimeter:", LABEL_FMT), format(squarePerimResult, NUM_FMT), "linear", unit)
    squareAreaResult = p4geom.squareArea(size)
    print(format("Area:", LABEL_FMT), format(squareAreaResult, NUM_FMT), "square", unit)
      
def displayCubeResults(size, unit):
    print("-" * DASH_NUM, "\nCube Calculations\n", "-" * DASH_NUM, sep = '')
    cubeVolumeResult = p4geom.cubeVolume(size)
    print(format("Volume:", LABEL_FMT), format(cubeVolumeResult, NUM_FMT), "cubic", unit)
    cubeSurfAreaResult = p4geom.cubeSurfArea(size)
    print(format("Surface area:", LABEL_FMT), format(cubeSurfAreaResult, NUM_FMT), "square", unit)
    
def displayCircleResults(size, unit):
    print("-" * DASH_NUM, "\nCircle Calculations\n", "-" * DASH_NUM, sep = '')
    circleCircumResult = p4geom.circleCircum(size)
    print(format("Circumference:", LABEL_FMT), format(circleCircumResult, NUM_FMT), "linear", unit)
    circleAreaResult = p4geom.circleArea(size)
    print(format("Area:", LABEL_FMT), format(circleAreaResult, NUM_FMT), "square", unit)
    
def displaySphereResults(size, unit):
    print("-" * DASH_NUM, "\nSphere Calculations\n", "-" * DASH_NUM, sep = '')
    sphereVolumeResult = p4geom.sphereVolume(size)
    print(format("Volume:\t", LABEL_FMT), format(sphereVolumeResult, NUM_FMT), "cubic", unit)
    sphereSurfAreaResult = p4geom.sphereSurfArea(size)
    print(format("Surface area:", LABEL_FMT), format(sphereSurfAreaResult, NUM_FMT), "square", unit)

main()    

#At one point I was mixing up the ways you import a module and I ended up not adding the "filename." to my function calls.
#For testing I gave the large size: 453415 to see if my code would break. I got an overflow error message. That is something I would like to fix later.
#Another test case I did was I put 453 as the size to see where the overflow limit would be.
#Even though it had 221 digits its output was small enough that I didn't get an overflow number.
#However, when I expand by shell, no second line is necessary and it looks nice. 
#In the future I would like to change my code so the second line lines up with the first digit   
#From this assignment I learned not to mix up the three different ways you can import a module
#I ended up not coding "module." because I thought it wasn't necessary.
#I also learned that the name of my return varible cannot be the same as the function that called it.
#I must have been mixing up it up with something else.
#For my next assignment I won't make those mistakes again.
#I also compared size 4 with my classmates and found I mixed up the order of some numbers and forgot a(). 
