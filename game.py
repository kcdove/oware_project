
# creating the board
# total_number_of_seeds = 48
#  total_number_of_pits = 12
pitseeds = [ 4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0] # this is an array of the number of seed in the pit

playing = True

Player1_pit = ('a', 'b', 'c', 'd', 'e', 'f')
player2_pit = ('g', 'h', 'i', 'j', 'k', 'l')

while(playing):
    # a tuple of the player's pits
    player1 = Player1_pit
    if player1:
        say = ("player1s' Turn. chose from g-l")
    else:
        say =("invalid pit")
    player2 = player2_pit
    if player2:
        say = ("player2s' Turn. chose from g-l")
    else:
        say =("invalid pit")
    print(say)
    
   
    i = 0          #index variable
    for seed in pitseeds:
        pitseeds[i] = int(pitseeds[i] )
        if int(pitseeds[i]) < 10:
            pitseeds[i] = " " + str(pitseeds[i])
        else:
            pitseeds[i] = str()
        i = i + 1
    print("")
    if player2:
        print("        l    k    j    i    h    g")
    print("+----+----+----+----+----+----+----+----+")
    print("|    | "+ pitseeds[12] +" | "+ pitseeds[11] +" | "+ pitseeds[10] +" | "+ pitseeds[9] +" | "+ pitseeds[8] +" | "+ pitseeds[7] +" |    |")
    print("| "+ pitseeds[13] +" |----+----+----+----+----+----| "+ pitseeds[6] +" |")
    print("|    | "+ pitseeds[0] +" | "+ pitseeds[1] +" | "+ pitseeds[2] +" | "+ pitseeds[3] +" | "+ pitseeds[4] +" | "+ pitseeds[5] +" |    |")
    print("+----+----+----+----+----+----+----+----+")
    
    
    if player1:
        print("        a    b    c    d    e    f")
        print("")
    userInput = input ("Enter 'q' to QUIT the game: ")
    
    if userInput == "q":
        playing = False
        
#  how to pick the seed
# how to distribute the seed
# assign the players
# how players take turns
#  make sure the player select a valid pit
# how to determine who wins 