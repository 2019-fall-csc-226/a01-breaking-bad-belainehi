######################################################################
# Author: Dr. Scott Heggen      TODO: Change this to your name
# Username: heggens             TODO: Change this to your username
#
# Assignment: A01
#
# Purpose: A program that returns your Chinese Zodiac animal given a
# birth year between 1988 and 1999. Also prints your friend's animal,
# and your compatibility with that friend's animal.
######################################################################
# Acknowledgements:
#   Original Author: Dr. Scott Heggen
######################################################################

# Remember to read the detailed notes about each task in the A01 document.

######################################################################
# (Required) Task 1
# TODO Ask user for their birth year
import time

yob=input ("Hello! What year were you born? Be honest now!")

# TODO Check the year using if conditionals, and print the correct animal for that year.
# See the a01_pets.py for examples
if yob == "1996" or yob == "1972" or yob == "1982":
    print("You are a rat! Hope there aren't any Cats around. ")
elif yob == "1973" or yob == "1985" or yob == "1997":
    print("You are an Ox!")
elif yob == "1974" or yob == "1986" or yob == "1998":
    print("You are a Tiger! Meow?")
elif yob == "1975" or yob == "1987" or yob == "1999":
    print("You are a Rabbit!")
elif yob == "1976" or yob == "1988" or yob == "2000":
    print("You are a Dragon! How scary and nobel. Do you spit fire?")
elif yob == "1977" or yob=="1989" or yob=="2001":
    print("You are a Snake!")
elif yob == "1978" or yob == "1990" or yob == "2002":
    print("You are a Horse!")
elif yob == "1979" or yob == "1991" or yob == "2003":
    print("You are a Goat!")
elif yob == "1980" or yob == "1992" or yob == "2004":
    print("You are a Monkey!")
elif yob == "1981" or yob == "1993" or yob == "2005":
    print("You are a Rooster! Please don't wake up in the morning.")
elif yob == "1982" or yob== "1994" or yob== "2006":
    print("You are a Dog!")
elif yob == "1983" or yob== "1995" or yob== "2007":
    print("You are a Pig!")
else:
    print ("Please input a number between 1972 and 2007. ")
time.sleep (3)
######################################################################
# (Required) Task 2
# TODO Ask the user for their friend's birth year
fyob = input ("Now let's check your friend's year. What is their birth year?")

# TODO Similar to above, check your friend's year using if conditionals, and print the correct animal for that year
if fyob == "1996" or fyob == "1972" or fyob == "1982":
    print ("They are a rat! Hope there aren't any Cats around. ")
elif fyob == "1973" or  fyob=="1985" or fyob== "1997":
    print ("They are an Ox!")
elif fyob == "1974" or fyob=="1986" or fyob== "1998":
    print("They are a Tiger! Meow?")
elif fyob == "1975" or fyob== "1987" or fyob== "1999":
    print("They are a Rabbit!")
elif fyob == "1976" or fyob== "1988" or fyob== "2000":
    print("They are a Dragon! How scary and nobel. Do they spit fire.")
elif fyob == "1977" or fyob== "1989" or fyob== "2001":
    print("They are a Snake!")
elif fyob == "1978" or fyob=="1990" or fyob== "2002":
    print("They are a Horse!")
elif fyob == "1979" or fyob== "1991" or fyob== "2003":
    print("They are a Goat!")
elif fyob == "1980" or fyob== "1992" or fyob== "2004":
    print("They are a Monkey!")
elif fyob == "1981" or fyob== "1993" or fyob== "2005":
    print("They are a Rooster! Hope theey don't wake everybody up in the morning.")
elif fyob == "1982" or fyob== "1994" or fyob== "2006":
    print("They are a Dog!")
elif fyob == "1983" or fyob== "1995" or fyob== "2007":
    print("They are a Pig!")
else:
    print ("Please input a number between 1972 and 2007. ")
######################################################################
# (Optional) Task 3
# TODO Check for compatibility between your birth year and your friend's birth year
# NOTE: You can always assume the first input is your birth year (i.e., 1982 for me).
# This way, you are not writing a ton of code to consider every possibility.
# In other words, only do one row of the sample compatibility table.



# TODO print if you are a strong match, no match, or in between
