import random

words = ['python', 'java', 'kotlin', 'javascript']
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z']
pc = random.choice(words)
print('H A N G M A N\n')


def check_letter(pc, user, hint):
    new_hint = ''
    for i, x in enumerate(pc):
        if x == user:
            new_hint += user
            continue
        else:
            new_hint += hint[i]
            continue
    return new_hint


def game():
    t = 8
    user = ''
    hint = '-'*(len(pc))
    user_try = ''
    while t > 0:
        print('')
        hint = str(check_letter(pc, user, hint))
        print(hint)
        user = input('Input a letter:')
        if user in user_try:
            print('You already typed this letter')
            continue
        elif user not in letters and len(user) == 1:
            print('It is not an ASCII lowercase letter')
            continue
        elif len(user) != 1:
            print('You should input a single letter')
            continue
        elif user not in pc:
            print('No such letter in the word')
            t -= 1
        user_try += user
        if t == 0 and hint == pc:
            print(f'You guessed the word {pc}!')
            print('You survived!')
        elif t == 0 and hint != pc:
            print('You are hanged!')

while True:
    play = input('Type "play" to play the game, "exit" to quit:')
    if play.lower() == 'play':
        game()
    else:
        break
