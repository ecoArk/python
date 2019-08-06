import random

instruction = "The one getting the distance goal first is the winner"

goal_distance = 10

user = input("Enter your name: ")
bot_1 = "Turing"
bot_2 = "Bool"

user_distance = 0
bot_1_distance = 0
bot_2_distance = 0

# It helps to check wether the distance of the user and the bot
# is different or not. if it is different than the other
def check_duplicate(checked_value, param1, param2):
    if checked_value != param1 and checked_value != param2:
        return checked_value
    else:
        return 0

while user_distance < goal_distance and bot_1_distance < goal_distance and bot_2_distance < goal_distance:
    user_move = int(input("Enter your number from 1 to 3: "))
    if 1 <= user_move <= 3:
        bot_1_move = random.randint(1, 3)
        bot_2_move = random.randint(1, 3)
        print(user_move, bot_1_move, bot_2_move)
        # if user_move != bot_1_move and user_move != bot_2_move:
        #     user_distance += user_move
        user_distance += check_duplicate(user_move, bot_1_move, bot_2_move)
        bot_1_distance += check_duplicate(bot_1_move, bot_2_move, user_move)
        bot_2_distance += check_duplicate(bot_2_move, bot_1_move, user_move)

        print("\nAfter that turn.")
        standing = "%s: %d km\n%s: %d km\n%s: %d km\n" % (
            user, user_distance, bot_1, bot_1_distance, bot_2, bot_2_distance)
        print(standing)
    else:
        print("Enter number 1 to 3 only!")

if user_distance > bot_1_distance and user_distance > bot_2_distance:
    winner = user
elif bot_1_distance > user_distance and bot_1_distance > bot_2_distance:
    winner = bot_1
elif bot_2_distance > user_distance and bot_2_distance > bot_1_distance:
    winner = bot_2
print("Congratulations. The winner is %s." % winner)