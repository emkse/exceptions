Bestelling = {}

def addPizzatoList():
    yn = input("Wilt u nog een pizza? [J/N] \n")
    if yn == "J":
        print(Bestelling)
        getPizzaChoice()
    elif yn == "N":
            print(Bestelling)
            exit()

def numberSize():
    global persoonKeuze
    if persoonKeuze <= 1:
        persoonKeuze = "Small"
        Bestelling["Bestelling: "] = persoonKeuze
        addPizzatoList()
    elif persoonKeuze <= 2:
        persoonKeuze = "Medium"
        Bestelling["Bestelling: "] = persoonKeuze
        addPizzatoList()
    elif persoonKeuze <= 3:
        persoonKeuze = "Large"
        Bestelling["Bestelling: "] = persoonKeuze
        addPizzatoList()


def getPizzaChoice():
    global persoonKeuze
    while True:
        print("""\033[0m
        Kies uw pizza:
            [1] Small
            [2] Medium
            [3] Large
            """)
        try:
            persoonKeuze = int(input("Kies hier een pizza: "))
            numberSize()
        except ValueError:
            print("Sorry maar ik snap u niet.")
            getPizzaChoice()    
        
getPizzaChoice()