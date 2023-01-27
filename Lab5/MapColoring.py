# map_coloring.py
# From Classic Computer Science Problems in Python Chapter 3
# Copyright 2018 David Kopec
# Adopted from Reference:  
# https://github.com/davecom/ClassicComputerScienceProblemsInPython/blob/master/Chapter3/csp.py

from csp import Constraint, CSP
from typing import Dict, List, Optional


class MapColoringConstraint(Constraint[str, str]):
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
    variables: List[str] = ["WA", "NT", "SA", "Q", "NSW", "V", "T"]
    domains: Dict[str, List[str]] = {}
	
    for variable in variables:
        domains[variable] = ["red", "green", "blue"]
    
    csp: CSP[str, str] = CSP(variables, domains)
    csp.add_constraint(MapColoringConstraint("WA", "NT"))
    csp.add_constraint(MapColoringConstraint("WA", "SA"))
    csp.add_constraint(MapColoringConstraint("SA", "NT"))
    csp.add_constraint(MapColoringConstraint("Q", "NT"))
    csp.add_constraint(MapColoringConstraint("Q", "SA"))
    csp.add_constraint(MapColoringConstraint("Q", "NSW"))
    csp.add_constraint(MapColoringConstraint("NSW", "SA"))
    csp.add_constraint(MapColoringConstraint("V", "SA"))
    csp.add_constraint(MapColoringConstraint("V", "NSW"))
    csp.add_constraint(MapColoringConstraint("V", "T"))
    solution: Optional[Dict[str, str]] = csp.backtracking_search()
    if solution is None:
        print("No solution found!")
    else:
        print(solution)