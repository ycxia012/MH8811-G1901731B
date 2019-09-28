while True:
    n = input('Which function you would like to use? 1,2 or 3? If no, pls enter no for exit')


    def func1():
        print('Hello World!')


    def func2():
        name = input('Enter your username:')
        print('Hello,', name, '!')


    def func3():
        celsius = float(input('Enter the celsius you want to convert:'))
        fahrenheit = celsius * 1.8 + 32
        print(fahrenheit)


    def users(n):
        if n == '1':
            return func1()

        if n == '2':
            return func2()

        if n == '3':
            return func3()

        if n == 'no':
            return exit("Thanks for using!")


    users(n)


