import os
# balances contains first the person's name then their balance e.g item1 = user1 item2 = user1's balance etc
os.system('pip install scratchattach')
os.system('pip install flask')
# template here: os.system('pip install package_name')
space = 
import scratchattach
import flask
import json # built in module

with open ('balances.json','r') as file:
    balances = json.load(file)

session = sa.login("username", "password")
project = session.connect_cloud('project id')
client = project.requests()

@client.request # property function, gets data from scratch
def ping() # received when using send request name 'ping' in project
    print("Pinging recieved from scratch.")
    return "pong" # returns 'pong' to Scratch in response list.

@client.request
def new(argument1) # recieved when flag clicked, put code in project: when flag clicked, send request: new, argument1: username
user = argument1
if user in balances
    return "old user"
else:
    balances.append(user)
    balances.append("100")
    return "new"

@client.request
def gift(argument1, argument2) # arg1 is the amount you want to gift and arg2 is who you want to gift it to then a space then who gifted it to you. 
    for i in argument2
        if argument2[i] == space:
            if who_gift in balances:
                balances[balances.index(who_gift) + 1] = balances[balances.index(who_gift) + 1] + argument1
                item = i
                for i in range(item, len(argument)) 
                    gifter = gifter + argument2[i]
                    
                balances[balances.index(gifter) + 1] = balances[balances.index(gifter) + 1] - argument1
        else:
            who_gift = who_gift + argument2[i] 
    
