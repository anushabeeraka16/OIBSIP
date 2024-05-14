import random
import string
def generate_password(length,numbers=True,special_characters=True):
   leng=string.ascii_letters
   num=string.digits
   sc=string.punctuation
   print(leng,num,sc,"\n")
   char=leng
   if numbers:
      char+=num
   if special_characters:
      char+=sc
   pwd=""
   yes=False
   has_num=False
   has_sc=False
   
   while not yes or len(pwd)<length:
      new=random.choice(char)
      pwd+=new
      
      if new in num:
         has_num=True
      if new in sc:
         has_sc=True
         
      yes =True
      if numbers:
         yes=has_num
      if special_characters:
         yes=yes and has_sc
   return pwd
length=int(input("enter min length"))
has_num=input("number 1/0:").lower()=="1"
has_sc=input("special character 1/0:").lower()=="1"
pwd=generate_password(length,has_num,has_sc)
print("password=",pwd)
   