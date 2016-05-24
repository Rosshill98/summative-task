from rocket import rocket
from graph import graph
class main:
    def start(self):
        specs = rocket().getSpecs()
        variables = rocket().deriveVectors(specs)
        graph().drawGraph(variables,specs)

main().start() #initializes the program
