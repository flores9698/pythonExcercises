#!/usr/bin/env python3
"""Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. 
Hint: how does an even / odd number react differently when divided by 2?  """
import sys


def isEven(number):
	""" Returns True when the number entered is even False otherwise"""
	if number%2 == 0:
		return True
	return False


if len(sys.argv)==2:
	number= float(sys.argv[1])
	if isEven(number):
		print("The number {} is even.".format(number))
	else:
		print("The number {} is odd.".format(number))

else:
	number= float(input("Enter a number you want to know if its even or odd"))
	if isEven(number):
		print("The number {} is even.".format(number))
	else:
		print("The number {} is odd.".format(number))


