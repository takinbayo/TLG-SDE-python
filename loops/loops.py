#!/usr/bin/env python3

farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]



#first = farms[0]["agriculture"]

#for x in first:
 #   print(x)

farm_chosen = input("Choose a farm, you know the choices :) : ")

num = 0

if input == "W Farm":
    num = 1
elif input == "SE Farm":
    num = 2

farm = farms[num]["agriculture"]
for x in farm:
    print(x)

