# Making the guess the number game

import random

target = random.randint(1, 40)
guess = []

print("You got 10 chance to guess the number from 1 to 40\n")

while len(guess) < 10:
    print('Input your guess!')
    chance = int(input('> '))
    guess = guess + [chance]
    if chance < target:
        print("You guess too low.")
    elif chance > target:
        print("You guess too high.")
    elif chance == target:
        print("You guess right", target,". You've made it in", len(guess), 'try.')
        break

for i in guess:
    print(i)