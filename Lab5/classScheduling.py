
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
    variables: List[tuple] = [("Room1", "1pm", "Teacher1"), ("Room2", "2pm", "Teacher2"), ("Room3", "3pm", "Teacher3")]
    domains: Dict[str, List[str]] = {}
	
    for variable in variables:
        domains[variable] = ["Intro to Tech", "Advanced Programming", "Networking Basics"]
    
    csp: CSP[str, str] = CSP(variables, domains)
    csp.add_constraint(classScheduling(("Room1", "1pm", "Teacher1"), ("Room2", "2pm", "Teacher2")))
    csp.add_constraint(classScheduling(("Room1", "1pm", "Teacher1"), ("Room3", "3pm", "Teacher3")))
    csp.add_constraint(classScheduling(("Room2", "2pm", "Teacher2"), ("Room3", "3pm", "Teacher3")))
    
    
    solution: Optional[Dict[str, str]] = csp.backtracking_search()
    if solution is None:
        print("No solution found!")
    else:
        print(solution)