# Let's try making a hangman game

# random module is used for making the question
import random

# sample question
city = ['semarang', 'jakarta', 'bandung', 'surabaya', 'malang']
chance = 0
tried_answer = []

# Establish the framework of the answer
answer = city[random.randint(0, len(city)-1)]
disp_question = list(answer)
guess_question = []
for i in disp_question: guess_question.append('_')

# Establish the loop for answering the question
while chance < 7:
    print(guess_question)
    print('guess the letter')
    guess = input('> ')
    if guess in disp_question:
        print('you got it right')
        finding = [i for i, x in enumerate(disp_question) if x == guess]
        for i in finding:
            guess_question[i] = guess

    elif guess not in answer:
        chance = chance + 1
        tried_answer = tried_answer + [guess]
        print('Wrong Answer:', tried_answer, '_ ' * (7 - chance))
    else:
        continue

    if guess_question == disp_question:
        print(guess_question)
        print("You win, the answer is", answer)
        break

# print('GAME OVER. The answer is', answer)