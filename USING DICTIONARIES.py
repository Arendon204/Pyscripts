﻿1/9 


2/9


zodiac_elements = {"water": ["Cancer", "Scorpio", "Pisces"], "fire": ["Aries", "Leo", "Sagittarius"], "earth": ["Taurus", "Virgo", "Capricorn"], "air":["Gemini", "Libra", "Aquarius"]}




print(zodiac_elements["earth"])
print(zodiac_elements["fire"])




3/9


zodiac_elements = {"water": ["Cancer", "Scorpio", "Pisces"], "fire": ["Aries", "Leo", "Sagittarius"], "earth": ["Taurus", "Virgo", "Capricorn"], "air":["Gemini", "Libra", "Aquarius"]}


zodiac_elements["energy"] = "Not a Zodiac element"


KeyError = "energy"


if KeyError in zodiac_elements:
  print(zodiac_elements["energy"])






4/9






user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}


tc_id = user_ids.get("teraCoder", 0)


print(tc_id)


stack_id = user_ids.get("superStackSmash", 100000)


print(stack_)










5/9




available_items = {"health potion": 10, "cake of the cure": 5, "green elixir": 20, "strength sandwich": 25, "stamina grains": 15, "power stew": 30}




health_points = 20




health_points += available_items.pop("stamina grains", 0)


health_points += available_items.pop("power stew", 0)




health_points += available_items.pop("mystic bread", 0)


print(health_points)


print(available_items)








6/9




user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}




num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}






users = user_ids.keys()


lessons = num_exercises.keys()


print(users)


print(lessons)
7/9


num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}




total_exercises = 0




for num in num_exercises.values():
  total_exercises += num


print(total_exercises)




8/9


pct_women_in_occupation = {"CEO": 28, "Engineering Manager": 9, "Pharmacist": 58, "Physician": 40, "Lawyer": 37, "Aerospace Engineer": 9}




for occupation, woman in pct_women_in_occupation.items():
  print("Women make up " + str(woman) + " percent of "+ occupation +"s.")












































9/9




tarot = { 1:        "The Magician", 2:        "The High Priestess", 3:        "The Empress", 4:        "The Emperor", 5:        "The Hierophant", 6:        "The Lovers", 7:        "The Chariot", 8:        "Strength", 9:        "The Hermit", 10:        "Wheel of Fortune", 11:        "Justice", 12:        "The Hanged Man", 13:        "Death", 14:        "Temperance", 15:        "The Devil", 16:        "The Tower", 17:        "The Star", 18:        "The Moon", 19:        "The Sun", 20:        "Judgement", 21:        "The World", 22: "The Fool"}


spread = {}


spread["past"] = tarot.pop(13)
spread["present"] = tarot.pop(22)
print(spread)




spread["future"] = tarot.pop(10)


for key, value in spread.items():
  print("Your " + key + " is the " + value + " card.")