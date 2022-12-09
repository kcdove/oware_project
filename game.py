
# creating the board
# total_number_of_seeds = 48
#  total_number_of_pits = 12
pitseeds = [ 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4] # this is an array of the number of seed in the pit

playing = True

# player1 = input ("players one: enter your name: ")


player1 = True

msgcode = 0

while(playing):
    # a tuple of the player's pits
    if player1 and msgcode == 0:
       msg = ("player1's Turn. chose from a-f")
    elif not(player1) and msgcode == 0:
       msg = ("player2's Turn. chose from g-l" )
    # elif player1 and msgcode == -2:
    #    msg = "Invalid input. Try again, player1"  
    # elif not(player1) and msgcode == -2:
    #    msg = "Invalid input. Try again, player2" 
    elif player1 and msgcode == -1:
        msg = ("you must choose a non-empty bin, player1")
    elif not(player1) and msgcode == -1:
        msg = ("you must choose a non-empty bin, player2")
    print("")
    print(msg)
    print("")
    msgcode = 0
    
    i = 0          #index variable
    for seed in pitseeds:
        pitseeds[i] = int(pitseeds[i] )
        if int(pitseeds[i]) < 13:
            pitseeds[i] = " " + str(pitseeds[i])
        else:
            pitseeds[i] = str()
        i = i + 1
        
        
    print("")
   
    print("   l    k    j    i    h    g")
    print("+----+----+----+----+----+----+")
    print("| "+ pitseeds[11] +" | "+ pitseeds[10] +" | "+ pitseeds[9] +" | "+ pitseeds[8] +" | "+ pitseeds[7] +" | "+ pitseeds[6] +" |")
    print("|----+----+----+----+----+----|")
    print("| "+ pitseeds[0] +" | "+ pitseeds[1] +" | "+ pitseeds[2] +" | "+ pitseeds[3] +" | "+ pitseeds[4] +" | "+ pitseeds[5] +" |")
    print("+----+----+----+----+----+----+")
    
    print("   a    b    c    d    e    f")
    print("")
   
    userInput = input ("Enter a letter to choose a pit or 'q' to QUIT the game: ") 
    
    if userInput == "q":
        selectedpit = 0 
        playing = False
   
    elif player1 and userInput == "a":  #  how to pick the seed
        selectedpit = 0 
    elif player1 and userInput == "b":
        selectedpit = 1 
    elif player1 and userInput == "c":
        selectedpit = 2
    elif player1 and userInput == "d":
        selectedpit = 3
    elif player1 and userInput == "e":
        selectedpit = 4 
    elif player1 and userInput == "f":
        selectedpit = 5 
    elif not(player1) and userInput == "g":
        selectedpit = 6    
    elif not(player1) and userInput == "h":
        selectedpit = 7               
    elif not(player1) and userInput == "i":
        selectedpit = 8               
    elif not(player1) and userInput == "j":
        selectedpit = 9               
    elif not(player1) and userInput == "k":
        selectedpit = 10
    elif not(player1) and userInput == "l":
        selectedpit = 11     
    else:
        selectedpit = -2
        msgcode = -2    #Invalid input
        
    if int(selectedpit) >= 0:
        seedsow = pitseeds[selectedpit]
        pitseeds[selectedpit] = 0
        if int(seedsow) <= 1:
            msgcode = -1   #empty bin was chosen
       
                 #    how to distribute the seed # 
                 
    recievingpit = selectedpit + 1
    if recievingpit == 12:
        recievingpit = 0

    while (int(seedsow) > 0): 
        if (player1 and (int(recievingpit))== 11):
            recievingpit = 0
        pitseeds[recievingpit] = int(pitseeds[recievingpit]) + 1  
        seedsow = int(seedsow) - 1
        recievingpit = int(recievingpit) + 1
        if int (recievingpit) > 11:
           recievingpit = 0   
            
        # if recievingpit > 1  and seedsow == 1:  
        #     # seedsow = int(seedsow) - 1 
        #      pitseeds[recievingpit] = int(pitseeds[recievingpit]) + 1  
        # seedsow = int(seedsow) - 1
        # recievingpit = int(recievingpit) + 1
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
        
        # # if seedsow == 1 and recievingpit >= 1:
        # #     pitseeds[recievingpit] = int(pitseeds[recievingpit]) 
        # #     print (pitseeds[recievingpit])
        # #     player1 = not(player1) 
       
    
    
    
    
        #      #how to redistribute the seed
    

    player1 = not(player1)         
               
# when its invalid iput player1 it should b player1 turn to play
# how to distribute the seed

# how to determine who wins 