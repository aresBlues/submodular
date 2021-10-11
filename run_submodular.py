from typing import Set, TypeVar

from submodmax.abstract_optimizer import AbstractSubmodularFunction, AbstractOptimizer
from submodmax.randomized_double_greedy_search import RandomizedDoubleGreedySearch

E = TypeVar('E')


class ObjectiveFunction(AbstractSubmodularFunction):
    def evaluate(self, input_set: Set[int]) -> float:
        if input_set == set():
            return 0
        elif input_set == {1}:
            return  5
        elif input_set == {2}:
            return 5  
        elif input_set == {3}:
            return 5
        elif input_set == {4}:
            return 5
        elif input_set == {1,2}:
            return 8
        elif input_set == {1,3}:
            return 9
        elif input_set == {1,4}:
            return 10
        elif input_set == {2,3}:
            return 4
        elif input_set == {2,4}:
            return 1
        elif input_set == {3,4}:
            return 
        elif input_set == {1, 2, 3}:
            return 4
        elif input_set == {1, 2, 4}:
            return 5
        elif input_set == {1, 3, 4}:
            return 3
        elif input_set == {2, 3, 4}:
            return 2
        elif input_set == {1, 2, 3, 4}:
            return 2
        else:
            raise Exception(f"The input set was not expected: {input_set} ")

def run_example():
    

    ground_set: Set[int] = {1, 2, 3, 4, 5}
    submodular_objective_function = ObjectiveFunction()

    optimizer: AbstractOptimizer = RandomizedDoubleGreedySearch(
        objective_function=submodular_objective_function,
        ground_set=ground_set,
        debug=False
    )
    local_optimum: Set[int] = optimizer.optimize()
    
    print(f"The local optimum {local_optimum}")
   


if __name__ == '__main__':
    run_example()
