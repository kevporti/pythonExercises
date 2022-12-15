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

exerciseThree(3)