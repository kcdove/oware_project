# creating the board
# total_number_of_seeds = 48
#  total_number_of_pits = 12
pitseeds = [ 4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0] # this is an array of the number of seed in the pit

playing = True

while(playing):
    i = 0
    for element in pitseeds:
        pitseeds[i] = int(pitseeds[i] )
        if int(pitseeds[i]) < 10:
            pitseeds[i] = " " + str(pitseeds[i])
        else:
            pitseeds[i] = str()
        i = i + 1
    print("")
    print("+----+----+----+----+----+----+----+----+")
    print("|    | "+ pitseeds[12] +" | "+ pitseeds[11] +" | "+ pitseeds[10] +" | "+ pitseeds[9] +" | "+ pitseeds[8] +" | "+ pitseeds[7] +" |    |")
    print("| "+ pitseeds[13] +" |----+----+----+----+----+----| "+ pitseeds[6] +" |")
    print("|    | "+ pitseeds[0] +" | "+ pitseeds[1] +" | "+ pitseeds[2] +" | "+ pitseeds[3] +" | "+ pitseeds[4] +" |"+ pitseeds[5] +"  |    |")
    print("+----+----+----+----+----+----+----+----+")
    print("")
    userInput = input ("Enter 'q' to QUIT the game: ")
    
    if userInput == "q":
        playing = False   