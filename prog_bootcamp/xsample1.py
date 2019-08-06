# import math
#
# # get input from user and print it
# name = input("What is your name?: ")
# age = int(input("How old are you?: "))
#
# print("Hi", name.capitalize(), "! In 10 years you will be", age + 10, "y.o.")
#
#
# # St Ives problem
# print("There will be", (1+1+(7*7*7*7)), "going to St. Ives")
#
# # Lollies problem
# print("\n\n")
# lollies = int(input("Enter the number of lollies: "))
# num_people = int(input("Enter the number of people: "))
#
# print("Each person will get", lollies // num_people,
#       "lollies, and you will have,", lollies % num_people, "left.")
#
# # volume of cylinder
# cyl_radius = int(input("Cylinder radius: "))
# cyl_height = int(input("Cylinder height: "))
#
# cyl_volume = math.pi * (cyl_radius ** 2) * cyl_height
#
# print(cyl_volume)
#
# # hypotenuse length
# f_triangle_side = int(input("Input the first side: "))
# s_triangle_side = int(input("Input the second side: "))
#
# hypotenuse = math.sqrt(f_triangle_side ** 2 + s_triangle_side ** 2)
# print(hypotenuse)

# # Celsius to Fahrenheit
# print("\n\nLet's try converting Celsius to Fahrenheit or vice versa.")
# print("Please specify from either C or Fahrenheit you want to convert.")
# retry = 'y'
#
# while retry == 'y':
#     option = input("From Celsius or Fahrenheit? (c/f) ")
#     if option == 'c':
#         celsius = int(input("Input the number you want to convert: "))
#         celsius_to_fahrenheit = (celsius * 9 / 5) + 32
#         print("That number", celsius,"C is", celsius_to_fahrenheit, "F.")
#     elif option == 'f':
#         fahrenheit = int(input("Input the number you want to convert: "))
#         fahrenheit_to_celsius = (fahrenheit - 32) * 5 / 9
#         print("That number", fahrenheit,"C is", fahrenheit_to_celsius, "F.")
#     else:
#         print("Please check your input!")
#     retry = input("Do you want to retry? (y/n): ")
# print("Thank you for using our service.")