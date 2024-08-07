#!/usr/bin/env python3

# create a while loop that stops when correct answer is given
# we want to give the player 3 turns only
# If they get the capital correct, ask what continent. (region in module)

from countryinfo import CountryInfo
import random
import pycountry

isGameOn = True
gameRound = 3

while isGameOn:
    
    pyCountries = list(pycountry.countries)
    random_country = random.choice(pyCountries)
    chosen_country = CountryInfo(random_country.name)
    capital = chosen_country.capital()

    firstAnswer = input(f"What is the capital of {random_country.name}? ")

    
    if firstAnswer.lower() == capital.lower():
        print("Correct! Nice Geography skills")
        continent = chosen_country.region()
        secondAnswer = input(f"Which continent is {random_country.name} in? ")
        
        if secondAnswer.lower() == continent.lower():
            print("Correct Again! Nice Job")
        else: 
            print(f"Incorrect! The correct answer is {continent}")

        isGameOn = False

    else:
        print(f"Wrong Answer! the capital of {random_country.name} is {capital} ")
        gameRound -= 1
   
   
    if gameRound == 0:
        print("Game Over! Go and Study!")
        isGameOn = False
