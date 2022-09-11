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
#returns True if equation is valid
def checkEquation(e):
    i = 0
    while i < len(e):
        if e[i].isdigit() or checkStrForSigns(e[i]):
            i += 1
        elif e[i] == 's' or 'c':
            if checkForValidLetterSign(e, i) == 0:
                return False
            else:
                i += 2 + checkForValidLetterSign(e, i)
        else:
            return False
    return True
#if there's a lowercase letter, checks for if its a valid sign. n is place of letter in str e
#0 == invalid, any other value == valid
def checkForValidLetterSign(e, n):
    global equation
    equation = e
    newN = n + 1
    lenOfSign = 0
    while True:
        if newN == len(e):
            e += ')'
            return checkForValidLetterSign(e, n)
        elif e[newN] == ')':
            word = e[n:newN+1]
            #variable for expression between parenthases
            between = e[n+5:newN]
            if checkEquation(between):
                if word == 'sqrt(' + between + ')' or 'sin(' + between + ')' or 'cos(' + between + ')':
                    return lenOfSign
                else:
                    return 0
            else:
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
    whatToDo = simpledialog.askstring("CalcStore", """What do you want to do?
    To look at an equation, type "look."
    To add a new equation, type "add."
    To edit an equation, type "edit."
    To solve an equation, type "solve."
    """)
    
    match whatToDo:
        case None:
            quit()
        case "add":
            equation = simpledialog.askstring("Add Equation", "Please type the equation you want to add.")
            
            while True:
                if equation == None:
                    break
                if checkEquation(equation):
                    saveEquation(equation)
                    break
                else:
                    equation = simpledialog.askstring("Add Equation", """That is not a valid equation!
    Please type the equation you want to add.""")
