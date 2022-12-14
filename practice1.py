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

def recursion(numbersToShow, startFromNumber, counter = 0):
  if (counter < numbersToShow):
    if (startFromNumber % 2 == 0):
      counter = counter + 1
      print(startFromNumber)
    recursion(numbersToShow, startFromNumber + 1, counter)

def exerciseThree():
  numbersToShow = int(input("Cantidad de numeros pares a mostrar:"))
  startFromNumber = int(input("Mostrar despues del numero:"))
  recursion(numbersToShow, startFromNumber)


# Ex 4: Write a program that calculates and prints the result of the sum of the first 50 natural numbers
# using a recursive function.

def exerciseFour(number = 50, sumOfNumbers = 0):
  if (number > 0):
    sumOfNumbers += number
    exerciseFour(number - 1, sumOfNumbers)
  else:
    print(sumOfNumbers)

# Ex 5: Write a program that calculates and prints the result of the sum of the first N natural numbers
# using a recursive function.
# N = number

def exerciseFive():
  number = int(input("Ingrese el numero hasta donde sumar:"))
  exerciseFour(number, 0)

# Ex 6: Write a program that calculates and prints the result of the sum of the natural numbers greater
# than N and lesser than M using a recursive function.
# N = startFromNumber
# M = stopAtNumber

def recursiveSum(startFromNumber = 1, stopAtNumber = 0, sum = 0):
  if (startFromNumber <= stopAtNumber):
    sum += startFromNumber
    recursiveSum(startFromNumber + 1, stopAtNumber, sum)
  else:
    print(sum)

def exerciseSix():
  startFromNumber = int(input("Ingrese el numero inicial para la suma:"))
  stopAtNumber = int(input("Ingrese el numero hasta donde sumar:"))
  recursiveSum(startFromNumber, stopAtNumber)