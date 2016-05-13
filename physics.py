from equations import equations
from solve import solve

class main:
    def start(self):
        variables, eqType = self.getVariables() # get known variables & type of problem
        equation = solve().findEquation(variables.keys(),eqType) # find usable equation
        symbol, answer = solve().solveEq(equation[0],equation[1],variables) # Solve for the 1 unknown
        answer = str(answer).replace('{','').replace('}','')
        print("\n{0} = {1}".format(symbol,answer))

    def getVariables(self):
        eqType = int(raw_input("Enter 1 for constant velocity, 2 for constant aceleration, or 3 for constant jerk: "))
        print("Please enter the know variables, leaving fields blank for unknown or unused variables.")
        print("LEAVE ONE BLANK!")
        oldVars = {'t1':"", 'a1':"", 'a2':"", 'j':"", 'v1':"", 'x1':"", 'x1':"", 't2':"", 'v2':"", 'x2':""}
        if eqType == 1:
            oldVars['t1'] = raw_input("t1: ")
            oldVars['v1'] = raw_input("v1: ")
            oldVars['x1'] = raw_input("x1: ")
            oldVars['t2'] = raw_input("t2: ")
            oldVars['x2'] = raw_input("x2: ")
        elif eqType == 2:
            oldVars['t1'] = raw_input("t1: ")
            oldVars['a'] = raw_input("a: ")
            oldVars['v1'] = raw_input("v1: ")
            oldVars['x1'] = raw_input("x1: ")
            oldVars['t2'] = raw_input("t2: ")
            oldVars['v2'] = raw_input("v2: ")
            oldVars['x2'] = raw_input("x2: ")
        elif eqType == 3:
            oldVars['t1'] = raw_input("t1: ")
            oldVars['a1'] = raw_input("a1: ")
            oldVars['a2'] = raw_input("a2: ")
            oldVars['j'] = raw_input("j: ")
            oldVars['v1'] = raw_input("v1: ")
            oldVars['x1'] = raw_input("x1: ")
            oldVars['t2'] = raw_input("t2: ")
            oldVars['v2'] = raw_input("v2: ")
            oldVars['x2'] = raw_input("x2: ")
        variables = {}
        for name, value in oldVars.iteritems():
            if value != "": variables[name] = float(value)
        return variables, eqType

main().start()
