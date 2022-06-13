score = 0
#asking what your names is, greeting you with your name,  and explaing that this is a te reo quiz and explaing what you'll do while doing it.
import time
name =input("what is your name?")
time.sleep(1.5)
print("hello", name)
time.sleep(1)
print("this is a te reo quiz, doing this quiz you will know or learn te reo phases")
time.sleep(2)

def question1():
#this is question one, in questions one it ask you a question if Mōrena the means good morning in english. this can be correct or False. if you enter true or false, then it will tell you if you are correct or incorrect. then it will move you to question 2.
  global score
  print("this is question one")
  choice_1 = input("Mōrena means good morning in te reo / true or false? ")
  choice_1 = choice_1.lower()

  if choice_1 == "true":
   print("correct")
   score += 1
  elif choice_1 == "false":
   print("incorrect")
   score -= 1
def question2():
#this is question two, in questions two it ask you a question if purū  the means green in english. this can be correct or False. if you enter true or false,then it will tell you if you are correct or incorrect. then it will move you to question 3.
  global score
  print("this is question two")
  space = input("purū means green in te reo / true or false? ")
  space = space.lower()
  
  if space == "true":
    print("incorrect")
    score -= 1
  elif space == "false":
    print("correct")
    score += 1
def question3():
#this is question three, in questions three it ask you a question if Kei te nga mihi  the means  how are you in english. this can be correct or False. if you enter true or false,then it will tell you if you are correct or incorrect. then it will move you to question 4.
  global score
  print("this is question three")
  color = input("Kei te nga mihi means how are you in te reo / true or false? ")
  color = color.lower()
  
  if color == "true":
     print("incorrect")
     score -= 1
  elif color == "false":
    print("correct")
    score += 1
def question4():
#this is question four, in questions four it ask you a question if akomanga the means classroom in english. this can be correct or False. if you enter true or false,then it will tell you if you are correct or incorrect. then it will move you to question 5.
  global score
  print("this is question four")
  size = input("akomanga means classroom in te reo / true or false? ")
  size = size.lower()
  
  if size == "true":
     print("correct")
     score += 1
  elif size == "false":
    print("incorrect")
    score -= 1
def question5():
#this is question five, in questions five it ask you a question if rorohiko the means computer in english. this can be correct or False. if you enter true or false,then it will tell you if you are correct or incorrect. then it will end.
  global score
  print("this is question five")
  line = input("rorohiko means computer in te reo / true or false? ")
  line = line.lower()
  
  if line == "true":
     print("correct")
     score += 1
  elif line == "false":
    print("incorrect")
    score -= 1




question1()

question2()

question3()

question4()

question5()
(score)
print(score)