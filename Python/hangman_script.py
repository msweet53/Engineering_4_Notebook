# hangman script
#by Max Sweet
# 9.23.21
import time

amount_wrong = 0
game_lost = False 
play_again = True
word_chosen = ""
missed_letters = []
letter_guessed = ""
letters_correct = []
game_won = False


while play_again == True:
    if word_chosen == "": #of there has been no input for the word, then ask for one and set it
        word_chosen = input("Player 1, please input your word")
        amount_of_letters = len(word_chosen)*("-") #string for what to print
        print("\n" * 50) #clear
    if amount_wrong >= 0: #below is construction for the hangman, the end = "" code is to make sure it doesnt drop a line when needed. it is fairly self explanitory.
        print("---┐")
    if amount_wrong >= 1:
        print("   0")
    else:
        print()
    if amount_wrong >= 2:
        print("  /", end = "")
    else:
        print(end = "")
    if amount_wrong >= 3:
        print("|", end = "")
    else:
        print(end ="")
    if amount_wrong >= 4:
        print("\\")
    else:
        print()
    if amount_wrong >= 5:
        print("  /", end =" ")
    else:
        print(end = " ")
    if amount_wrong >= 6:
        print("\\")
        game_lost = True
    else:
        print()


    print("Missed Letters:", missed_letters) #prints some things like what letters have been missed and the print variable for the dash word display
    print(amount_of_letters)    
    print()
    letter_guessed = input("Guess your letter:") #asks for a letter guessed input
    for place in range(len(word_chosen)): # looking at the range of the length of the word
        if word_chosen[place] == letter_guessed: #if the letter is present at a certain place
            amount_of_letters = amount_of_letters[:place] + letter_guessed + amount_of_letters[place+1:] #set the print variable to what it should be
    
    if "-" not in amount_of_letters: #if there are no empty spaces left the player wins
        game_won = True
    
    if game_lost == True: #if the game is lost, ask if they want to play again. if not, break the loop. if so, reset variables and play again
        if input("Game over, you lost :(. Play again? Respond x for no.") == "x":
            play_again = False
        else:
            amount_wrong = 0
            missed_letters = []
            amount_of_letters = ""
            letter_guessed = ""
            word_chosen = ""
            game_lost = False
    
    if game_won == True: #if the game is lost, ask if they want to play again. if not, break the loop. if so, reset variables and play again
        if input("Game over, you won! :). Play again? Respond x for no.") == "x":
            play_again  = False
        else:
            amount_wrong = 0
            missed_letters = []
            amount_of_letters = ""
            letter_guessed = ""
            word_chosen = ""
            game_won = False
    
    if letter_guessed not in word_chosen:
        amount_wrong += 1
        missed_letters.append(letter_guessed)

    print("\n" * 50)
