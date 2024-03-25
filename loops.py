13/13


# Your code below:


single_digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


squares = []


for digits in single_digits:
  print(digits)
  squares.append(digits**2)


print(squares)




cubes = [ digits ** 3 for digits in single_digits ]
print(cubes)




12/13


heights = [161, 164, 156, 144, 158, 170, 163, 163, 157]




can_ride_coaster = [height for height in heights if height > 161]


print(can_ride_coaster)
  




11/13


grades = [90, 88, 62, 76, 74, 89, 48, 57]


scaled_grades = [grade + 10 for grade in grades]


print(scaled_grades)






10/13




sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]




scoops_sold = 0


for location in sales_data:
  print(location)
  for element in location:
    scoops_sold += element
  
print(scoops_sold)




9/13


ages = [12, 38, 34, 26, 21, 19, 67, 41, 17]


for i in ages:
  if i < 21:
    continue
  print(i)






8/13


dog_breeds_available_for_adoption = ["french_bulldog", "dalmatian", "shihtzu", "poodle", "collie"]
dog_breed_I_want = "dalmatian"


for dog_breed in dog_breeds_available_for_adoption:
  print(dog_breed)
  if dog_breed == dog_breed_I_want:
    break


print("They have the dog I want!")






7/13




students_period_A = ["Alex", "Briana", "Cheri", "Daniele"]
students_period_B = ["Dora", "Minerva", "Alexa", "Obie"]


for student in students_period_A:
  students_period_B.append(student)
  print(student)






6/13




python_topics = ["variables", "control flow", "loops", "modules", "classes"]


#Your code below: 
length = len(python_topics)


index = 0


while index < length:
  print("I am learning about " + python_topics[index])
  index += 1






5/13








#/While Loop Walkthrough
#count = 0
#print("Starting While Loop")
#while count <= 3:
  # Loop Body
  # Print if the condition is still true
#  print("Loop Iteration - count <= 3 is still true")
  # Print the current value of count 
#  print("Count is currently " + str(count))
  # Increment count
#  count += 1
#  print(" ----- ")
#print("While Loop ended")


# Your code below: 


countdown = 10


while countdown >= 0: 


  print(countdown)
  countdown -= 1


print("We have liftoff!")


  




4/13






promise = "I will finish the python loops module!"


for i in range(5):
  print(promise)








3/13








board_games = ["Settlers of Catan", "Carcassone", "Power Grid", "Agricola", "Scrabble"]


sport_games = ["football", "hockey", "baseball", "cricket"]


for game in board_games:
  print(game)


for i in sport_games:
  print(i)






2/13




# Write 10 print() statements below! 
print("This can be so much easier with loops!")
print("This can be so much easier with loops!")
print("This can be so much easier with loops!")
print("This can be so much easier with loops!")
print("This can be so much easier with loops!")
print("This can be so much easier with loops!")
print("This can be so much easier with loops!")
print("This can be so much easier with loops!")
print("This can be so much easier with loops!")
print("This can be so much easier with loops!")






1/13