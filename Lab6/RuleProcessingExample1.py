# Example Simple RuleBased System
from typing import List

#Keep track of all facts entered or derived in facts list
facts: List[str] = [""]
#Keep track of all conclusions entered or derived in conclusion list
conclusion: List[str] = [""]
AskQ = True
RuleTriggered = True

def rules(triggerStatus):
    
#for variable in variables:
    while triggerStatus == True:    
        if "Animal has hair" in facts:
            if "Animal is a mammal" not in facts:
                
                facts.append("Animal is a mammal")
                conclusion.append("Animal is a mammal")
                triggerStatus = True
                print("Facts=", facts)
                print("Conclusions=", conclusion)
                return triggerStatus
        
        if "Animal gives milk" in facts:
            if "Animal is a mammal" not in facts:
                
                facts.append("Animal is a mammal")
                conclusion.append("Animal is a mammal")
                triggerStatus = True
                print("Facts=", facts)
                print("Conclusions=", conclusion)
                return triggerStatus
        
        if "Animal has feathers" in facts:
            if "Animal is a bird" not in facts:
                
                facts.append("Animal is a bird")
                conclusion.append("Animal is a bird")
                triggerStatus = True
                print("Facts=", facts)
                print("Conclusions=", conclusion)                
                return triggerStatus
        
        
        if "Animal lays eggs" in facts:
                triggerStatus = True
                print("Facts=", facts)
                print("Conclusions=", conclusion)     
                if "Animal flies" in facts and "Animal lays eggs" in facts:
                    if "Animal is a bird" not in facts:
                        
                        facts.append("Animal is a bird")
                        conclusion.append("Animal is a bird")
                        triggerStatus = True
                        print("Facts=", facts)
                        print("Conclusions=", conclusion)                
                        return triggerStatus
                return triggerStatus
        if "Animal flies" in facts:
                triggerStatus = True
                print("Facts=", facts)
                print("Conclusions=", conclusion)   
                if "Animal flies" in facts and "Animal lays eggs" in facts:
                    if "Animal is a bird" not in facts:
                        
                        facts.append("Animal is a bird")
                        conclusion.append("Animal is a bird")
                        triggerStatus = True
                        print("Facts=", facts)
                        print("Conclusions=", conclusion)                
                        return triggerStatus
                return triggerStatus
        
        
        
           
        if "Animal eats meat" in facts:
                triggerStatus = True
                print("Facts=", facts)
                print("Conclusions=", conclusion)   
                if "Animal eats meat" in facts and "Animal is a mammal" in facts:
                    if "Animal is a carnivore" not in facts:
                        
                        facts.append("Animal is a carnivore")
                        conclusion.append("Animal is a carnivore")
                        triggerStatus = True
                        print("Facts=", facts)
                        print("Conclusions=", conclusion)                
                        return triggerStatus
                
                return triggerStatus
            
        if "Animal is a mammal" in facts:
                triggerStatus = True
                print("Facts=", facts)
                print("Conclusions=", conclusion)      
                if "Animal eats meat" in facts and "Animal is a mammal" in facts:
                    if "Animal is a carnivore" not in facts:
                       
                        facts.append("Animal is a carnivore")
                        conclusion.append("Animal is a carnivore")
                        triggerStatus = True
                        print("Facts=", facts)
                        print("Conclusions=", conclusion)                
                        return triggerStatus
                elif "Animal has pointed teeth" in facts and "Animal has pointed teeth" in facts and "Animal has claws" in facts and "Animal is a mammal" in facts:
                    if "Animal is a carnivore" not in facts:
                        
                        facts.append("Animal is a carnivore")
                        conclusion.append("Animal is a carnivore")
                        triggerStatus = True
                        print("Facts=", facts)
                        print("Conclusions=", conclusion)                
                        return triggerStatus
                elif "Animal has hoofs" in facts and "Animal is a mammal" in facts:
                    if "Animal is an ungulate" not in facts:
                        
                        facts.append("Animal is an ungulate")
                        conclusion.append("Animal is an ungulate")
                        triggerStatus = True
                        print("Facts=", facts)
                        print("Conclusions=", conclusion)                
                        return triggerStatus
                elif "Animal chews cud" in facts and "Animal is a mammal" in facts:
                    if "Animal is an ungulate" not in facts:
                        
                        facts.append("Animal is an ungulate")
                        conclusion.append("Animal is an ungulate")
                        facts.append("Animal is even-toed")
                        conclusion.append("Animal is even-toed")
                        triggerStatus = True
                        print("Facts=", facts)
                        print("Conclusions=", conclusion)                
                        return triggerStatus
                return triggerStatus
        
        if "Animal has pointed teeth" in facts:
                triggerStatus = True
                print("Facts=", facts)
                print("Conclusions=", conclusion)   
                if "Animal has pointed teeth" in facts and "Animal has pointed teeth" in facts and "Animal has claws" in facts and "Animal is a mammal" in facts:
                    if "Animal is a carnivore" not in facts:
                        
                        facts.append("Animal is a carnivore")
                        conclusion.append("Animal is a carnivore")
                        triggerStatus = True
                        print("Facts=", facts)
                        print("Conclusions=", conclusion)                
                        return triggerStatus
                
                return triggerStatus
        
        if "Animal has claws" in facts:
                triggerStatus = True
                print("Facts=", facts)
                print("Conclusions=", conclusion)   
                if "Animal has pointed teeth" in facts and "Animal has pointed teeth" in facts and "Animal has claws" in facts and "Animal is a mammal" in facts:
                    if "Animal is a carnivore" not in facts:
                        
                        facts.append("Animal is a carnivore")
                        conclusion.append("Animal is a carnivore")
                        triggerStatus = True
                        print("Facts=", facts)
                        print("Conclusions=", conclusion)                
                        return triggerStatus
                
                return triggerStatus
            
        if "Animal eyes point forward" in facts:
                triggerStatus = True
                print("Facts=", facts)
                print("Conclusions=", conclusion)   
                if "Animal has pointed teeth" in facts and "Animal has pointed teeth" in facts and "Animal has claws" in facts and "Animal is a mammal" in facts:
                    if "Animal is a carnivore" not in facts:
                        
                        facts.append("Animal is a carnivore")
                        conclusion.append("Animal is a carnivore")
                        triggerStatus = True
                        print("Facts=", facts)
                        print("Conclusions=", conclusion)                
                        return triggerStatus
                
                return triggerStatus
       
        if "Animal has hoofs" in facts:
                triggerStatus = True
                print("Facts=", facts)
                print("Conclusions=", conclusion)   
                if "Animal has hoofs" in facts and "Animal is a mammal" in facts:
                    if "Animal is an ungulate" not in facts:
                        
                        facts.append("Animal is an ungulate")
                        conclusion.append("Animal is an ungulate")
                        triggerStatus = True
                        print("Facts=", facts)
                        print("Conclusions=", conclusion)                
                        return triggerStatus
                
                return triggerStatus
        if "Animal chews cud" in facts:
                triggerStatus = True
                print("Facts=", facts)
                print("Conclusions=", conclusion)   
                if "Animal has hoofs" in facts and "Animal is a mammal" in facts:
                    if "Animal is an ungulate" not in facts:
                        facts.append("Animal is even-toed")
                        conclusion.append("Animal is even-toed")
                        facts.append("Animal is an ungulate")
                        conclusion.append("Animal is an ungulate")
                        triggerStatus = True
                        print("Facts=", facts)
                        print("Conclusions=", conclusion)                
                        return triggerStatus
                
                return triggerStatus
       
        if "Animal is a carnivore" in facts:
                triggerStatus = True
                print("Facts=", facts)
                print("Conclusions=", conclusion)      
                if "Animal has a tawny color" in facts and "Animal has dark spots" in facts and "Animal is a carnivore" in facts:
                    if "Animal is a cheetah" not in facts:
                       
                        facts.append("Animal is a cheetah")
                        conclusion.append("Animal is a cheetah")
                        triggerStatus = False
                        print("Facts=", facts)
                        print("Conclusions=", conclusion)                
                        return triggerStatus
                elif "Animal has a tawny color" in facts and "Animal has black stripes" in facts and "Animal is a carnivore" in facts:
                    if "Animal is a tiger" not in facts:
                       
                        facts.append("Animal is a tiger")
                        conclusion.append("Animal is a tiger")
                        triggerStatus = False
                        print("Facts=", facts)
                        print("Conclusions=", conclusion)                
                        return triggerStatus
                
                return triggerStatus
            
        if "Animal has a tawny color" in facts:
                triggerStatus = True
                print("Facts=", facts)
                print("Conclusions=", conclusion)   
                if "Animal has a tawny color" in facts and "Animal has dark spots" in facts and "Animal is a carnivore" in facts:
                    if "Animal is a cheetah" not in facts:
                       
                        facts.append("Animal is a cheetah")
                        conclusion.append("Animal is a cheetah")
                        triggerStatus = False
                        print("Facts=", facts)
                        print("Conclusions=", conclusion)                
                        return triggerStatus
                elif "Animal has long legs" in facts and "Animal has a long neck" in facts and "Animal has a tawny color" in facts and "Animal has dark spots" in facts and "Animal is an ungulate" in facts:
                    if "Animal is a giraffe" not in facts:
                       
                        facts.append("Animal is a giraffe")
                        conclusion.append("Animal is a giraffe")
                        triggerStatus = False
                        print("Facts=", facts)
                        print("Conclusions=", conclusion)                
                        return triggerStatus
                
                return triggerStatus
            
        if "Animal has dark spots" in facts:
                triggerStatus = True
                print("Facts=", facts)
                print("Conclusions=", conclusion)   
                if "Animal has a tawny color" in facts and "Animal has dark spots" in facts and "Animal is a carnivore" in facts:
                    if "Animal is a cheetah" not in facts:
                       
                        facts.append("Animal is a cheetah")
                        conclusion.append("Animal is a cheetah")
                        triggerStatus = False
                        print("Facts=", facts)
                        print("Conclusions=", conclusion)                
                        return triggerStatus
                elif "Animal has long legs" in facts and "Animal has a long neck" in facts and "Animal has a tawny color" in facts and "Animal has dark spots" in facts and "Animal is an ungulate" in facts:
                    if "Animal is a giraffe" not in facts:
                       
                        facts.append("Animal is a giraffe")
                        conclusion.append("Animal is a giraffe")
                        triggerStatus = False
                        print("Facts=", facts)
                        print("Conclusions=", conclusion)                
                        return triggerStatus
                
                return triggerStatus
            
        if "Animal has black stripes" in facts:
                triggerStatus = True
                print("Facts=", facts)
                print("Conclusions=", conclusion)   
                if "Animal has a tawny color" in facts and "Animal has black stripes" in facts and "Animal is a carnivore" in facts:
                    if "Animal is a tiger" not in facts:
                       
                        facts.append("Animal is a tiger")
                        conclusion.append("Animal is a tiger")
                        triggerStatus = False
                        print("Facts=", facts)
                        print("Conclusions=", conclusion)                
                        return triggerStatus
                elif "Animal has a white color" in facts and "Animal has black stripes" in facts and "Animal is an ungulate" in facts:
                    if "Animal is a zebra" not in facts:
                       
                        facts.append("Animal is a zebra")
                        conclusion.append("Animal is a zebra")
                        triggerStatus = False
                        print("Facts=", facts)
                        print("Conclusions=", conclusion)                
                        return triggerStatus
                
                return triggerStatus
            
        if "Animal is an ungulate" in facts:
                triggerStatus = True
                print("Facts=", facts)
                print("Conclusions=", conclusion)      
                if "Animal has long legs" in facts and "Animal has a long neck" in facts and "Animal has a tawny color" in facts and "Animal has dark spots" in facts and "Animal is an ungulate" in facts:
                    if "Animal is a giraffe" not in facts:
                       
                        facts.append("Animal is a giraffe")
                        conclusion.append("Animal is a giraffe")
                        triggerStatus = False
                        print("Facts=", facts)
                        print("Conclusions=", conclusion)                
                        return triggerStatus
                elif "Animal has a white color" in facts and "Animal has black stripes" in facts and "Animal is an ungulate" in facts:
                    if "Animal is a zebra" not in facts:
                       
                        facts.append("Animal is a zebra")
                        conclusion.append("Animal is a zebra")
                        triggerStatus = False
                        print("Facts=", facts)
                        print("Conclusions=", conclusion)                
                        return triggerStatus
                
                return triggerStatus
            
        if "Animal has long legs" in facts:
                triggerStatus = True
                print("Facts=", facts)
                print("Conclusions=", conclusion)      
                if "Animal has long legs" in facts and "Animal has a long neck" in facts and "Animal has a tawny color" in facts and "Animal has dark spots" in facts and "Animal is an ungulate" in facts:
                    if "Animal is a giraffe" not in facts:
                       
                        facts.append("Animal is a giraffe")
                        conclusion.append("Animal is a giraffe")
                        triggerStatus = False
                        print("Facts=", facts)
                        print("Conclusions=", conclusion)                
                        return triggerStatus
                elif "Animal does not fly" in facts and "Animal has long legs" in facts and "Animal has a long neck" in facts and "Animal is black and white" in facts and "Animal is a bird" in facts:
                    if "Animal is a penguin" not in facts:
                       
                        facts.append("Animal is a penguin")
                        conclusion.append("Animal is a penguin")
                        triggerStatus = False
                        print("Facts=", facts)
                        print("Conclusions=", conclusion)                
                        return triggerStatus
                
                
                return triggerStatus
        if "Animal has a long neck" in facts:
                triggerStatus = True
                print("Facts=", facts)
                print("Conclusions=", conclusion)      
                if "Animal has long legs" in facts and "Animal has a long neck" in facts and "Animal has a tawny color" in facts and "Animal has dark spots" in facts and "Animal is an ungulate" in facts:
                    if "Animal is a giraffe" not in facts:
                       
                        facts.append("Animal is a giraffe")
                        conclusion.append("Animal is a giraffe")
                        triggerStatus = False
                        print("Facts=", facts)
                        print("Conclusions=", conclusion)                
                        return triggerStatus
                elif "Animal does not fly" in facts and "Animal has long legs" in facts and "Animal has a long neck" in facts and "Animal is black and white" in facts and "Animal is a bird" in facts:
                    if "Animal is a penguin" not in facts:
                       
                        facts.append("Animal is a penguin")
                        conclusion.append("Animal is a penguin")
                        triggerStatus = False
                        print("Facts=", facts)
                        print("Conclusions=", conclusion)                
                        return triggerStatus
                
                
                return triggerStatus
        if "Animal has a white color" in facts:
                triggerStatus = True
                print("Facts=", facts)
                print("Conclusions=", conclusion)      
                if "Animal has a white color" in facts and "Animal has black stripes" in facts and "Animal is an ungulate" in facts:
                    if "Animal is a zebra" not in facts:
                       
                        facts.append("Animal is a zebra")
                        conclusion.append("Animal is a zebra")
                        triggerStatus = False
                        print("Facts=", facts)
                        print("Conclusions=", conclusion)                
                        return triggerStatus
                
                
                return triggerStatus
            
        if "Animal is a bird" in facts:
                triggerStatus = True
                print("Facts=", facts)
                print("Conclusions=", conclusion)      
                if "Animal does not fly" in facts and "Animal has long legs" in facts and "Animal has a long neck" in facts and "Animal is black and white" in facts and "Animal is a bird" in facts:
                    if "Animal is a penguin" not in facts:
                       
                        facts.append("Animal is a penguin")
                        conclusion.append("Animal is a penguin")
                        triggerStatus = False
                        print("Facts=", facts)
                        print("Conclusions=", conclusion)                
                        return triggerStatus
                elif "Animal is a good flyer" in facts and "Animal is a bird" in facts:
                    if "Animal is an albatross" not in facts:
                       
                        facts.append("Animal is an albatross")
                        conclusion.append("Animal is an albatross")
                        triggerStatus = False
                        print("Facts=", facts)
                        print("Conclusions=", conclusion)                
                        return triggerStatus
                
                return triggerStatus
        if "Animal is black and white" in facts:
                triggerStatus = True
                print("Facts=", facts)
                print("Conclusions=", conclusion)      
                if "Animal does not fly" in facts and "Animal has long legs" in facts and "Animal has a long neck" in facts and "Animal is black and white" in facts and "Animal is a bird" in facts:
                    if "Animal is a penguin" not in facts:
                       
                        facts.append("Animal is a penguin")
                        conclusion.append("Animal is a penguin")
                        triggerStatus = False
                        print("Facts=", facts)
                        print("Conclusions=", conclusion)                
                        return triggerStatus
                
                
                return triggerStatus
        if "Animal does not fly" in facts:
                triggerStatus = True
                print("Facts=", facts)
                print("Conclusions=", conclusion)      
                if "Animal does not fly" in facts and "Animal has long legs" in facts and "Animal has a long neck" in facts and "Animal is black and white" in facts and "Animal is a bird" in facts:
                    if "Animal is a penguin" not in facts:
                       
                        facts.append("Animal is a penguin")
                        conclusion.append("Animal is a penguin")
                        triggerStatus = False
                        print("Facts=", facts)
                        print("Conclusions=", conclusion)                
                        return triggerStatus
                
                
                return triggerStatus
        if "Animal is a good flyer" in facts:
                triggerStatus = True
                print("Facts=", facts)
                print("Conclusions=", conclusion)      
                if "Animal is a good flyer" in facts and "Animal is a bird" in facts:
                    if "Animal is an albatross" not in facts:
                       
                        facts.append("Animal is a albatross")
                        conclusion.append("Animal is a albatross")
                        triggerStatus = False
                        print("Facts=", facts)
                        print("Conclusions=", conclusion)                
                        return triggerStatus
                
                
                return triggerStatus
            
        
    else:
        triggerStatus = False
        print("Conclusion reached", conclusion)
        return triggerStatus
        
def GetData(triggerStatus):
    if triggerStatus == True:
        Ans = input("\n Do you want to enter a fact (Y/N)?  ")
        if Ans == 'Y':
            print("\nCurrent Facts:  ", facts)
    
            factInput = input("\nEnter a fact:  ")
            #Check whether it is in the list
            if factInput not in facts:
                facts.append(factInput)
                #facts.append("Animal has hair")
            print("\nNew facts", facts)
            return True
        else:
            return False
    else:
        print("Conclusion reached: ", conclusion)
        return
    
# Main
while (AskQ):
    AskQ = GetData(RuleTriggered)
    if RuleTriggered == True:
        RuleTriggered = rules(RuleTriggered)
print("Finished Rule Processing")   
	
       
    

