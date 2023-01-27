def ruleSystem(userInput):
    if userInput.wantExpensiveWine == True and userInput.isNewYearEve == True:
        return "Bond's Champagne" #r1
    
    elif userInput.wantExpensiveWine == True and userInput.inEntree == "steak":
        return "Chateau Earl of Bartonville Red" #r2
    
    elif userInput.wantCheapWine == True and userInput.inEntree == "chicken" and userInput.isGuestLiked == False:
        return "Honey Henry's Apple Wine" #r3
    
    elif userInput.wantCheapWine == True and userInput.isEntreeKnown == False:
        return "Toe Lakes Rose" #r4
    
    elif userInput.wantBeer == True and userInput.inEntree == "mexican":
        return "Dos Equis" #r5
    
    elif userInput.wantBeer == True:
        return "Coors" #r6
    
    elif userInput.isGuestHealthNut == True:
        return "Glop" #r7
    
    elif userInput.isGuestHealthNut == True and userInput.doServeCarrots == False:
        return "Carrot Juice" #r8
    
    elif userInput.wantWine == True and userInput.ImpressGuests == True:
        userInput.wantExpensiveWine = True
        return True #r9
    
    elif userInput.wantWine == True:
        userInput.wantCheapWine = True
        return True #r10
    
    elif userInput.isGuestSophisticated == True:
        userInput.wantWine = True
        return True #r11
    
    elif userInput.inEntree == "Mexican":
        userInput.wantBeer = True
        return True #r12
    
    elif userInput.isGuestLiked == False and userInput.isEntreeCateredBy == "not-so-good caterers":
        userInput.wantBeer = True
        return True #r13
    
    elif userInput.doGuestDrinkAlcohol == False:
        return "Water" #r14