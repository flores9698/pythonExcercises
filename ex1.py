#!/usr/bin/env python3
""" Create a program that asks the user to enter their name and their age. 
Print out a message addressed to them that tells them the year that they will turn 100 years old."""

def yearOF100(age):
	"""Returns the year when the person turn 100 year """
	current_year= 2020
	year100= current_year-age+100

	return year100



name = input("Enter your name: ")
current_age = int(input("How old were you or will you be this year: "))

year= yearOF100(current_age)

print("Hello {} you have {} and in the year {} you would be 100 years old".format(name,current_age,year))

