from email.base64mime import body_encode
import math

'''This program will calculate two different financial calculations
Investmet or Home loan, depending on the input given by the user'''

# choose investment or bond 
start_program=input("Are you interested in Investment or Bond?").lower()
if start_program == "investment":
    p = input("Insert initial amount investment: ") #initial amount invested
    r_percentage = input("Insert the annual interest rate as a percentage: ") #annual interest rate
    r_float = float(r_percentage.strip('%'))/100 #interest rate 
    t = input("Insert the Number of Years the money is invested for: ") #number of years that the money is invested for  
    interest = input("Write down if you want a Simple or Compound variable: ").lower()

    if interest == "compound":
        a = (float(p)*(1+r_float))*float(t) # a is the total ammount inclusive of interest 
        print("Your total compound ammount is" + " " + str(a)) # 
    elif interest == "simple":
        a = (float(p)*(1+r_float*float(t))) # a is the total ammount inclusive of interest 
        print("the total ammount is"+ " " + str(a))
    
elif start_program == "bond":
    p = float(input("Type present value house: ")) # current value of the house as a float
    i_percentage = input("Type the interest rate: ") #interest rate
    i_float=float(i_percentage.strip("%"))/100
    interest_rate=(i_float/12)

    n = float(input("Number of months: "))
    repayment= (interest_rate*p)/(1-(1+interest_rate)**-n)
    
    print("the total number of repayment", repayment)
else:
    print("this input is invalid")

