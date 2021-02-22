from random import randint

answer = randint(1, 10)

while True:
    try:
        guess = input('Guess a number 1 ~ 10: \n')

        if 0 < int(guess) < 11:
            if guess == answer:
                print('You are more intelligent that you look, eh?')
            break
        else:
            print('Hey! I said 1 ~ 10 smart face!')
    except ValueError:
        print('I can tell you know how to read, I said numbers!')
        continue
