from rocket import rocket
from graph import graph
def main():
    specs = rocket().getSpecs()
    variables = rocket().deriveVectors(specs)
    graph().drawGraph(variables,specs)

main() #initializes the program
