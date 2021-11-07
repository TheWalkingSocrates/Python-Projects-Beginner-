# A Tic Tac Toe Game played by 2 players


board = {'7': ' ' ,'8': ' ' ,'9': ' ' ,
         '4': ' ' ,'5': ' ' ,'6': ' ' ,
         '1': ' ' ,'2': ' ' ,'3': ' ' }

keys = []

for key in board:
    keys.append(key)

def printBoard(board):
    print(f"{board['7']} | {board['8']} | {board['9']} ")
    print("- o - o -")
    print(f"{board['4']} | {board['5']} | {board['6']} ")
    print("- o - o -")
    print(f"{board['1']} | {board['2']} | {board['3']} ")
    
def game():
    turn = 'X'
    count = 0
    print(f"Your turn {turn} .Move to which place?")
    

    for i in range(10):
        printBoard(board)
        print("It's your turn," + turn + ".Move to which place?")
        move = input()
        #If the specific board place is empty , it'll add the player's turn to that place
        if board[move]  == ' ':
            board[move] = turn
            count +=1
        else:
            print('This Place is already filled. Please select a new place')
            continue

        if count >=5:
            if(board['7'] == board['8'] == board['9'] != ' ' or 
             (board['4'] == board['5'] == board['6'] != ' ') or 
             (board['1'] == board['2'] == board['3'] != ' ') or 
             (board['1'] == board['4'] == board['7'] != ' ') or 
             (board['2'] == board['5'] == board['8'] != ' ') or
             (board['3'] == board['6'] == board['9'] != ' ') or 
             (board['1'] == board['5'] == board['9'] != ' ') or 
             (board['3'] == board['5'] == board['7'] != ' ')) :   
                printBoard(board)
                print("\nGame Over.\n")                
                print(f" **** {turn} won. ****")                
                break

        if count == 9 :
            print("Game Over")
            print("It's a Tie!")
        
        if turn == 'X' :
            turn = 'O'
        else :
            turn = 'X'

    restart = input("Do want to play Again?(y/n)")
    if restart == "y" or restart == "Y":  
        for key in keys:
            board[key] = " "

if __name__ == '__main__':
    game()
