def main():
  # MAIN REPL CODE
  import re 

  run = True
  print("REPL Initialized")

  print("This is the Homework REPL \n Input statements using the Syntax for calculations to common mathematical problems")

  print("//*//*//*//*//*//*//*//*//*//*// \n \n")

  while run == True:
    
    x = input('>> ')

    if x == "EXIT":
      run = False
      print("END OF PROGRAM")
      break

    tokens = re.split("\s", x)

    if tokens[0] != "GIVE":
      print("INVALID INPUT")
      continue
    if tokens[1] == "MIDPOINT":
      tempA = tokens[3].replace("(", "")
      tempB = tempA.replace(")", "")
      x_split = re.split(",", tempB)

      temp2A = tokens[5].replace("(", "")
      temp2B = temp2A.replace(")", "")
      y_split = re.split(",", temp2B)
    
      midpoint(float(x_split[0]), float(y_split[0]), float(x_split[1]), float(y_split[1]))
      

    if tokens[1] == "DISTANCE":
      tempA = tokens[3].replace("(", "")
      tempB = tempA.replace(")", "")
      x_split = re.split(",", tempB)

      temp2A = tokens[5].replace("(", "")
      temp2B = temp2A.replace(")", "")
      y_split = re.split(",", temp2B)
  
      distance(float(x_split[0]), float(y_split[0]), float(x_split[1]), float(y_split[1]))

      
    if tokens[1] == "SLOPE":
      tempA = tokens[3].replace("(", "")
      tempB = tempA.replace(")", "")
      x_split = re.split(",", tempB)

      temp2A = tokens[5].replace("(", "")
      temp2B = temp2A.replace(")", "")
      y_split = re.split(",", temp2B)
    
      slope(float(x_split[0]), float(y_split[0]), float(x_split[1]), float(y_split[1]))

    if tokens[1] == "SURFACEAREA":

      if tokens[3] == "CYLINDER":
        radius = tokens[7]
        length = tokens[11]
        if float(radius) > 0 and float(length) > 0:
          surfaceArea_cylinder(float(radius),float(length))
        else: 
          print("INVALID INPUT")
      
      if tokens[3] == "CONE":
        radius = tokens[7]
        length = tokens[11]
        if float(radius) > 0 and float(length) > 0:
          surfaceArea_cone(float(radius),float(length))
        else: 
          print("INVALID INPUT")
          
      if tokens[3] == "CUBE":
        length = tokens[7]
        if float(length) > 0:
          surfaceArea_cube(float(length))
        else: 
          print("INVALID INPUT")

      if tokens[3] == "SPHERE":
        radius = tokens[7]
        if float(radius) > 0:
          surfaceArea_sphere(float(radius))
        else: 
          print("INVALID INPUT")

    
    if tokens[1] == "AREA":

      if tokens[3] == "SQUARE":
        length = tokens[7]
        if float(length) > 0:
          area_of_square(float(length))
        else: 
          print("INVALID INPUT")

      if tokens[3] == "CIRCLE":
        radius = tokens[7]
        if float(radius) > 0:
          area_of_circle(float(radius))
        else: 
          print("INVALID INPUT")
      
      if tokens[3] == "RECTANGLE":
        length = tokens[7]
        width = tokens[11]
        if float(length) > 0 and float(width) > 0:
          area_of_rectangle(float(length),float(width))
        else: 
          print("INVALID INPUT")

      if tokens[3] == "TRIANGLE":
        base = tokens[7]
        height = tokens[11]
        if float(base) > 0 and float(height) > 0:
          area_of_traingle(float(base),float(height))
        else: 
          print("INVALID INPUT")

      if tokens[3] == "TRAPEZOID":
        base1 = tokens[7]
        base2 = tokens[11]
        height = tokens[15]
        if float(base1) > 0 and float(base2) > 0 and float(height) > 0:
          area_of_trapezoid(float(base1),float(base2),float(height))
        else: 
          print("INVALID INPUT")

    if tokens[1] == "VOLUME":
      if tokens[3] == "CUBE":
        if (float(tokens[7])) > 0:
          cube_Volume((float(tokens[7])))
        else: 
          print("INVALID INPUT")
        
      if tokens[3] == "CONE":
        if (float(tokens[7]) > 0 and (float(tokens[11])) > 0):
            cone_Volume((float(tokens[7])), (float(tokens[11])))
        else: 
          print("INVALID INPUT")
          
      if tokens[3] == "CYLINDER":
        if (float(tokens[7]) > 0 and (float(tokens[11])) > 0):
            cylinder_Volume((float(tokens[7])), (float(tokens[11])))
        else: 
          print("INVALID INPUT")
          
      if tokens[3] == "SPHERE":
        if (float(tokens[7])) > 0:
          sphere_Volume((float(tokens[7])))
        else: 
          print("INVALID INPUT")

"""Helper Functions"""

import math

# midpoint volume
def midpoint(x1, x2, y1, y2):
  x = (x1+x2)/2
  y = (y1+y2)/2
  return print("Midpoint is: ("+str(x)+","+str(y)+")")

# surface area cube
def surfaceArea_cube(s):
  return print("Surface Area of Cube is: " + str(6*s*s))

# surface area cylinder
def surfaceArea_cylinder(r,h):
  return print("Surface Area of Cube is: " + str(2*math.pi*r*h + (2*math.pi*r*r)))

#surface area cone
def surfaceArea_cone(r,l):
  return print("Surface Area of Cone is: " + str((1/3) * math.pi*r*r*l))

# surface area sphere
def surfaceArea_sphere(r):
  return print("Surface Area of Sphere is: " + str((4/3) * math.pi*r*r*r))

# distance formula
def distance(x1, y1, x2, y2):
  return print("Distance is " + str(math.sqrt((x1-x2)**2+(y1-y2)**2)))


# volume cube
def cube_Volume(side):
  return print("Volume of Cube: " + str(math.pow(side,3)))


# volume cylinder
def cylinder_Volume(r, h):
  return print("Volume of Cylinder: " + str((math.pi *(r**2)*h)))


# cone volume
def cone_Volume(r, h):
  return print("Volume of Cone: " + str(math.pi * (r**2) * (h/3)))

# sphere volume
def sphere_Volume(r):
  return print("Volume of sphere: " + str((4/3)*math.pi*(math.pow(r,3))))

# slope formula
def slope(x1,y1,x2,y2):
  return print("The slope is: " + str((y2-y1)/(x2-x1)))

# area square
def area_of_square(s) -> float:
    """Return the area of a square."""
    area = s**2
    return print("Area is " + str(area))

# area rectangle
def area_of_rectangle(l, w) -> float:
    """Return the area of a rectangle."""
    area = l * w
    return print("Area is " + str(area))

# area circle
def area_of_circle(r) -> float:
    """Return the area of a circle."""
    area = math.pi * r ** 2
    return print("Area is " + str(area))

# area triangle
def area_of_triangle(b, h) -> float:
    """Return the area of a triangle."""
    area = 0.5 * b * h
    return print("Area is " + str(area))

# area trapezoid
def area_of_trapezoid(b_1, b_2, h) -> float:
    """Return the area of a trapezoid."""
    area = 0.5 * h * (b_1 + b_2)
    return print("Area is " + str(area))

main()
