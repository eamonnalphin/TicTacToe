#Tic Tac Toe
import random

print("Tic Tac Toe")
print("A | B | C")
print("---------")
print("D | E | F")
print("---------")
print("G | H | I")

def XorO():
        humansChoice = input("X or O? ")
        humansChoice = humansChoice.upper()
        print(humansChoice)
        if humansChoice == "X":
            player1 = "human"
        else:
            player1 = "computer"
        return player1




def game1():
    #human in player 1, X's
    gamePlay = []
    compMoves = []
    humanMoves = []

    def openWinSaveFile():
        WinSaveFile = []
        with open("savedOWins.txt") as File:
            for line in File:
                WinSaveFile.append(line)
        File.close()
        return WinSaveFile

    def openTieSaveFile():
        TieSaveFile = []
        with open("savedOTies.txt") as File:
            for line in File:
                TieSaveFile.append(line)
        File.close()
        return TieSaveFile
    

    WinningStrategies = openWinSaveFile()
    TyingStrategies = openTieSaveFile()

    def addToWinning(gamePlay, WinningStrategies):
        WinningStrategies+=[gamePlay]
        savedWins = open("savedOWins.txt","w")

        for strategy in WinningStrategies:
            savedWins.writelines("%s\n" %strategy)
        savedWins.close()
        return WinningStrategies

    def addToTying(gamePlay, TyingStrategies):
        TyingStrategies+=[gamePlay]
        savedTies = open("savedOTies.txt","w")

        for strategy in TyingStrategies:
            savedTies.writelines("%s\n" %strategy)
        savedTies.close()
        return TyingStrategies



    def convertToString(Array):
        output = "".join(str(x) for x in Array)
        return output



    def checkStrategies(gamePlay,WinningStrategies,TyingStrategies,compMoves,humanMoves):
        nextMove = "0"
        print("gameplay length:" +str(len(gamePlay)))

        if len(gamePlay) == 0:
            #print("gamestart move")
            nextMove = "E"
                
        if nextMove == "0":
            print("offense")
            #print(compMoves)
            nextMove = oneMoveToWin(compMoves,gamePlay)

        
        if nextMove == "0":
            print("defense")
            #print(humanMoves)
            nextMove = oneMoveToWin(humanMoves,gamePlay)


        if nextMove == "0":
            print("checking for a winning strategy")
            for strategy in WinningStrategies:
                strategyString = convertToString(strategy)
                #print(strategyString)
                moveString = convertToString(gamePlay)
                #print(moveString)
                if moveString in strategyString:
                    #print("found match")
                    nextMove = strategyString[len(moveString)]
                    break


        if nextMove == "0":
            print("checking for a tying strategy")
            for strategy in TyingStrategies:
                strategyString = convertToString(strategy)
                moveString = convertToString(gamePlay)
                if moveString in strategyString:
                    nextMove = strategyString[len(moveString)]
                    break
        
        if nextMove == "0":
            print("making random move")
            availableMoves = availableMovesCheck(gamePlay)
            nextMove = randomMove(availableMoves)

    
        return nextMove





    def displayGrid(compMoves,humanMoves):
        one = ["A","B","C"]
        two = ["D","E","F"]
        three = ["G","H","I"]
        

        for move in humanMoves:
            if move == "A":
                one[0] = "X"
            elif move == "B":
                one[1] = "X"
            elif move == "C":
                one[2] = "X"
            elif move == "D":
                two[0] = "X"
            elif move == "E":
                two[1] = "X"
            elif move == "F":
                two[2] = "X"
            elif move == "G":
                three[0] = "X"
            elif move == "H":
                three[1] = "X"
            elif move == "I":
                three[2] = "X"
            
        for move in compMoves:
            if move == "A":
                one[0] = "O"
            elif move == "B":
                one[1] = "O"
            elif move == "C":
                one[2] = "O"
            elif move == "D":
                two[0] = "O"
            elif move == "E":
                two[1] = "O"
            elif move == "F":
                two[2] = "O"
            elif move == "G":
                three[0] = "O"
            elif move == "H":
                three[1] = "O"
            elif move == "I":
                three[2] = "O"

        print(one[0]+" | "+one[1]+" | "+one[2])
        print("---------")
        print(two[0]+" | "+two[1]+" | "+two[2])
        print("---------")
        print(three[0]+" | "+three[1]+" | "+three[2])


        


    def numbers_to_strings(argument):
        switcher = {
            0: "A",
            1: "B",
            3: "C",
            4: "D",
            5: "E",
            6: "F",
            7: "G",
            8: "H",
            9: "I",
            
        }
        return switcher.get(argument, "E")


    def randomMove(remainingMoves):
        randomAvailableMove = random.randint(0,len(remainingMoves)-1)
        nextMove = remainingMoves[randomAvailableMove]
        return nextMove

    def humanMove():
        currentMove = input("Choose a free space:")
        return currentMove.upper()


    def availableMovesCheck(gamePlay):
        allMoves = ["A","B","C","D","E","F","G","H","I"]
        remainingMoves = allMoves
        match = False
        for move in gamePlay:
            for space in allMoves:
                if move == space:
                    remainingMoves.remove(move)
        print("remaining moves:")
        print(remainingMoves)
        return remainingMoves
                    
                


    def checkMove(currentMove, gamePlay):
        repeat = True
        while repeat == True:
            taken = False
            #check the entire array to see if the space is taken:
            for i in range(0,len(gamePlay)):
                if gamePlay[i] == currentMove:
                    taken = True
                    repeat = False
            repeat = False
        return taken


    def oneMoveToWin(moveList,gamePlay):
        W1 = ["A","B","C"]
        W2 = ["A","E","I"]
        W3 = ["A","D","G"]
        W4 = ["B","E","H"]
        W5 = ["C","E","G"]
        W6 = ["D","E","F"]
        W7 = ["G","H","I"]
        W8 = ["C","F","I"]

        combos = [W1,W2,W3,W4,W5,W6,W7,W8]

        for winningCombo in combos:
            match = 0
            nextMove = "0"
            taken = False
            takenCheck = True
            for spot in winningCombo:
                taken = checkMove(spot,gamePlay)
                #print(spot+" is "+ str(taken))
                for space in moveList:
                    #print(spot + " vs " + space)
                    if spot==space:
                        #print("match")
                        match+=1
                    if spot!=space and taken==False:
                        nextMove=spot
                        takenCheck = False
                    if match >= 2 and takenCheck == False:
                        #print(nextMove)
                        #print("match = 2 and the spot is free")
                        return nextMove
                    
        nextMove = "0"
        return nextMove
        


         

    def winCheck(moveList):
        W1 = ["A","B","C"]
        W2 = ["A","E","I"]
        W3 = ["A","D","G"]
        W4 = ["B","E","H"]
        W5 = ["C","E","G"]
        W6 = ["D","E","F"]
        W7 = ["G","H","I"]
        W8 = ["C","F","I"]

        combos = [W1,W2,W3,W4,W5,W6,W7,W8]


        
        for winningCombo in combos:
            match = 0
            for spot in winningCombo:
                for space in moveList:
                    if spot==space:
                        match+=1
            if match == 3:
                return True


    def main(WinningStrategies, TyingStrategies):
        gamePlay = []
        compMoves = []
        humanMoves = []


        currentSpace = 0
        compSpace = 0
        humanSpace = 0
 
        
        playAgain = "Y"
        
        while playAgain == "Y":
            while currentSpace != 9:
                turn = "human"
                print("Human\'s turn")
                while turn == "human":
                    currentMove = humanMove()
                    taken = checkMove(currentMove,gamePlay)

                    if taken == False:
                        gamePlay.append(currentMove)
                        humanMoves.append(currentMove)
                        humanWin = winCheck(humanMoves)

                        displayGrid(compMoves,humanMoves)
                        
                        if humanWin == True:
                            print("You Win!")
                            break

                        turn = "computer"

                currentSpace+=1
                humanSpace+=1

                if humanWin == True:
                    break

                if currentSpace == 9:
                    print("Draw...")
                    TyingStrategies = addToTying(gamePlay, TyingStrategies)
                    break

                print('Computer\'s turn')
                while turn == "computer":
                    #currentMove = randomMove()
                    currentMove = checkStrategies(gamePlay, WinningStrategies,TyingStrategies,compMoves,humanMoves)
                    if (not currentMove.isalpha()):
                        currentMove = randomMove(availableMovesCheck(gamePlay))
                    
                    taken = checkMove(currentMove,gamePlay)
                    if taken == False:
                        print("Computer's move: " + currentMove)
                        gamePlay.append(currentMove)
                        compMoves.append(currentMove)
                        computerWin = winCheck(compMoves)
                        displayGrid(compMoves,humanMoves)
                        
                        if computerWin == True:
                            WinningStrategies = addToWinning(gamePlay, WinningStrategies)
                            print("Computer Wins!")
                            break

                        turn = "human"

                currentSpace+=1
                compSpace+=1

                if computerWin == True:
                    break
                
                if currentSpace == 9:
                    print("Draw...")
                    TyingStrategies = addToTying(gamePlay, TyingStrategies)
                    break


            while playAgain != "N":
                playAgain = input("Play Again? Y/N?")
                playAgain = playAgain.upper()
                if playAgain == "Y":
                    currentSpace == 0
                    currentSpace = 0
                    compSpace = 0
                    humanSpace = 0
                    print("A | B | C")
                    print("---------")
                    print("D | E | F")
                    print("---------")
                    print("G | H | I")
                    main(WinningStrategies, TyingStrategies)
                    break
                else:
                    print("Thanks for playing!")
                    import sys
                    sys.exit(0)
                
            
    
    main(WinningStrategies, TyingStrategies)


##################################################################################################

def game2():
    gamePlay = []
    compMoves = []
    humanMoves = []            

    def openWinSaveFile():
        WinSaveFile = []
        with open("savedXWins.txt") as File:
            for line in File:
                WinSaveFile.append(line)
        File.close()
        return WinSaveFile

    def openTieSaveFile():
        TieSaveFile = []
        with open("savedXTies.txt") as File:
            for line in File:
                TieSaveFile.append(line)
        File.close()
        return TieSaveFile
    

    WinningStrategies = openWinSaveFile()
    TyingStrategies = openTieSaveFile()

    def addToWinning(gamePlay, WinningStrategies):
        WinningStrategies+=[gamePlay]
        savedWins = open("savedXWins.txt","w")

        for strategy in WinningStrategies:
            savedWins.writelines("%s\n" %strategy)
        savedWins.close()
        return WinningStrategies

    def addToTying(gamePlay, TyingStrategies):
        TyingStrategies+=[gamePlay]
        savedTies = open("savedXTies.txt","w")

        for strategy in TyingStrategies:
            savedTies.writelines("%s\n" %strategy)
        savedTies.close()
        return TyingStrategies



    def convertToString(Array):
        output = "".join(str(x) for x in Array)
        return output



    def checkStrategies(gamePlay,WinningStrategies,TyingStrategies,compMoves,humanMoves):
        nextMove = "0"
        print("gameplay length:" +str(len(gamePlay)))

        if len(gamePlay) == 0:
            #print("gamestart move")
            nextMove = "E"
                
        if nextMove == "0":
            print("offense")
            #print(compMoves)
            nextMove = oneMoveToWin(compMoves,gamePlay)

        
        if nextMove == "0":
            print("defense")
            #print(humanMoves)
            nextMove = oneMoveToWin(humanMoves,gamePlay)


        if nextMove == "0":
            print("checking for a winning strategy")
            for strategy in WinningStrategies:
                strategyString = convertToString(strategy)
                #print(strategyString)
                moveString = convertToString(gamePlay)
                #print(moveString)
                if moveString in strategyString:
                    #print("found match")
                    nextMove = strategyString[len(moveString)]
                    break


        if nextMove == "0":
            print("checking for a tying strategy")
            for strategy in TyingStrategies:
                strategyString = convertToString(strategy)
                moveString = convertToString(gamePlay)
                if moveString in strategyString:
                    nextMove = strategyString[len(moveString)]
                    break
        
        if nextMove == "0":
            print("making random move")
            availableMoves = availableMovesCheck(gamePlay)
            nextMove = randomMove(availableMoves)

    
        return nextMove





    def displayGrid(compMoves,humanMoves):
        one = ["A","B","C"]
        two = ["D","E","F"]
        three = ["G","H","I"]
        

        for move in compMoves:
            if move == "A":
                one[0] = "X"
            elif move == "B":
                one[1] = "X"
            elif move == "C":
                one[2] = "X"
            elif move == "D":
                two[0] = "X"
            elif move == "E":
                two[1] = "X"
            elif move == "F":
                two[2] = "X"
            elif move == "G":
                three[0] = "X"
            elif move == "H":
                three[1] = "X"
            elif move == "I":
                three[2] = "X"
            
        for move in humanMoves:
            if move == "A":
                one[0] = "O"
            elif move == "B":
                one[1] = "O"
            elif move == "C":
                one[2] = "O"
            elif move == "D":
                two[0] = "O"
            elif move == "E":
                two[1] = "O"
            elif move == "F":
                two[2] = "O"
            elif move == "G":
                three[0] = "O"
            elif move == "H":
                three[1] = "O"
            elif move == "I":
                three[2] = "O"

        print(one[0]+" | "+one[1]+" | "+one[2])
        print("---------")
        print(two[0]+" | "+two[1]+" | "+two[2])
        print("---------")
        print(three[0]+" | "+three[1]+" | "+three[2])


        


    def numbers_to_strings(argument):
        switcher = {
            0: "A",
            1: "B",
            3: "C",
            4: "D",
            5: "E",
            6: "F",
            7: "G",
            8: "H",
            9: "I",
            
        }
        return switcher.get(argument, "E")


    def randomMove(remainingMoves):
        randomAvailableMove = random.randint(0,len(remainingMoves)-1)
        nextMove = remainingMoves[randomAvailableMove]
        return nextMove

    def humanMove():
        currentMove = input("Choose a free space:")
        return currentMove.upper()


    def availableMovesCheck(gamePlay):
        allMoves = ["A","B","C","D","E","F","G","H","I"]
        remainingMoves = allMoves
        match = False
        for move in gamePlay:
            for space in allMoves:
                if move == space:
                    remainingMoves.remove(move)
        print("remaining moves:")
        print(remainingMoves)
        return remainingMoves
                    
                


    def checkMove(currentMove, gamePlay):
        repeat = True
        while repeat == True:
            taken = False
            #check the entire array to see if the space is taken:
            for i in range(0,len(gamePlay)):
                if gamePlay[i] == currentMove:
                    taken = True
                    repeat = False
            repeat = False
        return taken


    def oneMoveToWin(moveList,gamePlay):
        W1 = ["A","B","C"]
        W2 = ["A","E","I"]
        W3 = ["A","D","G"]
        W4 = ["B","E","H"]
        W5 = ["C","E","G"]
        W6 = ["D","E","F"]
        W7 = ["G","H","I"]
        W8 = ["C","F","I"]

        combos = [W1,W2,W3,W4,W5,W6,W7,W8]

        for winningCombo in combos:
            match = 0
            nextMove = "0"
            taken = False
            takenCheck = True
            for spot in winningCombo:
                taken = checkMove(spot,gamePlay)
                #print(spot+" is "+ str(taken))
                for space in moveList:
                    #print(spot + " vs " + space)
                    if spot==space:
                        #print("match")
                        match+=1
                    if spot!=space and taken==False:
                        nextMove=spot
                        takenCheck = False
                    if match >= 2 and takenCheck == False:
                        #print(nextMove)
                        #print("match = 2 and the spot is free")
                        return nextMove
                    
        nextMove = "0"
        return nextMove
        


         

    def winCheck(moveList):
        W1 = ["A","B","C"]
        W2 = ["A","E","I"]
        W3 = ["A","D","G"]
        W4 = ["B","E","H"]
        W5 = ["C","E","G"]
        W6 = ["D","E","F"]
        W7 = ["G","H","I"]
        W8 = ["C","F","I"]

        combos = [W1,W2,W3,W4,W5,W6,W7,W8]


        
        for winningCombo in combos:
            match = 0
            for spot in winningCombo:
                for space in moveList:
                    if spot==space:
                        match+=1
            if match == 3:
                return True


    def main(WinningStrategies, TyingStrategies):
        gamePlay = []
        compMoves = []
        humanMoves = []


        currentSpace = 0
        compSpace = 0
        humanSpace = 0
 
        
        playAgain = "Y"
        
        while playAgain == "Y":
            while currentSpace != 9:
                print('Computer\'s turn')
                turn = "computer"
                while turn == "computer":
                    #currentMove = randomMove()
                    currentMove = checkStrategies(gamePlay, WinningStrategies,TyingStrategies,compMoves,humanMoves)
                    taken = checkMove(currentMove,gamePlay)
                    if taken == False:
                        print(currentMove)
                        gamePlay.append(currentMove)
                        compMoves.append(currentMove)
                        computerWin = winCheck(compMoves)
                        displayGrid(compMoves,humanMoves)
                        
                        if computerWin == True:
                            WinningStrategies = addToWinning(gamePlay, WinningStrategies)
                            print("Computer Wins!")
                            break

                        turn = "human"

                currentSpace+=1
                compSpace+=1

                if computerWin == True:
                    break
                
                if currentSpace == 9:
                    print("Draw...")
                    TyingStrategies = addToTying(gamePlay, TyingStrategies)
                    break

                


                print("Human\'s turn")
                while turn == "human":
                    currentMove = humanMove()
                    taken = checkMove(currentMove,gamePlay)

                    if taken == False:
                        gamePlay.append(currentMove)
                        humanMoves.append(currentMove)
                        humanWin = winCheck(humanMoves)

                        displayGrid(compMoves,humanMoves)
                        
                        if humanWin == True:
                            print("You Win!")
                            break

                        turn = "computer"

                currentSpace+=1
                humanSpace+=1

                if humanWin == True:
                    break

                if currentSpace == 9:
                    print("Draw...")
                    TyingStrategies = addToTying(gamePlay, TyingStrategies)
                    break

           
            while playAgain != "N":
                playAgain = input("Play Again? Y/N?")
                playAgain = playAgain.upper()
                if playAgain == "Y":
                    currentSpace == 0
                    currentSpace = 0
                    compSpace = 0
                    humanSpace = 0
                    print("A | B | C")
                    print("---------")
                    print("D | E | F")
                    print("---------")
                    print("G | H | I")
                    main(WinningStrategies, TyingStrategies)
                    break
                else:
                    print("Thanks for playing!")
                    import sys
                    sys.exit(0)
                        
                
            
    
    main(WinningStrategies, TyingStrategies)



#MAIN COMMAND:
player1 = XorO()
if player1 == "human":
    print("You are player 1")
    game1()
else:
    print("Computer is player 1")
    game2()

