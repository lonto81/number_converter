from random import *
import time

number = int(input('What number would you like to convert today?'))
print ("You chose the number: ", number)
time.sleep(1)
choice = int(input("What number system would you like to convert it to? ""Please choose from the following selections: (1) Binary,(2) Octal, (3) Decimal, (4) Hexadecimal: "))
print("You chose: ", choice)
time.sleep(1)
if choice == 1:
    print(number, "In Binary is:", bin(number))
    time.sleep(1)
elif choice == 2:
    print(number, "In Octal is:", oct(number))
    time.sleep(1)
elif choice == 3:
    print(number, "In Decimal is:", int(number))
    time.sleep(1)
elif choice == 4:
    print(number, "In Hexadecimal is:", hex(number))
    time.sleep(1)
