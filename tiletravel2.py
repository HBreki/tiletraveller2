def play():
    while True:
        NORTH = 'n'
        EAST = 'e'
        SOUTH = 's'
        WEST = 'w'
        
        def move(direction, col, row):
            ''' Returns updated col, row given the direction '''
            if direction == NORTH:
                row += 1
            elif direction == SOUTH:
                row -= 1
            elif direction == EAST:
                col += 1
            elif direction == WEST:
                col -= 1
            return(col, row)    
        
        def is_victory(col, row):
            ''' Return true is player is in the victory cell '''
            return col == 3 and row == 1 # (3,1)
        
        def print_directions(directions_str):
            print("You can travel: ", end ='')
            first = True
            for ch in directions_str:
                if not first:
                    print(" or ", end='')
                if ch == NORTH:
                    print("(N)orth", end='')
                elif ch == EAST:
                    print("(E)ast", end='')
                elif ch == SOUTH:
                    print("(S)outh", end='')
                elif ch == WEST:
                    print("(W)est", end='')
                first = False
            print(".")
                
        def find_directions(total, col, row):
            ''' Returns valid directions as a string given the supplied location '''
            if col == 1 and row == 1:   # (1,1)
                valid_directions = NORTH
            elif col == 1 and row == 2: # (1,2)
                total=lever(total) 
                valid_directions = NORTH+EAST+SOUTH
            elif col == 1 and row == 3: # (1,3)
                valid_directions = EAST+SOUTH
            elif col == 2 and row == 1: # (2,1)
                valid_directions = NORTH
            elif col == 2 and row == 2: # (2,2)
                total=lever(total)
                valid_directions = SOUTH+WEST
            elif col == 2 and row == 3: # (2,3)
                total=lever(total)
                valid_directions = EAST+WEST
            elif col == 3 and row == 2: # (3,2)
                total=lever(total)
                valid_directions = NORTH+SOUTH
            elif col == 3 and row == 3: # (3,3)
                valid_directions = SOUTH+WEST
            return valid_directions, total
        
        def play_one_move(col, row, valid_directions):
            ''' Plays one move of the game
                Return if victory has been obtained and updated col,row '''
            victory = False
            direction = input("Direction: ")
            direction = direction.lower()
            
            if not direction in valid_directions:
                print("Not a valid direction!")
            else:
                col, row = move(direction, col, row)
                victory = is_victory(col, row)
            return victory, col, row
        
        def lever(total):
            lever_question = input("Pull a lever (y/n): ")
            if lever_question == "y" or lever_question == "Y":
                total = total + 1
                print("You received 1 coin, your total is now", str(total)+".")
            return total 
            
        # The main program starts here
        victory = False
        row = 1
        col = 1
        total=0
            
        valid_directions = NORTH
        print_directions(valid_directions)
        
        while not victory:
            victory, col, row = play_one_move(col, row, valid_directions)
            if victory:
                print("Victory! Total coins", str(total)+".")
                play = input("Play again (y/n): ")
                if play == "y" or play == "Y":
                    pass
                else:
                    return
            else:
                valid_directions, total = find_directions(total, col, row)
                print_directions(valid_directions)
play()
