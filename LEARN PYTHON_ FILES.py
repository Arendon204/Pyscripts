1/13




with open("welcome.txt") as text_file:


  text_data = text_file.read()


print(text_data)






2/13




with open("how_many_lines.txt") as lines_doc:


  for line in lines_doc.readlines():
    print(line)






3/13


with open("just_the_first.txt") as first_line_doc:


  first_line = first_line_doc.readline()
  print(first_line)






4/13




with open("bad_bands.txt", "w") as bad_bands_doc:
  bad_bands_doc.write("bad_bands")


















5/13


#We’ve got a file, cool_dogs.txt, filled with all the cool dogs we know. Somehow while compiling this list we forgot about one very cool dog. Let’s fix that problem by adding him to our cool_dogs.txt.


#Open up our file cool_dogs.txt in append-mode and assign it to the file object cool_dogs_file.


with open("cool_dogs.txt", "a") as cool_dogs_file:


  cool_dogs_file.write("“Air Buddy\n”")








6/13


with open('fun_file.txt') as close_this_file: 


setup = close_this_file.readline()
punchline = close_this_file.readline()


print(setup)






7/13




with open("logger.csv") as log_csv_file:
  print(log_csv_file.read())




























8/13


import csv




with open("cool_csv.csv") as cool_csv_file:
  cool_csv_dict = csv.DictReader(cool_csv_file)


  for fact in cool_csv_dict:
    print(fact["Cool Fact"])






9/13






import csv






with open("books.csv") as books_csv:
  books_reader = csv.DictReader(books_csv, delimiter='@')




  isbn_list = [book['ISBN'] for book in books_reader]


  #Create a list called isbn_list, iterate through books_reader to get the ISBN number of every book in the CSV file. Use the ['ISBN'] key for the dictionary objects passed to it.


  #To create the isbn_list, you can initialize an empty list. Then, inside a loop that goes through each row in books_reader, you can append the ISBN number from each row to the list. Remember, you can access the ISBN number from a row using the ['ISBN'] key.






10/13




import csv




access_log = [{'time': '08:39:37', 'limit': 844404, 'address': '1.227.124.181'}, {'time': '13:13:35', 'limit': 543871, 'address': '198.51.139.193'}, {'time': '19:40:45', 'limit': 3021, 'address': '172.1.254.208'}, {'time': '18:57:16', 'limit': 67031769, 'address': '172.58.247.219'}, {'time': '21:17:13', 'limit': 9083, 'address': '124.144.20.113'}, {'time': '23:34:17', 'limit': 65913, 'address': '203.236.149.220'}, {'time': '13:58:05', 'limit': 1541474, 'address': '192.52.206.76'}, {'time': '10:52:00', 'limit': 11465607, 'address': '104.47.149.93'}, {'time': '14:56:12', 'limit': 109, 'address': '192.31.185.7'}, {'time': '18:56:35', 'limit': 6207, 'address': '2.228.164.197'}]
fields = ['time', 'address', 'limit']






with open("logger.csv", "w") as logger_csv:


  log_writer = csv.DictWriter(logger_csv,fieldnames = fields )


  log_writer.writeheader()


  for log in access_log:
    log_writer.writerow(log)












  
11/13




import json




with open('message.json') as message_json:
  message = json.load(message_json)
  print(message[('text')])


  #Pass the JSON file object as an argument to json.load() and save the resulting Python dictionary as message.
                
________________


12/13


import json


data_payload = [
  {'interesting message': 'What is JSON? A web application\'s little pile of secrets.',
   'follow up': 'But enough talk!'}
]




with open('data.json', 'w') as data_json:
  json.dump(data_payload, data_json)




#Call json.dump() with data_payload and data_json to convert our data to JSON and then save it to the file data.json.




13/13


Lesson finished