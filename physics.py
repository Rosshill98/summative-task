import sys
sys.setrecursionlimit(5000)
from rocket import rocket
class main:
    def start(self):
        specs = rocket().getSpecs()
        variables = rocket().deriveVectors(specs)
        rocket().drawGraph(variables,specs)

main().start()
