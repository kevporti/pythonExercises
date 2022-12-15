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

# 1.2 Firsts programs using strings.

# Ex 7: Write a program that recieves a name and returns the name concatenated twice.

def exerciseSeven(name):
  print(name*2)

# Ex 8: Write a program that recieves a name and a number N, and returns the name given N times.

def exerciseEight(name, number):
  print(name*number)

# 1.3 Firsts interactive programs.

# Ex 9: Complete the following items:
#   - Write a sum function that recieves two numbers and returns the result of the sum.
#   - Write a substraction function that recieves two numbers and returns the result.
#   - Write a multiplication function that recieves two numbers and returns the result.
#   - Write a division function that recieves two numbers and returns the result.
#   - Write a program that shows a message asking the user to choose one of the following options:
#   - 1. Suma
#   - 2. Resta
#   - 3. Multiplicacion
#   - 4. Division
#   And then ask for two numbers and show the result.
#   - Add an option like this:
#   - 5. Salir
#   So that while the user doenst press 5, the program keeps working following the past items.

def sum(number1, number2):
  return number1 + number2

def substraction(number1, number2):
  return number1 - number2

def multiplication(number1, number2):
  return number1 * number2

def division(number1, number2):
  if(number2 == 0):
    return "No se puede dividir por 0"
  return number1 / number2

def calculator():
  print("\n1. Suma \n2. Resta \n3. Multiplicacion \n4. Division\n\n5. Salir")
  operation = int(input("\nPor favor seleccione la operacion a realizar: "))
  if (operation == 5):
    print("Hasta luego...")
    return
  number1 = int(input("Ingrese el primer numero: "))
  number2 = int(input("Ingrese el segundo numero: "))

  if (operation == 1):
    result = sum(number1, number2)
    print("El resultado de la operacion es: " + str(result))
  elif (operation == 2):
    result = substraction(number1, number2)
    print("El resultado de la operacion es: " + str(result))
  elif (operation == 3):
    result = multiplication(number1, number2)
    print("El resultado de la operacion es: " + str(result))
  elif (operation == 4):
    result = division(number1, number2)
    print("El resultado de la operacion es: " + str(result))
  calculator()


calculator()