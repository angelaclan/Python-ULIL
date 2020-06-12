from card import Card 
import sys
print(sys.argv[1:])
playerOne = [Card() for i in range(int(sys.argv[1]))]
playerTwo = [Card() for i in range(int(sys.argv[1]))]

table = []
while len(playerOne) > 0 and len(playerTwo) > 0:
    cardPlayerOne = playerOne[0]
    cardPlayerTwo = playerTwo[0]
    playerOne = playerOne[1:]
    playerTwo = playerTwo[1:]

    print (" player one plays")
    cardPlayerOne.printCard()
    print (" player two plays")
    cardPlayerTwo.printCard()
    table.append(cardPlayerOne)
    table.append(cardPlayerTwo)
    
    if cardPlayerOne.compare(cardPlayerTwo) == 1:
        print('win')
        playerOne.extend(table)
        table = []
        
    elif cardPlayerOne.compare(cardPlayerTwo) == -1:
        print('lose')
        playerTwo.extend(table)
        table = []
        
    else:
        print('war')
    

            
