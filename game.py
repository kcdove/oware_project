
# creating the board
# total_number_of_seeds = 48
#  total_number_of_pits = 12
pitseeds = [ 4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0] # this is an array of the number of seed in the pit

playing = True

player1 = True

msgCode = 0

#Player1_pit = ('a', 'b', 'c', 'd', 'e', 'f')
#player2_pit = ('g', 'h', 'i', 'j', 'k', 'l')

while(playing):
    # a tuple of the player's pits
    #player1 = Player1_pit
    #if player1:
     #   say = ("player1s' Turn. chose from g-l")
    #else:
     #   say =("invalid pit")
    #player2 = player2_pit
    #if player2:
     #   say = ("player2s' Turn. chose from g-l")
    #else:
     #   say =("invalid pit")
    #print(say)
    
    
    msg = ""
    if player1 and msgCode == 0:
        msg = "Player One's turn, choose from a-f"
    elif not(player1) and msgCode == 0:
        msg = "Player Two's turn, choose from g-l"
    elif player1 and msgCode == -2:
        msg = "Invalid Input. Try again Player One"
    elif not(player1) and msgCode == -2:
        msg = "Invalid Input. Try again Player Two"
    elif player1 and msgCode == -1:
        msg = "You must choose a non-empty bin, Player One"
    elif not(player1) and msgCode == -1:
        msg = "You must choose a non-empty bin, Player Two"
    elif player1 and msgCode == -3:
        msg = "Invalid Input. Try again Player One"
    elif not(player1) and msgCode == -3:
        msg = "Invalid Input. Try again Player Two"
    print("")
    print(msg)
    print("") 
    msgCode = 0   
    
   
    i = 0          #index variable
    for seed in pitseeds:
        pitseeds[i] = int(pitseeds[i] )
        if int(pitseeds[i]) < 10:
            pitseeds[i] = " " + str(pitseeds[i])
        else:
            pitseeds[i] = str()
        i = i + 1
        #end of the loop
        
    print("")
    
    print("        l    k    j    i    h    g")
    print("+----+----+----+----+----+----+----+----+")
    print("|    | "+ pitseeds[12] +" | "+ pitseeds[11] +" | "+ pitseeds[10] +" | "+ pitseeds[9] +" | "+ pitseeds[8] +" | "+ pitseeds[7] +" |    |")
    print("| "+ pitseeds[13] +" |----+----+----+----+----+----| "+ pitseeds[6] +" |")
    print("|    | "+ pitseeds[0] +" | "+ pitseeds[1] +" | "+ pitseeds[2] +" | "+ pitseeds[3] +" | "+ pitseeds[4] +" | "+ pitseeds[5] +" |    |")
    print("+----+----+----+----+----+----+----+----+")
    
    
    
    print("        a    b    c    d    e    f")
    print("")
    userInput = input ("Enter a letter to choose a bin or 'q' to QUIT the game: ")
    
    if userInput == "q":
        playing = False
    elif player1 and userInput == "a":
        selectedBin = 0
    elif player1 and userInput == "b":
        selectedBin = 1
    elif player1 and userInput == "c":
        selectedBin = 2
    elif player1 and userInput == "d":
        selectedBin = 3
    elif player1 and userInput == "e":
        selectedBin = 4
    elif player1 and userInput == "f":
        selectedBin = 5
    elif not(player1) and userInput == "l":
        selectedBin = 12
    elif not(player1) and userInput == "k":
        selectedBin = 11
    elif not(player1) and userInput == "j":
        selectedBin = 10
    elif not(player1) and userInput == "i":
        selectedBin = 9
    elif not(player1) and userInput == "h":
        selectedBin = 8
    elif not(player1) and userInput == "g":
        selectedBin = 7
    else:
        selectedBin = -2
        msgCode = -2  #invalid input
       
   
 
    if int(selectedBin) >= 0:
        takeawayPile = pitseeds[selectedBin]  
        
        if int(takeawayPile) > 0:
            
            ######## INSTEAD OF THIS PART BELOW WE NEED A LOGIC THAT MOVES OUR PILES CLOCKWISE
            userInput = input ("Enter a letter to distribute seeds or 'q' to QUIT the game: ")
            
            if userInput == "q":
                playing = False
            elif not(player1) and userInput == "a":
                selectedBin2 = 0
            elif not(player1) and userInput == "b":
                selectedBin2 = 1
            elif not(player1) and userInput == "c":
                selectedBin2 = 2
            elif not(player1) and userInput == "d":
                selectedBin2 = 3
            elif not(player1) and userInput == "e":
                selectedBin2 = 4
            elif not(player1) and userInput == "f":
                selectedBin2 = 5
            elif player1 and userInput == "l":
                selectedBin2 = 12
            elif player1 and userInput == "k":
                selectedBin2 = 11
            elif player1 and userInput == "j":
                selectedBin2 = 10
            elif player1 and userInput == "i":
                selectedBin2 = 9
            elif player1 and userInput == "h":
                selectedBin2 = 8
            elif player1 and userInput == "g":
                selectedBin2 = 7
            else:
                selectedBin2 = -3
                msgCode = -3  #invalid input
            
                ###### UNTIL HERE
            if selectedBin2 >= 0:
                pitseeds[selectedBin2] = str( int(pitseeds[selectedBin2]) + int(takeawayPile))
                pitseeds[selectedBin] = str(0)
                player1 = not(player1)
        else:
            msgCode = -1 # empty bin was chosen
        
#  how to pick the seed
# how to distribute the seed
# assign the players
# how players take turns
#  make sure the player select a valid pit
# how to determine who wins 