# shift+ F6 to rename variable
# python using half open range (start to last but nor including the last one)

# # Trying to print number from 0 to 100
# for i in range(0, 101):
#     print(i)

# input into list what user entered then end it with q then print the list
fruit = []
add_fruit = input(">>> ")

while add_fruit != 'q':
    if add_fruit != 'q':
        fruit.append(add_fruit)
        add_fruit = input(">>> ")
        fruit.sort()

print("Your fruit are %s" % fruit)

# # Trying to find the average of number of list
# my_number = [3, 5, 8, 2, 2, 1000]
# my_number_length = len(my_number)
#
# my_number_sum = 0
#
# for i in range(0, my_number_length):
#     my_number_sum += my_number[i]
#
# print("The average of my_number is", my_number_sum/my_number_length)

# # My code for trying to look for sum product
# factorial_number = int(input("> "))
# element_factorial_number = []
# for i in range(0, factorial_number):
#     element_factorial_number.append(factorial_number-i)
# print(element_factorial_number)
#
# element_factorial_number_length = len(element_factorial_number) + 1
#
# sum_product_element = 1
# for element in range(1, element_factorial_number_length):
#     sum_product_element *= element
#
# print(sum_product_element)

# # populating number in my list that is multiplies of 3
# my_list_of_number = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 15]
#
# muliplier_of_3 = []
# for number in my_list_of_number:
#     if number % 3 == 0:
#         muliplier_of_3.append(number)
#
# print(len(muliplier_of_3))

# # Fizz Buzz Problem
# input_number = input("Input number separated by space (' '):")
# splited_input = map(int, input_number.split(sep=' '))
# print(type(splited_input))
#
# converted_list = []
#
# for i in splited_input:
#     if i % 3 == 0 and i % 5 == 0:
#         converted_list.append("FizzBuzz")
#     elif i % 3 == 0:
#         converted_list.append("Fizz")
#     elif i % 5 == 0:
#         converted_list.append("Buzz")
#     else:
#         converted_list.append(i)
# print(converted_list)