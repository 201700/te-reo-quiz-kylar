score = 0

#asking what your names is, greeting you with your name,  and explaing that this is a te reo quiz and explaing what you'll do while doing it.
name=input("what is your name?")
print("hello", name)
print("this is a te reo quiz, doing this quiz you will know or learn te reo phases")

#this is question one, in questions one it ask you a question if Mōrena the means good morning in english. this can be correct or False. if you enter true or false, then it will tell you if you are correct or incorrect. then it will move you to question 2.
def question1():
 global score
 print("this is question one")
 choice = input("Mōrena means good morning in te reo / true or false? ")
 choice = choice.lower()
 
 if choice == "true":
  print("correct")
  question2()
  score =+ 1
 elif choice == "false":
   print("incorrect")
   question2()
   score =- 1

#this is question two, in questions two it ask you a question if purū  the means green in english. this can be correct or False. if you enter true or false,then it will tell you if you are correct or incorrect. then it will move you to question 3.
def question2():
  global score
  print("this is question two")
  space = input("purū means green in te reo / true or false? ")
  space = space.lower()
  
  if space == "true":
   print("incorrect")
   question3()
   score =- 1
  elif space == "false":
    print("correct")
    question3()
    score =+ 1
#this is question three, in questions three it ask you a question if Kei te nga mihi  the means  how are you in english. this can be correct or False. if you enter true or false,then it will tell you if you are correct or incorrect. then it will move you to question 4.
def question3():
  global score
  print("this is question three")
  color = input("Kei te nga mihi means how are you in te reo / true or false? ")
  color = color.lower()
  
  if color == "true":
   print("incorrect")
   question4()
   score =- 1
  elif color == "false":
    print("correct")
    question4()
    score =+ 1
#this is question two, in questions four it ask you a question if akomanga the means classroom in english. this can be correct or False. if you enter true or false,then it will tell you if you are correct or incorrect. then it will move you to question 5.
def question4():
  global score
  print("this is question four")
  size = input("akomanga means classroom in te reo / true or false? ")
  size == size.lower()
  if size == "true":
   print("correct")
   question5()
   score =+ 1
  elif size == "false":
   print("incorrect")
   question5()
   score =- 1
#this is question five, in questions five it ask you a question if rorohiko the means computer in english. this can be correct or False. if you enter true or false,then it will tell you if you are correct or incorrect. then it will end.
def question5():
  global score
  print("this is question five")
  line = input("rorohiko means computer in te reo / true or false? ")
  line == line.lower()
  
  if line == "true":
    print("correct")
    score =+ 1
  elif line == "false":
    print("incorrect")
    score =- 1

question1()
print(score)

question2()
print(score)

question3()
print(score)

question4()
print(score)

question5()
print(score)