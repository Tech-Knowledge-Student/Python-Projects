import random

user_score = 0
comp_score = 0

while True :
  userChoice = input("Enter choice or Quit : ").lower()
  
  if userChoice == "quit" :
    break

  if not(userChoice in ["rock", "paper", "scissor"]):
    print("Enter valid choice (Rock/Paper/Scissor)")
    continue
    
  compChoice = random.choice(["Rock", "Paper", "Scissor"]).lower()
  print("Computer's Choice :", compChoice)


  if(userChoice == "rock") :
    if compChoice == "rock" :
      print("Draw !! Try again 😅😅")
    elif compChoice == "scissor" :
      print("You Won 🎉🎉")
      user_score += 1
    else :
      print("Computer Won 😔😔")
      comp_score += 1

  elif userChoice == "paper" :
    if compChoice == "paper" :
      print("Draw !! Try again 😅😅")
    elif compChoice == "rock" :
      print("You Won 🎉🎉")
      user_score += 1
    else :
      print("Computer Won 😔😔")
      comp_score += 1

  else : 
    if compChoice == "paper" :
      print("You Won 🎉🎉")
      user_score += 1
    elif compChoice == "rock" :
      print("Computer Won 😔😔")
      comp_score += 1
    else :
      print("Draw !! Try again 😅😅")    

print("Your score :", user_score)
print("Computer's score :", comp_score)

if (user_score == comp_score) :
  print("Draw !!")
  print("Winner 🏆 🏆 : Both 😅😅")
else : 
  Winner = ("Computer", "You")[user_score>comp_score]

  print("Winner 🏆 🏆 : ", Winner)
print("----Game Over----")
