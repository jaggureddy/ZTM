from random import randint


def run_guess(g, answer):
    if 0 < int(g) < 11:
        if answer == int(g):
            print('')
            return True
        else:
            print('boo hoo')


if __name__ == '__main__':
    ans = randint(1, 10)

    while True:
        try:
            guess = input('Enter a number 1 to 10: ')
            if run_guess(guess, ans):
                break
        except ValueError:
            print('Invalid number entered')
            continue

