
from csp import Constraint, CSP
from typing import Dict, List, Optional


class classScheduling(Constraint[str, str]):
    def __init__(self, place1: str, place2: str) -> None:
        super().__init__([place1, place2])
        self.place1: str = place1
        self.place2: str = place2

    def satisfied(self, assignment: Dict[str, str]) -> bool:
        # If either map location (place) is not in the assignment 
		# then it is not yet possible for colors to conflict
        if self.place1 not in assignment or self.place2 not in assignment:
            return True
        
		# check if color assigned to place1 is not equal to place2
        return assignment[self.place1] != assignment[self.place2]


if __name__ == "__main__":
    Professors: List[str] = ["Professor Jim", "Professor Mike", "Professor George"]
    Rooms: List[str] = ["Room1", "Room2", "Room3", "Room4"]
    Courses: List[str] = ["Easy", "Medium", "Hard"]
    Time: List[str] = ["1", "2", "3", "4", "5"]
    domains: Dict[str, List[str]] = {}
	
    print (Rooms[1])
    
    #Assign allowabe values to each variable in the variables list
    for variable in Professors:
        domains[variable] = ["Scheduled", "Free"]
        
    csp: CSP[str, str] = CSP(Professors, domains)
    csp.add_constraint(classScheduling("Professor Jim", "Professor George"))
        
    for variable in Rooms:
        domains[variable] = ["Occupied", "Not Occupied"]
    
    csp: CSP[str, str] = CSP(Professors, domains)
    
    csp: CSP[str, str] = CSP(Rooms, domains)
    
    solution: Optional[Dict[str, str]] = csp.backtracking_search()
    if solution is None:
        print("No solution found!")
    else:
        print(solution)