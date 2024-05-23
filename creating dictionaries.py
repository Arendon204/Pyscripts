1/9






sensors =  {"living room": 21, "kitchen": 23, "bedroom": 20, "pantry": 22}
num_cameras = {"backyard": 6,  "garage": 2, "driveway": 1}


print(sensors)




2/9






translations = {"mountain" : "orod", "bread" : "bass", "friend" : "mellon", "horse" : "roch"}


3/9




children = {"von Trapp" : ["Johannes", "Rosmarie", "Eleonore"] , "Corleone" :  ["Sonny", "Fredo", "Michael"]}


4/9


my_empty_dictionary = {}


5/9


animals_in_zoo = {}
animals_in_zoo["zebras"] = 8
animals_in_zoo["monkeys"] = 12
animals_in_zoo["dinosaurs"] = 0
print(animals_in_zoo)


6/9


user_ids = {"teraCoder": 9018293, "proProgrammer": 119238, "theLooper": 138475
, "stringQueen":  85739}


print(user_ids)










7/9










oscar_winners = {"Best Picture": "La La Land", "Best Actor": "Casey Affleck", "Best Actress": "Emma Stone", "Animated Feature": "Zootopia"}


oscar_winners["Supporting Actress"] = "Viola Davis"


oscar_winners["Best Picture"] = "Moonlight"






8/9




drinks = ["espresso", "chai", "decaf", "drip"]
caffeine = [64, 40, 0, 120]




zipped_drinks = zip(drinks, caffeine)




drinks_to_caffeine = {key: value for key, value in zipped_drinks}


































9/9


songs = ["Like a Rolling Stone", "Satisfaction", "Imagine", "What's Going On", "Respect", "Good Vibrations"]
playcounts = [78, 29, 44, 21, 89, 5]


plays = {song:playcount for [song, playcount] in zip(songs, playcounts)}


print(plays)


plays["Respect"] = 94


plays["Purple Haze"] = 1


library = {"The Best Songs": plays, "Sunday Feelings": {}}


print(library)