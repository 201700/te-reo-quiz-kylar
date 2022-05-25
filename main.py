name=input 
print()

def question1():
  print("this is question one")
  choice = input("Mōrena means good morning in te reo / true or false? ")
  choice = choice.lower()
  
  if choice == "true":
    print("correct")
    question2()
  elif choice == "false":
    print("incorrect")
    question2()
  
def question2():
  print("this is question two")
  space = input("kākāriki means green in te reo / true or false? ")
  space = space.lower()
  if space == "true":
   print("correct")
   question3()
  elif space == "false":
    print("incorrect")
    question3()

def question3():
  print("this is question three")
  color = input("Kei te pēhea koe means how are you in te reo / true or false? ")
  color = color.lower()
  
  if color == "true":
   print("correct")
   question4()
  elif color == "false":
    print("incorrect")
    question4()

def question4():
  print("this is question four")
  size = input("akomanga means classroom in te reo / true or false? ")
  size == size.lower()
  if size == "true":
   print("correct")
   question5()
  elif size == "false":
   print("incorrect")
   question5()

def question5():
  print("this is question five")
  line = input("rorohiko means computer in te reo / true or false? ")
  line == line.lower()
  
  if line == "true":
    print("correct")
  elif line == "false":
    print("incorrect")


question1()