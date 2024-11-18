# person = ("Daniel", 23, "Netanya")
# (Name, Age, City) = person

# print(Name)
# print(Age)
# print(City)

# nusted_tuple = ((1, 2, 3),(4, 5, 6))
# print(nusted_tuple[0])

# numbers = (1, 2, 3, 2, 4, 2)
# #print(numbers.count(2))
# print(numbers.index(3))

# student = {
#     "name" : "Daniel",
#     "age" : 23,
#     "grade" : 100
# }
# print(student["name"])
# student.update({"school" : "Sela"})
# student.update({"age" : 40})
# student.pop("grade")
# print(student)

# capitals = {'France': 'Paris', 'Spain': 'Madrid', 'Japan': 'Tokyo'}
# for country, capital in capitals.items():
#     #print(f"The capital of {country} is {capital}.")
#     capital_of_germany = capitals.get('Germany', 'Not Found')
# print("The capital of Germany is:", capital_of_germany)

# Given string
#text = 'kolodko'

# Initialize an empty dictionary to store character counts
#char_count = {}

# Loop through each character in the string
#for char in text:
    # If the character is already in the dictionary, increment its count
    #if char in char_count:
        #char_count[char] += 1
    # If the character is not in the dictionary, add it with a count of 1
    #else:
        #char_count[char] = 1

# Print the resulting dictionary
#print(char_count)

# my_set = {1, 2, 3, 4, 5}
# my_set.add(6)
# my_set.add(3)
# my_set.remove(2)
# print(my_set)

# set_a = {1, 2, 3, 4}
# set_b = {3, 4, 5, 6}
# set_c = set_a.union(set_b)
# set_c = set_a.intersection(set_b)
# set_c = set_a.difference(set_b)
# set_c = set_a.symmetric_difference(set_b)
# print(set_c)

# numbers = [1, 2, 2, 3, 4, 4, 5]
# unique_numbers = list(set(numbers))
# print(unique_numbers)

# set_a = {1, 2, 3}
# set_b = {4, 5, 6}
# if 5 in set_a:
#     print(5)
# else:
#     print("null")

# set = {1, 2, 3}
# set.add(4)
# set.remove(3)
# set.discard(2)
# print(set)

# age = int(input("Please enter your age: "))

# if age >= 18:
#     print("you can drive")
# else:
#     print("your not old enought")
# if age == 16 or 17:
#     print("almost there!")

# number = int(input("Please enter your number: "))
# if number % 2 == 0:
#     print("The number is even.")
# else:
#     print("The number is odd.")

# score = input("Please enter your grade: ")
# if score == "A":
#     print("90-100")
# elif score == "B":
#     print("80-89")
# elif score == "C":
#     print("70-79")
# elif score == "D":
#     print("60-69")
# elif score == "F":
#     print("Below 60")

# number = int(input("Please enter your number: "))
# if number > 0:
#     print("positive")
# elif number < 0:
#     print("negative")
# elif number == 0:
#     print("Zero")

# age = int(input("What is your age? "))
# if age < 18 :
#     print("you get a discount")
# else: 
#     print(" ")
# student = input("Are you a student? ")
# if student == "yes":
#     print("you get a discount")
# elif student == "no":
#     print("L")

# i = 1
# while i < 11:
#   if i % 2 == 0:
#      print(i)
#   i += 1 


# ____________________________________________________________
# from datetime import datetime

# timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")

# with open("Journal.txt", "a") as journal_files:
#        while True:
#            entry = input("Enter your journal entry (or type quit to exit): ").strip()
         
#            if entry.lower() == "quit":
#                print("Exiting. Your entries have been saved")
#                break
        
#            journal_files.write(f"{timestamp} {entry}\n")

# print("Entry logged") 

# f = open("Journal.txt", "r")
# print(f.read())

# number_of_words = 0 
# with open(r"Journal.txt", "r") as file:
#      data = file.read()
    
#      lines = data.split()
    
#      number_of_words += len(lines)

#      lines = len(file.readlines())
# print(str(f"Word Count: {number_of_words}"))
# print(str(f"Line count: {lines}"))
#__________________________________________________________________


# Corrected file path


# number_of_words = 0 
# with open(r"Journal.txt", "r") as file:
#     data = file.read()
    
#     lines = data.split()
    
#     number_of_words += len(lines)

# print(number_of_words)





