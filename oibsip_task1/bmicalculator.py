name=input("enter your name:")
w=int(input("enter your weight in kgs:"))
h=int(input("enter your height in cms:"))
h_in_mt=h/100
BMI=(w)/(h_in_mt**2)
print(BMI)
if BMI>0:
    if(BMI<18.5):
        print(name +",you are underweight.")
    elif(BMI<=24.9):
        print(name +",your weight is normal.")
    elif(BMI<29.9):
        print(name +",you are overweight.")
    elif(BMI<34.9):
        print(name +",you are obese.")
    elif(BMI<39.9):
        print(name +",you are severly obese.")
    else:
        print(name +",you are morbidly obese.")
else:
        print("ivalid input")        