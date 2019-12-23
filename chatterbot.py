import time  

name = input("Namaste , what is your name? ")  # asking for the introduction by the user

time.sleep(2)
print("Hello " + name)     # Greetings by the chatbot

feeling = input("How are you today? ")

time.sleep(2)   # numberof seconds to be elapsed by the bot
if ("good" in feeling) or ("fine" in feeling) or ("awesome" in feeling) or ("happy" in feeling) or ("cheerful" in feeling):
    print("I'm feeling the same")
else:
    print("I'm sorry to hear that!")

time.sleep(2)
intro = input("Do you want to start  with your IQ challenge ")  # 
if "n" in intro.lower():
  print("Okay bro !")
  bye = input("bye then")
elif ("y" in intro.lower()) or ("sure" in intro.lower()) or ("carry on" in intro.lower()):
  score = 0
  print("Let`s start with your first question ")
  
  ques1 = input("Does any two of the following numbers add up to seventeen - (6 , 13 , 2 , 12 , 7 , 14) ?")  # first question
  if ("n" in ques1.lower() or "f" in  ques1.lower() ):
    score = score + 5
  else:
    pass
  
  print("Let`s move to second question")
  ques2 = input("Does \"racecar\" spell same backwards ?")                     # second question
  if ("y" in ques2.lower() or "t" in ques2.lower()):
    score = score + 5
  else:
    pass
  
  print("Let`s move to third question")
  
  ques3 = input("If u rearrange the word \"EOSSH \" , then you will get the name if a/an - ")   # Third question
  if (ques3.lower()=="shoes"):
    score = score + 5
  else:
    pass
  
  ques4 = input("Ralph travels four blocks north and then three blocks east .How many blocks is Ralph from his starting place?")  # fourth question
  if (ques4 == "5" or ques4.lower()=="five"):
    score = score + 5
  else:
    pass
  
  print("Now give us some time to calculate your final score ")     
  time.sleep(3)
  print("your score is: ",score)                  # claculation the final score
  time.sleep(1)
  if (score<=5):
    print("You need to work a little bit buddy")
  elif (5<score<=15):
    print("You got an average score")
  elif (score==20):
    print("You are the winner of this challenge . Congratulations")
else:
  print("Okay then")
  bye = input("bye then")                                      # goodbye msg from bot . 

