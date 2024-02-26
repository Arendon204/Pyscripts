# Uncomment this when you reach the "Use the Force" section
train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1


# Write your code below: 

def f_to_c(f_temp):
   return (32 - f_temp) * 5/9
  

   f100_in_celsius = f_to_c(100) 
  

def c_to_f(c_temp):
  return(32 + c_temp) * 5/9  

  c0_in_fahrenheit = c_to_f(0)

def get_force(mass, acceleration):
  return mass * acceleration 

train_force = get_force(train_mass, train_acceleration)

print(train_force)