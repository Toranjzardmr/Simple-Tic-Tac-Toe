'''
Game Display Format
"-------------"
"| 1 | 2 | 3 |"
"-------------"
"| 4 | 5 | 6 |"
"-------------"
"| 7 | 8 | 9 |"
"-------------"
'''
#VARIABLES

linear_line = "-------------"
row1 = "| 1 | 2 | 3 |"
row2 = "| 4 | 5 | 6 |"
row3 = "| 7 | 8 | 9 |"
p1 = ''
p2 = ''
r = 0


def game_display():
    #Just Prints The Game
    print(linear_line)
    print(row1)
    print(linear_line)
    print(row2)
    print(linear_line)
    print(row3)
    print(linear_line)

def position_choice():
    #Takes a number form user in (1-9)
    user_choice = 'Negetive!'
    acceptable_range = range(1, 10)
    within_range = False
    #Input validation
    while user_choice.isdigit() == False or within_range == False:

        user_choice = input("Enter a number between 1 to 9 as your position : ")

        # Wrong input messages
        if user_choice.isdigit() == False :
            print("Wrong! Please Enter a number")
        elif user_choice.isdigit() == True :
            if int(user_choice) in acceptable_range:
                within_range = True
            else:
                within_range = False
                print('Sorry the number is out of range(1-9) \n Please try again')

    return int(user_choice)



def player_mark():
    global r,p1,p2

    if r == 0 :
        player1_mark = 'A'
    
        while player1_mark not in ['X','O']:
            player1_mark = input("Player 1 choose your mark (X or O) : ")
            if player1_mark == 'x':
                player1_mark = 'X'
            elif player1_mark == 'o':
                player1_mark = 'O'

        player = player1_mark
        if player == 'X':
            p1 = 'X'
            p2 = 'O'
        else:
            p1 = 'O'
            p2 = 'X'
        
        
    elif r!= 0 and r%2 == 0 :
        player = p1
    elif r!= 0 and r%2 != 0 :
        player = p2
    r += 1
    return player



def mark_choice():

    xo = 'A'
    while xo not in ['X','O']:
        xo = input("Player 1 choose your mark (X or O) : ")
    return xo


def replacements(position,mark):
    global row1,row2,row3
       # Row 1
    if position == 1:
        row1 = row1[:2] + mark + row1[3:]
    elif position == 2:
        row1 = row1[:6] + mark + row1[7:]
    elif position == 3:
        row1 = row1[:10] + mark + row1[11:]
    
    # Row 2
    elif position == 4:
        row2 = row2[:2] + mark + row2[3:]
    elif position == 5:
        row2 = row2[:6] + mark + row2[7:]
    elif position == 6:
        row2 = row2[:10] + mark + row2[11:]
    
    # Row 3
    elif position == 7:
        row3 = row3[:2] + mark + row3[3:]
    elif position == 8:
        row3 = row3[:6] + mark + row3[7:]
    elif position == 9:
        row3 = row3[:10] + mark + row3[11:]


def win_check():
    # Check if X wins
    if row1[2] == row1[6] == row1[10] == 'X' or \
       row2[2] == row2[6] == row2[10] == 'X' or \
       row3[2] == row3[6] == row3[10] == 'X' or \
       row1[2] == row2[2] == row3[2] == 'X' or \
       row1[6] == row2[6] == row3[6] == 'X' or \
       row1[10] == row2[10] == row3[10] == 'X' or \
       row1[2] == row2[6] == row3[10] == 'X' or \
       row1[10] == row2[6] == row3[2] == 'X':
        print('X Wins!')
        return True

    # Check if O wins
    elif row1[2] == row1[6] == row1[10] == 'O' or \
         row2[2] == row2[6] == row2[10] == 'O' or \
         row3[2] == row3[6] == row3[10] == 'O' or \
         row1[2] == row2[2] == row3[2] == 'O' or \
         row1[6] == row2[6] == row3[6] == 'O' or \
         row1[10] == row2[10] == row3[10] == 'O' or \
         row1[2] == row2[6] == row3[10] == 'O' or \
         row1[10] == row2[6] == row3[2] == 'O':
        print('O Wins!')
        return True

    # If no winner, return False
    return False

def gameon_choice():
    game_r = 'B'

    while game_r not in ['Y', 'N','y','n']:
        game_r = input('Do you want to play again? (Y or N)')

    if game_r == 'Y' or game_r == 'y':
        return True
    elif game_r == 'N' or game_r == 'n':
        return False
    
    


def game_reset():
    global row1,row2,row3,p1,p2,r
    row1 = "| 1 | 2 | 3 |"
    row2 = "| 4 | 5 | 6 |"
    row3 = "| 7 | 8 | 9 |"
    p1 = 'X'
    p2 = 'O'
    r = 0



#Game Logic


game_on = True

while game_on :

    #Display the gameboard
    game_display()

    #whoose playing?
    mark = player_mark()

    #choose position
    position = position_choice()

    #replace the chosen position with players mark
    replacements(position,mark)

    # Check win status
    win_stat = win_check()

    # If there's a winner, ask to play again or stop
    if win_stat:
        game_display()
        game_reset()
        game_on = gameon_choice()
    else:
        # Continue playing if no winner yet
        game_on = True