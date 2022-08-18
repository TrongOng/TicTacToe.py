#Tic Tac Toe - Game : Trong Ong tictactoe.py
'''
Outline:
-*The first "While True:" loop is the landmark for restarting the game to the iteration; on firstt line so that the board reset's its values
-Create a Tic Tac Toe skeleton board using the dictionary that contains a key and a value
    -Each keys consist of numbers that correlates to it's Tic Tac Toe boxes
    -Then each value's are empty in order for the users to input the X or O input
-Then create a function; the outline's of the Tic Tac Toe in order to give it, it's board shape
    -The function will contain it's dictionary values + the ('-+-+-') + '|' design that gives the user an overlook of the board
-Create another function that gives it the rules or conditions of how to win the game
-The 3 functions + dictionary will be the primary skeleon of the game 
-Then create a display of how you want your game to look at the beginning 
-Prompt the users if he or she wants to begin the game 
    -if true, start the iterations 
    -else false, display GOODBYE
-If the user select "Yes", display the empty board and display Player 1 and Player 2 
-Then create a second "While Loop" that contains definite times the game will loop between each Player 1 + Player 2 moves which will be 4 times 
-Prompt Player 1 to place his or her "x" in the respectable number block
    -After Player 1 answeres, print the board containing the board values.
    -In each if elif statements, the method has another if statement that will execute if True which is the rules condition of the game
    -If rules of condition is True, break the second "while loop" and execute the next or last prompt
-Prompt Player 2 to place his or her "o" in the respectable number bock
    -After Player 2 answers, print the board containing the board values and contains prior answers
    -For the second "while loop" to count as 1, I did a additon assignment opertor i+=1 which means i+1=i
        -Starting the addition assignment opertor for Player 2 and not for Player 1 allows a full even rotation for the two players
    -In each if elif statements, the method has another if statement that will execute if True which is the rules condition of the game
    -If rules of condition is True, break the second "while loop" and execute the next or last prompt
-Once the second definite while loop ended
    -If the win(theBoard) condition is false, tell user it is a draw
    -if the condition is True, go to the next iteration which is...
    -Prompt the user to restart the game
    -If Yes, restart at the first while loop
    -elif No, say Goodbye and break
Logic:
-Create a while True: loop that iterates when the condition is True; on the first line so that ttthe board resetts if user wants to restart
-The dictionary will be named theBoard
    -There will be 9 keys; correlating to the traditional box
    -Each 9 keys, contains empty values
-Create function newBoard + theBoard = "newBoard(theBoard):"
    -newBoard contains the outlines of board ('-+-+-') and ('|')
    -theBoard contains the empty correlated values 
-Create a win function that has the theBoard attributes 
    -For each attritbutes or conditions returning true, print("You Win") 
        -Will be for "x" and "o" 
    -The "and" method allows all 3 conditions has to be true in order to execute
        -"if theBoard["7"] =="x" and theBoard["8"] == "x" and theBoard["9"] == "x":"
-Create the interface design that display the "welcome screen" 
    -print("===================================================")
    -print("Hello! Welcome To The Two Player Tic Tac Toe Game!")
    -print("===================================================")
-Create an integer input that has a variable "Start" to begin the game 
    -start = int(input("Would You Like To Begin?\n1.Yes\n2.No\nChoice: "))
-Letting the user know....
        print("Player 1 = x and Player 2 = o")
        print("Player 1 start first then Player 2")
-Create second While loop tha iterates a definite amount of times before the game will automatically end
    -i = 1
    -while i < 5: #Will execute max 4 times 
-Create an integer input that has a variable "pickX" to store in the value for player 1
    -pickX = int(input("Place Your X\n1.1\n2.2\n3.3\n4.4\n5.5\n6.6\n7.7\n8.8\n9.9\nChoice: "))
        -       if int(pickX) == 1:     #If pick 1 as True
                theBoard["1"] = "x"           #Store the key[1] as "x" if chosen
                print(newBoard(theBoard))       #display the new board with values
                if win(theBoard):             #This allows that if player 1 wins thru a condition of win(theBoard)
                    break                #the break method would break the while loop and go to the nextt iteration which is "restart"
-Create an integer input that has a variable "pickO" to store in the value for player 2
    -pickO = int(input("Place Your O\n1.1\n2.2\n3.3\n4.4\n5.5\n6.6\n7.7\n8.8\n9.9\nChoice: "))
        i += 1                           #Addition assignment operator to i for the definite amount to be counted
        theBoard["1"] = "o"              #storea the key[1] as o if chosen 
        print(newBoard(theBoard))        #Print the updated board
        if win(theBoard):               #if the condition (rules) of the game is true, start the next iteration
            break                         #break the definite loop and go to the next iteration
-Once the definite while loop ends...
            if win(theBoard) == False: #if condition is not true
            print("Draw - Cat") #display draw
-Prompt the user if he or she wants to play again, if yes, it will go back to the first while loop 
    -restart = int(input("Do you want to play again?\n1.Yes\n2.No\nChoice: "))
        if int(restart) == 2: #if no
            print("GOODBYE")
            break         #end the game /end the loop
'''
#Code
while  True:
    theBoard = {'7': ' ' , '8': ' ' , '9': ' ' ,
                '4': ' ' , '5': ' ' , '6': ' ' ,
                '1': ' ' , '2': ' ' , '3': ' ' }          
    def newBoard(theBoard):
        print(theBoard['7'] + '|' + theBoard['8'] + '|' + theBoard['9'])
        print('-+-+-')
        print(theBoard['4'] + '|' + theBoard['5'] + '|' + theBoard['6'])
        print('-+-+-')
        print(theBoard['1'] + '|' + theBoard['2'] + '|' + theBoard['3'])
    
    def win(theBoard):
        if theBoard["7"] =="x" and theBoard["8"] == "x" and theBoard["9"] == "x":
            print("X Win")
        elif theBoard["7"] =="x" and theBoard["4"] == "x" and theBoard["1"] == "x":
            print("X Win")
        elif theBoard["1"] =="x" and theBoard["2"] == "x" and theBoard["3"] == "x":
            print("X Win")
        elif theBoard["3"] =="x" and theBoard["6"] == "x" and theBoard["9"] == "x":
            print("X Win")
        elif theBoard["4"] =="x" and theBoard["5"] == "x" and theBoard["6"] == "x":
            print("X Win")
        elif theBoard["8"] =="x" and theBoard["5"] == "x" and theBoard["2"] == "x":
            print("X Win")
        elif theBoard["9"] =="x" and theBoard["5"] == "x" and theBoard["1"] == "x":
            print("X Win")
        elif theBoard["7"] =="x" and theBoard["5"] == "x" and theBoard["3"] == "x":
            print("X Win")
        if theBoard["7"] =="o" and theBoard["8"] == "o" and theBoard["9"] == "o":
            print("O Win")
        elif theBoard["7"] =="o" and theBoard["4"] == "o" and theBoard["1"] == "o":
            print("O Win")
        elif theBoard["1"] =="o" and theBoard["2"] == "o" and theBoard["3"] == "o":
            print("O Win")
        elif theBoard["3"] =="o" and theBoard["6"] == "o" and theBoard["9"] == "o":
            print("O Win")
        elif theBoard["4"] =="o" and theBoard["5"] == "o" and theBoard["6"] == "o":
            print("O Win")
        elif theBoard["8"] =="o" and theBoard["5"] == "o" and theBoard["2"] == "o":
            print("O Win")
        elif theBoard["9"] =="o" and theBoard["5"] == "o" and theBoard["1"] == "o":
            print("O Win")
        elif theBoard["7"] =="o" and theBoard["5"] == "o" and theBoard["3"] == "o":
            print("O Win")
        
    
    
    print("===================================================")
    print("Hello! Welcome To The Two Player Tic Tac Toe Game!")
    print("===================================================")
    start = int(input("Would You Like To Begin?\n1.Yes\n2.No\nChoice: "))
    if int(start) == 1:
        newBoard(theBoard)
        print("Player 1 = x and Player 2 = o")
        print("Player 1 start first then Player 2")
        i = 1
        while i < 5:  #Max 4 counts 
            pickX = int(input("Place Your X\n1.1\n2.2\n3.3\n4.4\n5.5\n6.6\n7.7\n8.8\n9.9\nChoice: "))
            if int(pickX) == 1:
                theBoard["1"] = "x"
                print(newBoard(theBoard))
                if win(theBoard):
                    break    #Bug, does not end the loop but due to the while loop condition, it will end the loop with the result of who wins
            elif int(pickX) == 2:
                theBoard["2"] = "x"
                print(newBoard(theBoard))
                if win(theBoard):
                    break    
            elif int(pickX) == 3:
                theBoard["3"] = "x"
                print(newBoard(theBoard))
                if win(theBoard):
                    break    
            elif int(pickX) == 4:
                theBoard["4"] = "x"
                print(newBoard(theBoard))
                if win(theBoard):
                    break 
            elif int(pickX) == 5:
                theBoard["5"] = "x"
                print(newBoard(theBoard))
                if win(theBoard):
                    break 
            elif int(pickX) == 6:
                theBoard["6"] = "x"
                print(newBoard(theBoard))
                if win(theBoard):
                    break 
            elif int(pickX) == 7:
                theBoard["7"] = "x"
                print(newBoard(theBoard))
                if win(theBoard):
                    break 
            elif int(pickX) == 8:
                theBoard["8"] = "x"
                print(newBoard(theBoard))
                if win(theBoard):
                    break 
            elif int(pickX) == 9:
                theBoard["9"] = "x"
                print(newBoard(theBoard))
                if win(theBoard):
                    break 
            pickO = int(input("Place Your O\n1.1\n2.2\n3.3\n4.4\n5.5\n6.6\n7.7\n8.8\n9.9\nChoice: "))
            if int(pickO) == 1:
                i += 1
                theBoard["1"] = "o"
                print(newBoard(theBoard))
                if win(theBoard):
                    break 
            elif int(pickO) == 2:
                i += 1
                theBoard["2"] = "o"
                print(newBoard(theBoard))
                if win(theBoard):
                    break 
            elif int(pickO) == 3:
                i += 1
                theBoard["3"] = "o"
                print(newBoard(theBoard))
                if win(theBoard):
                    break 
            elif int(pickO) == 4:
                i += 1
                theBoard["4"] = "o"
                print(newBoard(theBoard))
                if win(theBoard):
                    break 
            elif int(pickO) == 5:
                i += 1
                theBoard["5"] = "o"
                print(newBoard(theBoard))
                if win(theBoard):
                    break 
            elif int(pickO) == 6:
                i += 1
                theBoard["6"] = "o"
                print(newBoard(theBoard))
                if win(theBoard):
                    break 
            elif int(pickO) == 7:
                i += 1
                theBoard["7"] = "o"
                print(newBoard(theBoard))
                if win(theBoard):
                    break 
            elif int(pickO) == 8:
                i += 1
                theBoard["8"] = "o"
                print(newBoard(theBoard))
                if win(theBoard):
                    break 
            elif int(pickO) == 9:
                i += 1
                theBoard["9"] = "o"
                print(newBoard(theBoard))
                if win(theBoard):
                    break 
        if win(theBoard) == False:
            print("Draw - Cat")
        restart = int(input("Do you want to play again?\n1.Yes\n2.No\nChoice: "))
        if int(restart) == 2:
            print("GOODBYE")
            break
    elif int(start) == 2:
        print("GOODBYE")
        break
    
