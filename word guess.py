#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random
from random import choices
def game ():

    fwords=open(r"C:\Users\SHARMA'S\Desktop\vasvi\python\words.txt","r")
    fhints=open(r"C:\Users\SHARMA'S\Desktop\vasvi\python\hints.txt","r")
    score=0;
    lines=fhints.readlines()
    i=random.randint(0,10)
    line2=lines[i]
    print (line2)
    lines_1=fwords.readlines()
    line1=lines_1[i]
    #print(line1)
    j=0
    end=len(line1)-1
    answer=str(input("Give a try: "))
  
    while answer != line1.strip() :
        print("Incorrect")
        hint=str(input("do you need a hint?(write yes or no)"))
        if hint=="yes":
            if j < end:
                print(line1[j])
                j+=1
                score-=2;
            elif j>end:
                break;
                score-=2;
            answer=str(input("try again"))
        else :
            answer=str(input("try again"))
            
    if answer==line1.strip():
        print("you are right! congratulations")
        score+=10   

    print("your score: ", score, "\n ||game finish||")  
    print("the answer is : " ,line1)
    reply=str(input("want to play again? (write yes or no)"))
    if reply=="yes":
        game()
game() 

