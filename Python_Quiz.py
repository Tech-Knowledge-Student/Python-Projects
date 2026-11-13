qna = {
  "Which is the smallest state in India by area ?" : {
    'A' : 'Sikkim',
    'B' : 'Goa',
    'C' : 'Tripura',
    'D' : 'Manipur',
    'Ans' : 'B',
    'Price' : 10000
  },
  "Which is the capital of Australia ?" : {
    'A' : 'Sydney',
    'B' : 'Melbourne',
    'C' : 'Canberra',
    'D' : 'Perth',
    'Ans' : 'C',
    'Price' : 20000
  },
  "Which is the largest ocean in the Earth ?" : {
    'A' : 'Atlantic',
    'B' : 'Arctic',
    'C' : 'Pacific',
    'D' : 'Indian',
    'Ans' : 'C',
    'Price' : 30000
  },
  "When international yoga day is celebrated ? " : {
    'A' : '21 June',
    'B' : '5 June',
    'C' : '22 November',
    'D' : '13 December',
    'Ans' : 'A',
    'Price' : 40000
  },
  "Who is the national animal of India ? " : {
    'A' : 'Lion',
    'B' : 'Bengal Tiger',
    'C' : 'Elephant',
    'D' : 'Black Panther',
    'Ans' : 'B',
    'Price' : 50000
  }
}

score = 0
amount = 0

for each in qna :
  print(each)
  for key in 'ABCD' :
    print(key,":", qna[each][key])

  ans = input("Enter option of answer or quit : ").lower()

  while not(ans in ['a','b','c','d','quit']) :
    ans = input("Enter valid option (A/B/C/D) : ").lower()

  if ans == "quit" :
    break

  corr_ans = qna[each][qna[each]['Ans']]
    
  if ans == qna[each]['Ans'].lower() :
    print("Correct Answer 🎉🎉")
    score += 1
    amount += qna[each]['Price']
    print(f'Current Score : {score}')
    print(f"You Won ₹{qna[each]['Price']}")
  else :
    print("Wrong Answer 😔😔")
    print("Correct ans : ", qna[each]['Ans'],".",corr_ans)
    print(f'Current Score : {score}')


print(f"You answered {score} questions out of 5..")
print("You earned : Rs.", amount)

if amount == 0 :
  print("Don't Worry")
  print("Better luck next time 😊😊👍👍")
else :
  print("Well Played 👏👏")
  
print("----Game Over---")
