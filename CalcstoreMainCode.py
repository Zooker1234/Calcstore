import math
from tkinter import simpledialog, messagebox

#returns if string full of only ints
def checkStrForNonInt(s):
    for i in range(0, len(s)):
        if s[i] == "1" or s[i] == "2" or s[i] == "3" or s[i] == "4" or s[i] == "5" or s[i] == "6" or s[i] == "7" or s[i] == "8" or s[i] == "9" or s[i] == "0":
            pass
        else:
            return False
    return True
def checkStrForSigns(s):
    for i in range(0, len(s)):
        if s[i] == "+" or s[i] == '-' or s[i] == '/' or s[i] == '*' or s[i] == '%' or s[i] == '~sqrt~':
            pass
        else:
            return False
    return True
#returns if equation is valid
def checkEquation(e):
    i = 0
    while i < len(e):
        if checkStrForNonInt(e[i]) or checkStrForSigns(e[i]):
            i += 1
        elif e[i] == '~':
            if checkForValidGraveSign(e, i) == 0:
                return False
            else:
                i += 2 + checkForValidGraveSign(e, i)
        else:
            return False
    return True
#if there's a grave, checks for if its a valid sign. n is place of grave in str e
#0 == invalid, any other value == valid
def checkForValidGraveSign(e, n):
    newN = n + 1
    lenOfSign = 0
    while True:
        if e[newN+1] == '~':
            word = e[n:newN+1]
            if word == '~sqrt~':
                return lenOfSign
            else:
                return 0
        elif newN+1 == len(e):
            return 0
        else:
            lenOfSign += 1
            newN += 1
        
            
#saves an equation to the list
def saveEquation(e):
    with open('Equations.txt', 'a') as file:
                file.write(e + '\n')
def getEquation():
    pass
def SolveEquation():
    pass


while True:
    cancel = False
    
    
    whatToDo = simpledialog.askstring("choose", "what do you want to do?\
    \nTo look at an equation, type \"look.\"\nTo add a new equation, type \
    \"add.\"\nTo edit an equation, type \"edit.\"\nTo solve an equation, \
    type \"solve.\"").lower()
    while cancel == False:
        goodEquation = False
        if whatToDo == "add" or whatToDo == "\"add\"":
            equation = simpledialog.askstring("equation", "please type the equation \
you want to add.\nIf you changed your mind, type \"cancel\".").lower()
            while goodEquation == False:
                if checkEquation(equation) == True:
                    saveEquation(equation)
                    goodEquation = True
                elif equation == "cancel" or equation == "\"cancel\"":
                    cancel = True
                else:
                    equation = simpledialog.askstring("equation","That is not a valid equation!\nplease type the equation you want to add.\n If you changed your mind, type \"cancel\".").lower()
                    
                
