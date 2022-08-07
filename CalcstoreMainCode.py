import math
from tkinter import simpledialog, messagebox

#returns if string full of only ints
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
        if e[i].isdigit() or checkStrForSigns(e[i]):
            i += 1
        elif e[i] == '~':
            if checkForValidTildeSign(e, i) == 0:
                return False
            else:
                i += 2 + checkForValidTildeSign(e, i)
        else:
            return False
    return True
#if there's a tilde, checks for if its a valid sign. n is place of tilde in str e
#0 == invalid, any other value == valid
def checkForValidTildeSign(e, n):
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
    with open('equations.txt', 'a') as file:
                file.write(e + '\n')
def getEquation():
    pass
def SolveEquation():
    pass


while True:
    cancel = False
    
    while cancel == False:
        whatToDo = simpledialog.askstring("CalcStore", """What do you want to do?
    To look at an equation, type "look."
    To add a new equation, type "add."
    To edit an equation, type "edit."
    To solve an equation, type "solve."
    """).lower()
    """)
        
        goodEquation = False
        if whatToDo == "add" or whatToDo == "\"add\"":
            equation = simpledialog.askstring("Add Equation", """Please type the equation you want to add.
If you changed your mind, type "cancel".""").lower()
            while goodEquation == False:
                if checkEquation(equation) == True:
                    saveEquation(equation)
                    goodEquation = True
                elif equation == "cancel" or equation == "\"cancel\"":
                    cancel = True
                else:
                    equation = simpledialog.askstring("equation","That is not a valid equation!\nplease type the equation you want to add.\n If you changed your mind, type \"cancel\".").lower()
                    
                
