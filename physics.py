from equations import equations
from solve import solve
from rocket import rocket
class main:
    def start(self):
        specs = rocket().getSpecs()
        variables, eqType = rocket().deriveVectors(specs), 3
        # variables, eqType = self.getVariables() # get known variables & type of problem
        rocket().drawGraph(variables,specs)

    def getVariables(self):
        eqType = int(raw_input("Enter 1 for constant velocity, 2 for constant aceleration, or 3 for constant jerk: "))
        print("Please enter the know variables, leaving fields blank for unknown or unused variables.")
        print("LEAVE ONE BLANK!")
        oldVars = {'t1':'', 'a1':'', 'a2':'', 'j':'', 'v1':'', 'x1':'', 't2':'', 'v2':'', 'x2':''}
        if eqType in [1,2,3]:
            oldVars['t1'] = raw_input("t1: ")
            oldVars['v1'] = raw_input("v1: ")
            oldVars['x1'] = raw_input("x1: ")
            oldVars['t2'] = raw_input("t2: ")
            oldVars['x2'] = raw_input("x2: ")
        if eqType in [2,3]:
            oldVars['a1'] = raw_input("a1: ")
        if eqType == 3:
            oldVars['a2'] = raw_input("a2: ")
            oldVars['j'] = raw_input("j: ")
        variables = {}
        for name, value in oldVars.iteritems():
            if value != '': variables[name] = float(value)
        return variables, eqType

main().start()
