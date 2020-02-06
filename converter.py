#!/usr/bin/env python
# coding: utf-8

# In[2]:


import time
def kg(value,convert2):
    if convert2=="g" :
        a=value*1000000
        print(a)
        
    elif convert2=="mg":
        a=value*1000000
        print(a)
        
    elif convert2=="tonne":
        b=value*0.001
        print(b)
        
    elif convert2=="stone":
        a=value*0.157
        print(a)
        
    elif convert2=="pound":
        a=value*2.204
        print(a)
        
    elif convert2=="ounce":
        a=value*35.274
        print(a)
    else:
        print("A problem is being faced")

def g(value,convert2):
    if convert2=="kg" or "kilogram":
        b=value/1000
        print(b)
    elif convert2=="mg" or "milli gram" or "milligram":
        b=value*1000
        print(b)
    elif convert2=="tonne":
        b=value/(1e+6)
        print(b)
    elif convert2=="stone":
        b=value/0.000157
        print(b)
    elif convert2=="pound":
        b=value/0.002204
        print(b)
    elif convert2=="ounce":
        b=value/0.035274
        print(b)
    else:
        print("A problem is being faced")
        
def mg(value,convert2):
    if convert2=="kg" or "kilogram":
        b=value/1000000
        print(b)
    elif convert2=="g" or "gram":
        b=value/1000
        print(b)
    elif convert2=="tonne":
        b=value*1e-9
        print(b)
    elif convert2=="stone":
        b=value*1.57e-7
        print(b)
    elif convert2=="pound":
        b=value*2.20e-6
        print(b)
    elif convert2=="ounce":
        b=value*3.5e-5
        print(b)
    else:
        print("A problem is being faced")
        
def tonne(value,convert2):
    if convert2=="kg" or "kilogram":
        b=value*1000
        print(b)
    elif convert2=="mg" or "milli gram" or "milligram":
        b=value*1e+9
        print(b)
    elif convert2=="stone":
        b=value*1e+6
        print(b)
    elif convert2=="gram" or "g":
        b=value*1e+6
        print(b)
    elif convert2=="pound":
        b=value*2204.62
        print(b)
    elif convert2=="ounce":
        b=value*35274
        print(b)
    else:
        print("A problem is being faced")
        
def stone(value,convert2):
    if convert2=="kg" or "kilogram":
        b=value*6.35
        print(b)
    elif convert2=="mg" or "milli gram" or "milligram":
        b=value*6.35e+6
        print(b)
    elif convert2=="tonne":
        b=value*0.00635
        print(b)
    elif convert2=="gram":
        b=value*6350.29
        print(b)
    elif convert2=="pound":
        b=value*14
        print(b)
    elif convert2=="ounce":
        b=value*224
        print(b)
    else:
        print("A problem is being faced")
        
def pound(value,convert2):
    if convert2=="kg" or "kilogram":
        b=value*0.45
        print(b)
    elif convert2=="mg" or "milli gram" or "milligram":
        b=value*453592
        print(b)
    elif convert2=="tonne":
        b=value*0.000453
        print(b)
    elif convert2=="stone":
        b=value*0.071
        print(b)
    elif convert2=="gram":
        b=value*453.5
        print(b)
    elif convert2=="ounce":
        b=value/0.035274
        print(b)
    else:
        print("A problem is being faced")
        
        
def main():
    time.sleep(0.1)
    print("welcome to the weight converter")
    time.sleep(0.1)
    print("we can convert : kg , g , mg , pound , stone , ounce")
    convert1=input("from ? ")
    convert2=input("to? ")
    value=int(input("value? "))
    if convert1=="kg":
        kg(value,convert2)
    elif convert1=="g":
        g(value,convert2)
    elif convert1=="mg":
        mg(value,convert2)
    elif convert1=="tonne":
        tonne(value,convert2)
    elif convert1=="stone":
        stone(value,convert2)
    elif convert1=="pound":
        pound(value,convert2)
    ans=input("want to try again? ")

    if ans=="yes":
        main()
    
main()


# In[ ]:


def kg(value,convert2):
    if convert2=="g" or "gram":
        a=value*1000000
        print(a)
        
    elif convert2=="mg" or "milligram":
        a=value*1000000
        print(a)
        
    elif convert2=="tonne":
        a=value*0.001
        print(a)
        
    elif convert2=="stone":
        a=value*0.157
        print(a)
        
    elif convert2=="pound":
        a=value*2.204
        print(a)
        
    elif convert2=="ounce":
        a=value*35.274
        print(a)
    else:
        print("A problem is being faced")

def g(value,convert2):
    if convert2=="kg":
        b=value/1000
        print(b)
    elif convert2=="mg" or "milli gram" or "milligram":
        b=value*1000
        print(b)
    elif convert2=="tonne":
        b=value/(1e+6)
        print(b)
    elif convert2=="stone":
        b=value/0.000157
        print(b)
    elif convert2=="pound":
        b=value/0.002204
        print(b)
    elif convert2=="ounce":
        b=value/0.035274
        print(b)
    else:
        print("A problem is being faced")
        
def mg(value,convert2):
    if convert2=="kg":
        b=value/1000000
        print(b)
    elif convert2=="g" or "gram":
        b=value/1000
        print(b)
    elif convert2=="tonne":
        b=value*1e-9
        print(b)
    elif convert2=="stone":
        b=value*1.57e-7
        print(b)
    elif convert2=="pound":
        b=value*2.20e-6
        print(b)
    elif convert2=="ounce":
        b=value*3.5e-5
        print(b)
    else:
        print("error")
        
def main():
   # time.sleep(0.1)
    print("welcome to the weight converter")
  #  time.sleep(0.1)
    print("we can convert : kg , g , mg , pound , stone , ounce")
    convert1=input("from ? ")
    convert2=input("to? ")
    value=int(input("value? "))
    if convert1=="kg" or "kilogram":
        kg(value,convert2)
    elif convert1=="g" or "gram" :
        g(value,convert2)
    elif convert1=="mg" or "milligram" :
        mg(value,convert2)
    elif convert1=="tonne":
        tonne(value,convert2)
    elif convert1=="stone":
        stone(value,convert2)
    elif convert1=="pound":
        pound(value,convert2)
main()
ans=input("want to try again? ")
if ans=="yes":
    main()


# In[ ]:




