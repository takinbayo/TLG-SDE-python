#!/usr/bin/python3

import random
import time
"""Driving a simple game framework with
   a dictionary object | Alta3 Research"""


def showInstructions():
  """Show the game instructions when called"""
  #print a main menu and the commands
  print('''
    RPG Game
    ========
    Commands:
      go [direction]
      get [item]
    ''')


def showStatus():
  """determine the current status of the player"""
  # print the player's current location
  print('---------------------------\n')
  print('You are in the ' + currentRoom)
  # print what the player is carrying
  print('Inventory:', inventory)
  # check if there's an item in the room, if so print it
  if "item" in rooms[currentRoom]:
    print('You see a ' + rooms[currentRoom]['item'])

  print("---------------------------")

def show_health(health, strength, vampire_health, vampire_strength):
  print("-------------------------------------------------\n")
  print(f"health = {health} strength {strength} \n")
  print(
      f"Vampire health = {vampire_health} Vampire strength = {vampire_strength}\n"
  )
  print("-------------------------------------------------")


def combat():
  health = 100
  strength = 20
  vampire_health = 90
  vampire_strength = 15

  while health >= 0 and vampire_health >= 0:
    show_health(health, strength, vampire_health, vampire_strength)
    decrease_health = int(vampire_strength * random.random())
    decrease_vamp_health = int(strength * random.random())
    vampire_health -= decrease_vamp_health
    health -= decrease_health
    time.sleep(3)
    

    if vampire_health <= 0:
      print("************************************************")
      print("You have defeated the vampire bravely, You Win!")
      print("************************************************")
      vampire_health = 0
      show_health(health, strength, vampire_health, vampire_strength)
      break

    elif health <= 0:
      print("*****************************************")
      print("You fought bravely but have been Killed")
      print("*****************************************")
      health = 0
      show_health(health, strength, vampire_health, vampire_strength)
      break


# an inventory, which is initially empty
inventory = []

# a dictionary linking a room to other rooms
rooms = {
    'Hall': {
        'south': 'Kitchen',
        'east': 'Dungeon',
        'item': 'sword'
    },
    'Kitchen': {
        'north': 'Hall'
    },
    'Dungeon': {
        'west': 'Hall',
        'item': 'Vampire'
    }
}

# start the player in the Hall
currentRoom = 'Hall'

showInstructions()

# breaking this while loop means the game is over
while True:
  showStatus()

  # the player MUST type something in
  # otherwise input will keep asking
  move = ''
  while move == '':
    move = input('>')

  # normalizing input:
  # .lower() makes it lower case, .split() turns it to a list
  # therefore, "get golden key" becomes ["get", "golden key"]
  move = move.lower().split(" ", 1)

  #if they type 'go' first
  if move[0] == 'go':
    #check that they are allowed wherever they want to go
    if move[1] in rooms[currentRoom]:
      #set the current room to the new room
      currentRoom = rooms[currentRoom][move[1]]
    # if they aren't allowed to go that way:
    else:
      print('You can\'t go that way!')

  #if they type 'get' first
  if move[0] == 'get':
    # make two checks:
    # 1. if the current room contains an item
    # 2. if the item in the room matches the item the player wishes to get
    if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
      #add the item to their inventory
      inventory.append(move[1])
      #display a helpful message
      print(move[1] + ' got!')
      #delete the item key:value pair from the room's dictionary
      del rooms[currentRoom]['item']
    # if there's no item in the room or the item doesn't match
    else:
      #tell them they can't get it
      print('Can\'t get ' + move[1] + '!')

  if currentRoom == 'Dungeon':
    userAnswer = input('Do you want to Fight or Run?\t').lower()
    if userAnswer == "run":
      print("******************************************")
      print("The Vampire caught you, You DIED a COWARD!")
      print("******************************************")
      break
    elif userAnswer == "fight":
      combat()
      break
    else:
      print("Enter appropriate option, Fight or Run")

