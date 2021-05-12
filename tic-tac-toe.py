import time 
import random
import os


# board=[' ']*10
def Clear():
    os.system("Clear")

#instruction or help for the game
def ttt_instructions():
    print("Instruction for Tic Tac Toe game")
    print("When all 9 squares are full, the game will draw")
    print("If a player places their symbol, either diagonally or in a straight row or in a straight column then He/She is going to win the game")
    print("Position's on Tic Tac Toe board")
    print("------------------------------------------")
    print( "1" + "   |  " + "2" +  "  |   " + "3"  )
    print("____|_____|____")
    print(  "4"+  "   |  "+  "5"  +"  |   "+  "6")
    print("____|_____|____")
    print("    |     |    ")
    print(  "7"  +"   |  " + "8" +  "  |   " + "9" )
    print("------------------------------------------")

    time.sleep(3)

# display board
def display_board():
    print( board[1] + "   |  " + board[2] +  "  |   " + board[3]  )
    print("____|_____|____")
    print(  board[4]+  "   |  "+  board[5]  +"  |   "+  board[6]  )
    print("____|_____|____")
    print("    |     |    ")
    print(  board[7]  +"   |  " + board[8] +  "  |   " + board[9] )

#condition to win the game
def game_win(board,marker):
    while True:
        if (board[1]==marker and board[2]==marker and board[3]==marker) or (board[4]==marker and board[5]==marker and board[6]==marker) or (board[7]==marker and board[8]==marker and board[9]==marker) or (board[1]==marker and board[4]==marker and board[7]==marker) or (board[2]==marker and board[5]==marker and board[8]==marker) or (board[3]==marker and board[6]==marker and board[9]==marker) or (board[1]==marker and board[5]==marker and board[9]==marker) or (board[3]==marker and board[5]==marker and board[7]==marker):
            if 'X'==marker:
                return "X_win" 
                # break
            else:
                return "O_win"
                # break
        else:
            # print("Game not over!")
            break

# tic_tac_toe_play
def tic_tac_toe_play():
    while True:
        print("Game started!")
        user1=input("Enter the name of 1st player : ").capitalize()
        user2=input("Enter the name of 2nd player : ").capitalize()

        user_list=[user1,user2]

        player=random.choice(user_list)
        display_board()
        if player==user1:
            user2=user2
        else:
            user2=user1
            user1=player
                        

        # validation of Marker 
        user1_marker=input(f"{player} Enter your marker ('X','O') :").upper()
        while user1_marker not in ["X","O"]:
            user1_marker=input(f"{player} Enter your marker ('X','O') :").upper()

        user2_marker=""

        if user1_marker=="X":
            user2_marker="O"
        else:
            user2_marker="X"
        count=0
        flage=0
        while True:
            if flage==0:
                if count<9:
                    # validation of position on the board for player 1
                    valid1=False
                    while not valid1:
                        player1_move=int(input(f"{user1} your postion on the tic-tac-toe grid between 1-9 :"))
                        while player1_move not in [1,2,3,4,5,6,7,8,9]:
                            player1_move=int(input(f"{user1} your postion on the tic-tac-toe grid between 1-9 :"))

                        #to check weather position is occupied or not
                        if board[player1_move]==" ":
                            count+=1
                            valid1=True
                            board[player1_move]=user1_marker
                            #to check the user win the match or not
                            if game_win(board,user1_marker)==f"{user1_marker}_win":
                                flage+=1
                                display_board()
                                print(f"{user1} you have won the match")
                                board.clear()
                                time.sleep(2)
                                break
                        else:
                            print(f"{user1},This position is occupied")
                        display_board()

                else:
                    print("Game draw!")
                    board.clear() 
                    break 
            else:
                break
            if flage==0:
                if count<9:
                    # validation of position on the board for player 2
                    valid2=False
                    while not valid2:
                        player2_move=int(input(f"{user2} your position on the tic-tac-toe grid between 1-9 :"))
                        while player2_move not in [1,2,3,4,5,6,7,8,9]:
                            player2_move=int(input(f"{user2} your position on the tic-tac-toe grid between 1-9 :"))

                        #to check weather position is occupied or not
                        if board[player2_move]==" ":
                            count+=1
                            valid2=True
                            board[player2_move]=user2_marker
                            #to check the user win the match or not
                            if game_win(board,user2_marker)==f"{user2_marker}_win":
                                flage+=1
                                display_board()
                                print(f"{user2} you have won the match")
                                board.clear()
                                time.sleep(2)
                                break
                        else:
                            print(f"{user2} ,This position is occupied")
                        display_board()
                else:
                    print("Game draw!")
                    board.clear() 
                    break 
            else:
                break
        break

# tic_tac_toe_play()

if __name__ == '__main__':
    
    #this is the Game Loop
    while True:
        print("***********")
        print("Let's Play!!!")
        print("Enter 1 to play Tic Tac Toe")
        print("Enter 2 for Instruction or Help")
        # print("Enter 3 to see the match_info")
        print("Enter 3 to quit the match")
        print("***********")


        # Try block to handle the player choice 
        try:
            Choice=int(input("Enter your choice:"))
        except ValueError:
            Clear()
            print("Wrong Choice")
            continue
        # to play the Tic Tac Toe game
        if Choice==1:
            # this this our Tic Tac Toe grid or board
            board=[" "]*10
            Clear()
            # board.clear() 
            tic_tac_toe_play()
        # for instruction or help
        elif Choice==2:
            Clear()
            ttt_instructions()
        # for quitting the Game loop
        elif Choice==3:
            break
        # Other wrong input
        else:
            Clear()
            print("Wrong choice. Read instructions carefully.")  