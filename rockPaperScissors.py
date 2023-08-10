import random

list=["Rock","Paper","Scissor"]

noOfTimesUserWon = 0
noOfTimesComputerWon=0

while(True):
    userInput=input("Select amongst r for Rock,p forPaper,s for scissor and q to quit  ")
 
    computerInput=random.choice(list)

    if(userInput=="q"):
        break
    
    elif(userInput=="r" and computerInput=="Paper" ):
        print("Computer's Input=",computerInput)
        print("Computer won")
        noOfTimesComputerWon=noOfTimesComputerWon+1
    elif(userInput=="p" and computerInput=="Scissor"):
        print("Computer's Input=",computerInput)
        print("Computer won")
        noOfTimesComputerWon=noOfTimesComputerWon+1
    elif(userInput=="s" and computerInput=="Rock"):
        print("Computer's Input=",computerInput)
        print("Computer won")
        noOfTimesComputerWon=noOfTimesComputerWon+1
    elif(userInput==computerInput):
        print("Computer's Input=",computerInput)
        print("No one won")
        
    else:
        print("Computer's Input=",computerInput)
        print("User won")
        noOfTimesUserWon = noOfTimesUserWon+1


print("No. of times user won =",noOfTimesUserWon)
print("No.of times computer won =",noOfTimesComputerWon)