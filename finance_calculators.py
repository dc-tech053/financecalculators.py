# Import math before making the menu.

import math


print("                              MENU                           ")

print("")
print("investment - to calculate the amount of interest you will earn on your investment")
print("")
print("bond       - to calculate the amount you'll have to pay on a home loan")
print("")

# Use the 'menu' variable to enable the creation of if statements.
menu = input("Please enter either 'investment' or 'bond' from the menu above to proceed: ")

while menu != "investment" and menu != "bond":
        input("Please enter either 'investment' or 'bond' from the menu above to proceed: ")

# Create if statements to seperate the 2 choices; 'investment and 'bond', for the different lists of questions.
if menu == "investment":
        p = int(input("Please enter the amount of money you are depositing: "))
        r = int(input("Please enter the interest rate e.g. 8 if 8%: "))
        t = int(input("Please enter the number of years you are planning on investing:  "))

        interest = input("Please enter 'simple' or 'compound' interest:  ")

# Use the three formulae in the print statement.
        if interest == "simple":
            print("The amount you will get back on your investment after the given period is below: ")
            print (int(p *(1 + (r*0.01)*t)))
        if interest == "compound":
            print("The amount you will get back on your investment after the given period is below: ")
            print (int(p * math.pow((1 + (r/100)),t)))
# Cast/convert the formulae and 6 of the 7 user inputs, to integers. The interest variable input (line ) remains a string because it is not part of the calculation.
if menu == "bond":
        p = int(input("Please enter the present value of the house: "))
        i = int(input("Please enter the interest rate e.g. 7 if 7%: "))
        n = int(input("Please enter the number of months you plan to take to repay the bond e.g. 240 months: "))
        print("Your monthly repayment is printed below : ")
        print (int((i/100) * p)/(1 - (1 + (i/100))*(-n)))


        
