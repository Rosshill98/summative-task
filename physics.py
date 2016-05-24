from rocket import rocket
class main:
    def start(self):
        specs = rocket().getSpecs()
        variables = rocket().deriveVectors(specs)
        rocket().drawGraph(variables,specs)

main().start() #initializes the program
