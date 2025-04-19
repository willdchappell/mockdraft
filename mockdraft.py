import matplotlib as mpl
import random as rand
import pandas as pnd


teams = ("Detroit Lions", "Washington Commanders", "Green Bay Packers", "Kansas City Chiefs", "Minnesota Vikings")
lions = []
commanders = []
packers = []
chiefs = []
vikings = []
teamlist = (lions, commanders, packers, chiefs, vikings)
print(teams)
playerList = ["Travis Hunter", "Sheduer Sanders", "Cam Ward", "Mason Graham", "Kenneth Grant", "James Pierce", "Will Johnson", "Colston Loveland", "Tyler Warren"]
print(playerList)
def draft(name):
    while True:
        player = input("Select a Player ")
        if (player in playerList):
            break
        else:
            print("Player was not found, try again")
    playerList.remove(player)
    return player
round = 1
pick = 1
while round <= 1:
    for x in teams:
        print(f"The {x} are on the clock...")
        print(f"Top 5 available: {playerList[0:5]}")
        drafted = draft(x)
        teamlist[pick-1].append(drafted)
        print(f"{x} drafted {drafted} in round {round} pick {pick}")
        pick += 1
    round += 1
    
print("Here are every teams picks")
for x in range(0,5):
    print(f"{teams[x]}: {teamlist[x]}")    
print("Congratulations, end of the draft!!")

