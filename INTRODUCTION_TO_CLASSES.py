1/14


print(type(5))


my_dict = {}
print(type(my_dict))




my_list = []


print(type(my_list))




2/14


class Facade:
  pass


  #A class is a template for a data type. It describes the kinds of information that class will hold and how a programmer will interact with that data. Define a class using the class keyword. PEP 8 Style Guide for Python Code recommends capitalizing the names of classes to make them easier to identify.




3/14




class Facade:
  pass


facade_1 = Facade()


#Above, we created an object by adding parentheses to the name of the class. We then assigned that new instance to the variable cool_instance for safe-keeping so we can access our instance of CoolClass at a later time.




________________




4/14




class Facade:
  pass


facade_1 = Facade()


facade_1_type = type(facade_1)


print(facade_1_type)






5/14


class Grade:
 minimum_passing  = 65




6/14




class Rules:
  #For now, make the body of your class pass. This will allow your code to run without error.


  def washing_brushes(Rules):
    return "Point bristles towards the basin while washing your brushes."


    #Since we’ve now given this class a method, we can remove the pass that we added in the previous step.


________________




7/14




class Circle:
  pi = 3.14
  def area(self, radius):
    #Since .pi is a class variable, you can access it as an attribute of the class.
    return Circle.pi * radius ** 2




circle = Circle()
#To create an instance of the Circle class, you need to call the class name followed by parentheses. Assign this to the variable circle.




pizza_area = circle.area(12 / 2)
print(pizza_area)
teaching_table_area = circle.area(36 / 2)
print(teaching_table_area)
round_room_area = circle.area(11460 / 2)
print(round_room_area )




8/14


class Circle:
  pi = 3.14
  
  # Add constructor here:
  def __init__(self, diameter):
    self.diameter = diameter
    #Create a circle teaching_table with diameter 36.
    print(f"New circle with diameter: {self.diameter}")


teaching_table = Circle(36)














________________


9/14






class Store:
  pass
alternative_rocks = Store()


isabelles_ices = Store()
  


alternative_rocks.store_name = "Alternative Rocks"
isabelles_ices.store_name = "Isabelle's Ices"


string = "{}{}".format(alternative_rocks.store_name, isabelles_ices.store_name)
print(string)




10/14


can_we_count_it = [{'s': False}, "sassafrass", 18, ["a", "c", "s", "d", "s"]]


for element in can_we_count_it:
  if hasattr(element, "count"):
    print(str(type(element)) + " has the count attribute!")
  else:
    print(str(type(element)) + " does not have the count attribute :(")






________________


11/14


class Circle:
  pi = 3.14
  def __init__(self, diameter):
    print("Creating circle with diameter {d}".format(d=diameter))
    # Add assignment for self.radius here:
    self.radius = diameter / 2 
  def circumference(self):
    return 2 * self.pi * self.radius
    #Define a new method .circumference() for your circle object that takes only one argument, self, and returns the circumference of a circle with the given radius by this formula:




#Define three Circles with three different diameters.
medium_pizza = Circle(12)
teaching_table = Circle(36)
round_room = Circle(11460)


print(medium_pizza.circumference())
print(teaching_table.circumference())
print(round_room.circumference())


#Print out the circumferences of medium_pizza, teaching_table, and round_room.


12/14


print(dir(5))


def this_function_is_an_object(num):
  return "bruh ".format(num)


print(dir(this_function_is_an_object))
 
________________


13/14


class Circle:
  pi = 3.14
  
  def __init__(self, diameter):
    self.radius = diameter / 2
  
  def area(self):
    return self.pi * self.radius ** 2
  
  def circumference(self):
    return self.pi * 2 * self.radius


  def __repr__(self):
    return "Circle with radius {radius}".format(radius=self.radius)
  
  
medium_pizza = Circle(12)
teaching_table = Circle(36)
round_room = Circle(11460)




print(medium_pizza, 
teaching_table, 
round_room )


________________


14/14


class Student:
  def __init__(self, name, year):
    self.name = name
    self.year = year
    self.grades = []
    
  def add_grade(self, grade):
    if type(grade) is Grade:
      self.grades.append(grade)
      #Add an .add_grade() method to Student that takes a parameter, grade.
      #.add_grade() should verify that grade is of type Grade and if so, add it to the Student‘s .grades.
      #If grade isn’t an instance of Grade then .add_grade() should do nothing.


class Grade:
  minimum_passing = 65


  def __init__(self, score):
    self.score = score
    
roger = Student("Roger van der Weyden", 10)
sandro = Student("Sandro Botticelli", 12)
pieter = Student("Pieter Bruegel the Elder", 8)
pieter.add_grade(Grade(100))
#Create a new Grade with a score of 100 and add it to pieter‘s .grades attribute using .add_grade().