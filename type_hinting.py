from typing import List

# this tells that the sequance must be in list and the return value is float(just a help for developer)
def list_avg(sequence: List) -> float:
    return sum(sequence)/len(sequence)

list_avg(123)