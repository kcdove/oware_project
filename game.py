# creating the board
# total_number_of_seeds = 48
#  total_number_of_pits = 12
pitseeds = [ 4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4]

playing = True

while(playing):
    i = 0
    for element in pitseeds:
        if int(pitseeds[i]) < 10:
            pitseeds[i] = str(pitseeds[i])
    print("")
    print("+----+----+----+----+----+----+----+----+----+")
    print("|    |    |    |    |    |    |    |    |    |")
    print("|    |----+----+----+----+----+----+----|    |")
    print("|    |    |    |    |    |    |    |    |    |")
    print("+----+----+----+----+----+----+----+----+----+")
    print("")
    userInput = input ("Enter 'q' to QUIT the game: ")
    
    if userInput == "q":
        playing = False   