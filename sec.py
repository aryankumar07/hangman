import random
from words import word_list
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
lives=int(6)
comp=random.choice(word_list)
print(comp)
list2=[]
for i in range(len(comp)):
    list2.append('_')
print(list2)
store=False
while lives>=0:
    guess=input("enter the word : ")
    for h in range(len(list2)):
      if(list2[i]==guess):
        store=True


    if(not store):
      b=0
      for i in range(len(comp)):
          if(guess==comp[i]):
              b=1
              list2[i]=guess
    
      if(b==0):
          print(stages[lives])
          lives = lives-1
      
      a=''.join(map(str,list2))
      print(a)
      if(a==comp):
          print("you win")
          break
      if(lives<0):
          print("you lost")
          break
    else:
      print("already used")
