#1 For loop

# Ex 1: Write a defined cycle to print all numbers between 10 and 20.

def exerciseOne():
    for number in range(10, 21):
        print(number)

# Ex 2: Write a program to print all domino pieces, one per line, without repeating.

def exerciseTwo():
    pieces = []
    counter = 0

    for number1 in range(0, 7):
        for number2 in range(0, 7):
            if (not number2 < number1):
                pieces.extend([[number1, number2]])
                print(pieces[counter])
                counter += 1

# Ex 3: Modify the previous program so it can generate pieces of a game that can have numbers between 0 and N.

def exerciseThree(number):
    pieces = []
    counter = 0

    for number1 in range(0, number + 1):
        for number2 in range(0, number + 1):
            if (not number2 < number1):
                pieces.extend([[number1, number2]])
                print(pieces[counter])
                counter += 1

# Ex 4: Write a function that takes an M amount of values that are inserted by the user, and, as they enter, it shows
# the factorial of that number. The M number is inserted initially by the user.
# M = amountOfNumbers

def factorial(number):
    result = 1
    for i in range(1, number + 1):
        result = result * i
    return result

def exerciseFour():
    amountOfNumbers = int(input("Ingrese la cantidad de numeros a calcular: "))

    for i in range(0, amountOfNumbers):
        number = int(input("Ingrese un numero: "))
        result = factorial(number)
        print(result)

# Ex 5: Using the function, given as an example in the presentation, to convert a temperature from Fahrenheit to Celsuis,
# generate a temperature conversion table, from 0◦F to 120◦F, from 10 to 10.

def farCel(f):
    return (f-32)*5/9

def exerciseFive():
    maxInFar = 120

    print("Fahrenheit(◦F)          Celsius(◦C)")
    print("-----------------------------------")

    for i in range(0, maxInFar + 1, 10):
        celsius = '%.2f' % farCel(i)
        print(i, "                    |",  celsius)

# Ex 6: Write a function that gets an amount of pesos, an interest rate and a number of years and returns, as a result, the final amount.
# Use this formula: Cn = C * (1 + (x/100))^n, where C is the Initial Capital, x is the interest rate and n is the number of years.

def exerciseSix():
    pesos = int(input("Ingrese la cantidad de pesos inicial: "))
    interestRate = int(input("Ingrese la tasa de interes anual: "))
    years = int(input("Ingrese la cantidad de años a calcular: "))

    for i in range(1, years + 1):
        finalAmount = '%.2f' % (pesos * (1 + interestRate / 100)**i)
        print("El monto final despues del año", i, "es:", finalAmount)
        # Even though the exercise doesn't ask to show the process year by year, I think it's better like this. The section is to practice For Loops
        # and this exercise doesn't require it so I thought it would be nice to have one and improve the experience of the function.

# Ex 7: Write a function that gets an N number from parameters and prints the first N triangular numbers, with their index
# (Triangular numbers gets calculated by adding up every number from 1 to N)

def exerciseSeven(number):
    for i in range(1, number + 1):
        triangularNumber = 0
        for j in range(1, i + 1):
            triangularNumber = triangularNumber + j
        print(i, "-", triangularNumber)