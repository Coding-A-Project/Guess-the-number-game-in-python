import random
print ("Level 1 / 4")
i = (random.randint(1, 10))
g = eval(input("Enter Your Guess (1 to 10): "))
if (i == g): 
   import random
   print ("Level 2 / 4")
   i = (random.randint(1, 100))
   g = eval(input("Enter Your Guess (1 to 100): "))
   if (i == g): 
      import random
      print ("Level 3 / 4")
      i = (random.randint(1, 1000))
      g = eval(input("Enter Your Guess (1 to 1000): "))
      if (i == g): 
        import random
        print ("Level 3 / 4")
        i = (random.randint(1, 10000))
        g = eval(input("Enter Your Guess (1 to 10000): "))
        if (i == g):
            print('You have completed this game sucessfully. You must be the luckiest person in the world')
        else:
          print ('You Falied :-( ', "It was", i)        
      else:
        print ('You Falied :-( ', "It was", i) 
   else:
    print ('You Falied :-( ', "It was", i)   
else:
    print ('You Falied :-( ', "It was", i)    