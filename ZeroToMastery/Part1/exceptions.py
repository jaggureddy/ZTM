def display():
    try:
        age = int(input('enter age: '))
        print(age)
    except ValueError:
        print('invalid age entered')
        display()
    except ZeroDivisionError:
        print('Zero entered')
        display()
    else:
        print('thanks')


def sum(num1, num2):
    try:
        return num1 + num2
    except (TypeError, ZeroDivisionError) as err:
        print(f'please enter numbers {err}')
    else:
        print('thanks')
    finally:
        print('finally block')


sum(1, '2')
