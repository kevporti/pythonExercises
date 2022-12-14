# 1.1 First programs using numbers

# Ex 1: Write a program that prints the first 25 even natural numbers.

def exerciseOne(number = 1, numbersToShow = 25):
  numbersToCheck = numbersToShow * 2
  if (number <= numbersToCheck):
    if (number % 2 == 0):
      print(number)
    exerciseOne(number + 1, numbersToShow)

# Ex 2: Write a program that prints the first 100 even natural numbers.

def exerciseTwo():
  exerciseOne(number = 1, numbersToShow = 100)

# Ex 3: Write a program that prints the first N even numbers greater than M.
# N = numbersToShow
# M = startFromNumber

def recursion(numbersToShow, startFromNumber):
  numbersToCheck = numbersToShow * 2
  if (startFromNumber <= numbersToCheck):
    print(startFromNumber)
    # if (startFromNumber % 2 == 0):
      # print(startFromNumber)
    recursion(numbersToShow, startFromNumber + 1)

def exerciseThree():
  numbersToShow = int(input("Cantidad de numeros pares a mostrar:"))
  startFromNumber = int(input("Mostrar despues del numero:"))
  recursion(numbersToShow, startFromNumber)

exerciseThree()