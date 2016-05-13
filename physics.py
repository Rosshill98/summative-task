from sympy import solveset,sympify,symbols,Eq
from equations import equations

def main():
    variables, eqType = getVariables() # get known variables & type of problem
    equation = findEquation(variables.keys(),eqType) # find usable equation
    symbol, answer = solveEq(equation[0],equation[1],variables) # Solve for the 1 unknown
    answer = str(answer).replace('{','').replace('}','')
    print("\n{0} = {1}".format(symbol,answer))

def getVariables():
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

def findEquation(vars,eqType):
    #change so it allows for 1 missing var
    goodEqs = []
    if eqType == 1: eqs = equations.constantV
    elif eqType == 2: eqs = equations.constantA
    elif eqType == 3: eqs = equations.constantJ
    for equation in eqs:
        missing = 0
        goodEqs.append(equation)
        for variable in equation[1]:
            if variable not in vars:
                missing += 1
            if missing == 2:
                goodEqs.pop()
                break
    return(goodEqs[0])

def solveEq(exp,expVars,vars):
    LHS = exp.split(" = ")[0]
    RHS = exp.split(" = ")[1]
    LHS = sympify(LHS)
    RHS = sympify(RHS)
    for symbol, value in vars.iteritems():
        LHS = LHS.subs(symbol,value)
        RHS = RHS.subs(symbol,value)
    for symbol in expVars:
        if symbol not in vars.keys():
            x = symbols(symbol)
            break
    return str(x), solveset(Eq(RHS,LHS),x)

main()
