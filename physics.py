from rocket import rocket
class main:
    def start(self):
        specs = rocket().getSpecs()
        variables, eqType = rocket().deriveVectors(specs), 3
        rocket().drawGraph(variables,specs)

main().start()
