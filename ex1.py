#!/usr/bin/env python3
""" Create a program that asks the user to enter their name and their age. 
Print out a message addressed to them that tells them the year that they will turn 100 years old."""

def yearOF100(age):
	"""Returns the year when the person turn 100 year """
	current_year= 2020

	year100= current_year-age+100

	return year100



name = input("Enter your name: ")
age = input("Enter your current age: ")

year= yearOF100(age)

print("Hello {} you have {} and in the year {} you would be 100 years old".format(name,age,year))

