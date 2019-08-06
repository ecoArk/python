# Boolean value --> True or False
#
# # XOR you can't make both true or both false
# f_argument = True
# s_argument = False
#
# print((f_argument and not s_argument) or (s_argument and not f_argument))
#
# # Grade conversion
# score = int(input("Enter your score: "))
# desc_grade = "Your score will get"
#
# if score > 70:
#     print(desc_grade, "HD")
# elif score >= 60:
#     print(desc_grade, "C")
# elif score >= 50:
#     print(desc_grade, "P")
# elif score < 50:
#     print(desc_grade, "N")
# else:
#     print("Check your input!")
#
#
# # Name evaluator
# name = input("Enter your name: ")
#
# name_length = len(name)
#
# if name_length > 7:
#     print(name.upper())
# elif name_length < 6 and name_length > 4:
#     age = input("How old are you? :")
#     print("You are", age, "y.o.", name)
# else:
#     print("Hello", name)
#
# income = int(input("Input your income: "))
# tax = 0
#
# if income < 20000:
#     tax = 0
# elif income <= 20000 and income < 50000:
#     tax = 0.1
# elif income <= 50000 and income < 100000:
#     tax = 0.2
# elif income >= 100000:
#     tax = 0.3
# else:
#     print("Your income is out of acceptable range.")
#
# print(" Your income is:", income, "\n",
#       "Your deferred tax is:", int(income * tax), "\n",
#       "Your income after tax is:", int(income - (income * tax)))
#
# # Password recommendator
# password = input(">>>> ")
# password_last_digit = (password[-1]).isdigit()
# password_length = len(password)
# # password_last_digit_int = int(password_last_digit)
#
# # when using a loop remember to reassign the variable
#
# while not( password_last_digit and  password_length > 6):
#     password = input(">>>> ")
#     password_last_digit = (password[ -1 ]).isdigit()
#     password_length = len(password)
#
# print("Congratulation! You got a valid password.")
#
# int_list = '0123456789'
# password = input(">>>> ")
#
# password_last_digit = (password[-1])
# password_length = len(password)
# if (password_last_digit in int_list) and (password_length > 6):
#     print("You have valid password.")
# else:
#     print("Please check your password.")
#     password = input(">>>> ")
#     password_last_digit = password[-1]
#     password_length = len(password)
#     if (password_last_digit in int_list) and (password_length > 6):
#         print("You have valid password.")
#     else:
#         print("You got yur chance, sorry.")

# Making a program to calculate volume
# import math
#
# direction_1 = "\nPlease enter your choice."
# direction_2 = "You can choose one option between pyramid(p), cylinder(c), " \
#               "or sphere(s)."
# print(direction_1, direction_2)
#
# calculation = input("Do you want to calculate volume? (y/n)>>> ")
#
# while calculation == 'y':
#     option = input("Choose one option. (pyramid/cylinder/sphere >>> ")
#     if option == "pyramid" or option == "p" or option == "pyr":
#         print("Calculating the volume of pyramid, please input: ")
#         length = int(input("Input the length: "))
#         width = int(input("Input the width: "))
#         height = int(input("Input the height: "))
#         pyramid_vol = (length * width * height) / 3
#         print(pyramid_vol)
#     elif option == "cylinder" or option == "cyl" or option == "c":
#         print("Calculating the volume of cylinder, please input: ")
#         radius = int(input("Input the radius: "))
#         height = int(input("Input the height: "))
#         cylinder_vol = (math.pi * radius ** 2 * height)
#         print(cylinder_vol)
#     elif option == "sphere" or option == "sph" or option == "s":
#         print("Calculating the volume of sphere, please input: ")
#         radius = int(input("Input the radius: "))
#         sphere_vol = math.pi * radius ** 3 * 4 / 3
#         print(sphere_vol)
#     calculation = input("Do you want to calculate volume? (y/n)>>> ")
# print('Thank you for your kind input.')
