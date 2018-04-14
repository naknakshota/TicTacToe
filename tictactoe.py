#*******************************************************************
#                         Tic-Tac-Toe Game
#                        Author: Shota Nakamura
# Objective: Create a playable nxn Tic-Tac-Toe Board. 
#            Opponent will choose random placement on board.
#Note: This is the very basic TicTacToe game.
#*******************************************************************
import random

class TicTacToe():
    """
    TicTacToe game
    """

    def __init__(self, n): #board initialized as n*n where n is number of rows 
        self.n = n
        self.board = [([('-') for x in range(self.n)]) for y in range(self.n)] 

    def display(self): 
        for i in self.board:
            print(''.join(str(x) for x in i))
    
    def wonGame(self,r):
        #check if elements are equal
        self.r = r
        #Case for Horizontal	
        for i in self.board:
           if(all(k == 'o' for k in i) or all(k == 'x' for k in i)):
                return True
        #Case for Vertical
        for j in range(r):
           newList = [k[j] for k in self.board]
           if(all(p == 'o' for p in newList) or (all(p == 'x' for p in newList))):
                   return True
        #Case for Right-to-Left Diagonal
        for j in range(r):
           newList = []
           for k in range(r):
               newList.append(self.board[k][k])
           if(all(p == 'o' for p in newList) or (all(p == 'x' for p in newList))):
               return True 
        #Case for Left-to-Right Diagonal
        for j in range(r):
            newList = []
            q = r-1
            for k in range(r):
                newList.append(self.board[k][q])
                q -= 1
            if(all(p == 'o' for p in newList) or (all(p == 'x' for p in newList))):
                return True
   
    def updatePlayerState(self,r,c): #Updates Player State
        self.r = r #row access val in state 
        self.c = c #column access val in state
        if(self.board[self.r][self.c] == '-'):
            self.board[self.r][self.c] = 'o'
        else:
            print("Board Space already filled. Try Again.")
            #Here we will return a value that will prompt server to try again.
            return (70)
            #You need to call something here.

    def updateServerState(self, r): #Updates Server State
        random.seed()
        x = random.randint(0,r-1)
        y = random.randint(0,r-1)
        if(self.board[x][y] == '-'):
            self.board[x][y] = 'x'
        else:
            self.updateServerState(r)

    def fullBoard(self,r,m): 
        #Checks if the board is full
        if(m >= r*r):
            return True
      
class Server():
    """
    Server for TicTacToe game
    """

    def __init__(self):
        print('Starting New Game')

    def play(self):
        print("==================")
        print("| TicTacToe Game |")
        print("==================\n")
        self.moves = 0 #Keeps count to check whether board is full
        self.rows = int(input("Enter number of rows in TicTacToe board: "))
        t = TicTacToe(self.rows)
        t.display()
        while(self.moves != (self.rows*self.rows)):
           print("Player Move: \n")

           #playerInput() will set restrictions on player input
           (p,q) = self.playerInput()

           #updatePlayerState will Mark 'o' for user input with some restrictions
           if(t.updatePlayerState(p,q) != 70): #note that 70 is the indication for invalid board space here
               t.updatePlayerState
           else:
               (p,q) = self.playerInput()
               t.updatePlayerState(p,q)
           
           #Increment moves everytime a move has been made
           self.moves += 1

           #Checks if a winning move has been made
           if(t.wonGame(self.rows)): 
               print("You have won the Game")
               break
           #Checks if the board is full
           if(t.fullBoard(self.rows,self.moves)): 
               print("Tie Game")
               break
           #display the board
           t.display()

           #Randomly places a server move ('x')
           t.updateServerState(self.rows) 
           print("Server Move: \n")
           t.display()

           #Checks if the board is full
           if(t.wonGame(self.rows)): 
               print("You have lost the Game")
               break
           self.moves += 1

    def playerInput(self):
      k = -1
      j = -1
      #Restrict User Input for rows
      while(k < 0 or k > self.rows-1): 
          try:
              k = int(input("Choose row[0-"+str(self.rows-1)+"]: "))
          except ValueError:
              print("Input Out Of Bounds. Try Again")
      
      #Restrict User Input for Columns  
      while(j < 0 or j > self.rows-1): 
          try:
              j = int(input("Choose column[0-"+str(self.rows-1)+"]: "))
          except ValueError:
              print("Input Out of Bounds. Try Again")

      return (k,j) #We will use what is returned here


def main():
    s = Server()
    s.play()

if __name__ == '__main__':
    main()
