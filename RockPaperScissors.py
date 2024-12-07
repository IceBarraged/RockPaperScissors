import random

#Added to take a wider variety of inputs, the game will proceed provided the users input starts with 'R', 'P' or 'S'
def LEFT(s, length):
    # example: LEFT("apple",3) returns "app".
    return str(s[:length])

#Choices stay consistent, other variables are initialized so their loops work.
Choices = ["R","P","S"]
Replay = None
Replaychoice = "init"

try:
    while Replay != False:
        P1Choice = input("Let's play Rock, Paper, Scissors! Go ahead and choose!\n")

        #Reinitialized so the game is replayable, or you don't get caught in infinite loops etc.
        Funny = P1Choice
        P1Choice = LEFT(P1Choice,1)
        P1Choice = P1Choice.upper()
        Replaychoice = "init"
        CPUChoice = random.choice(Choices)

        input("Rock...(Press 'ENTER' to continue...)")
        input("Paper...(Press 'ENTER' to continue...)")
        input("Scissors!!!(Press 'ENTER' to continue...)")
        if P1Choice != "R" and P1Choice != "P" and P1Choice != "S":
            print("What do you mean you picked ",Funny,"??")
        else:
            if P1Choice == CPUChoice:
                print("We both picked ",CPUChoice,". It's a draw!")
            elif (P1Choice == "R" and CPUChoice != "P") or (P1Choice == "P" and CPUChoice != "S") or (P1Choice == "S" and CPUChoice != "R"):
                print("I picked ",CPUChoice," and you picked ",P1Choice,". You win!!!")
            else:
                print("I picked ",CPUChoice," and you picked ",P1Choice,". I win!!!")
        while Replaychoice.upper() != "Y" and Replaychoice.upper() != "N":
            Replaychoice = input("Play again? Y/N\n")
            if Replaychoice.upper() == "Y":
                Replay = True
            elif Replaychoice.upper() == "N":
                Replay = False
                print("Thanks for playing! Bye!")
            else:
                print("Sorry I didn't understand your request")
except:
    print("Sorry, I didn't understand your input! :(")