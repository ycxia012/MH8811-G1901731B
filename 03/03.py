# define all 3 functions 
def func1():
    print('Hello, World!')


def func2():
    name = input('Enter your username:')
    print('Hello,', name, '!')


def func3():
    celsius = float(input('Enter the celsius you want to convert:'))
    fahrenheit = celsius * 1.8 + 32
    print(fahrenheit)

    # ------------------------------------------------------------------------------- #


while True:
    n = input('Which function you would like to use?\n 1 for Hello world\n 2 for greeting\n 3 for transfer the temperature\n If no, enter something else to exit!')


    def users(n):
        if n == '1':
            return func1()

        elif n == '2':
            return func2()

        elif n == '3':
            return func3()

        else:
            return exit("Thanks for using!")


    users(n)
# end of function

