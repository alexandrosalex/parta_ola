
import random

NumPlayers = int(input("Please input number of players: "))
if NumPlayers < 2: 
    print("I am sorry!This game requires two or more players to be played.")
else:
    beans = int(input("Please input number of beans per player: "))
    print("--------------------------------------------------")
               
player_beans = [beans for x in range(NumPlayers)]
player=random.randint(1,NumPlayers) 
round=1
pot=0
game=True
spin=""
    
#arxh tou gurou
while game==True:
    zero_players=sum(x == 0 for x in player_beans) #paiktes me miden fasolia
    out_players=sum(x < 0 for x in player_beans) #apokleismenoi paiktes
    player_beans=[x - 1 for x in player_beans] #afairese ena apo olous
    
    out_players=sum(x < 0 for x in player_beans) #apokleismenoi paiktes
    if out_players == NumPlayers-1:
        game=False

    pot=pot+NumPlayers-out_players-zero_players
    newround=False

    print("Round ",round," begins: Everyone Puts 1")
    print("Current state:")
    print("Pot: ", pot)
    for x in range(NumPlayers):
        if player_beans[x]>=0:
            print("Player",x+1,"'s budget: ",player_beans[x])
        else:
             print("Player",x+1,"is eliminated")
    
    while newround==False and game==True:
        player=player+1
        if player==NumPlayers+1:
            player=1
        while player_beans[player-1]<0:
            player=player+1
            if player==NumPlayers+1:
                player=1
        number=random.randint(1,6)
        if number==1:
            spin="Take One"
            player_beans[player-1]=player_beans[player-1]+1
            pot=pot-1
            if pot==0:
                newround=True
        elif number==2:
            spin="Take Two"
            if pot==1:
                player_beans[player-1]=player_beans[player-1]+1
                pot=0
                newround=True
            elif pot==2:
                player_beans[player-1]=player_beans[player-1]+2
                pot=0
                newround=True
            else:
                player_beans[player-1]=player_beans[player-1]+2
                pot=pot-2
        elif number==3:
            spin="Take All"
            player_beans[player-1]=player_beans[player-1]+pot
            pot=0
            newround=True
        elif number==4:
            spin="Put One"
            player_beans[player-1]=player_beans[player-1]-1
            if player_beans[player-1]>=0:
                pot=pot+1
            
            out_players=sum(x < 0 for x in player_beans) #apokleismenoi paiktes
            if out_players == NumPlayers-1:
                game=False
                newround=True
        elif number==5:
            spin="Put Two"
            player_beans[player-1]=player_beans[player-1]-2
            if player_beans[player-1]==-1:
                pot=pot+1
            elif player_beans[player-1]>=0:
                pot=pot+2
            
            out_players=sum(x < 0 for x in player_beans) #apokleismenoi paiktes
            if out_players == NumPlayers-1:
                game=False
                newround=True
        else:
            spin="Everyone Puts a Bean"
            zero_players=sum(x == 0 for x in player_beans) #paiktes me miden fasolia
            out_players=sum(x < 0 for x in player_beans) #apokleismenoi paiktes
            player_beans=[x - 1 for x in player_beans] #afairese ena apo olous
            
            out_players=sum(x < 0 for x in player_beans) #apokleismenoi paiktes
            if out_players == NumPlayers-1:
                game=False
                newround=True
        
            pot=pot+NumPlayers-out_players-zero_players
        print("\nPlayer",player,"spinned",spin)
        print("Current state:")
        print("Pot: ", pot)
        for x in range(NumPlayers):
            if player_beans[x]>=0:
                print("Player",x+1,"'s budget: ",player_beans[x])
            else:
                 print("Player",x+1,"is eliminated")
    #while end
    if game==True:
        round=round+1
        print("Pot is zero: round ends")
        print("--------------------------------------------------")
    else:
        for x in range(NumPlayers):
            if player_beans[x]>=0:
                print("Game finished: Player",x+1,"wins")
