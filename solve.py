from sympy import solveset,sympify,symbols,Eq
from equations import equations
class solve:
    def findEquation(self,vars,eqType):
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

    def solveEq(self,exp,expVars,vars):
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
        symbol, answer = str(x), solveset(Eq(RHS,LHS),x)
        answer = str(answer).replace('{','').replace('}','')
        if(symbol == 't1'):
            return symbol, answer.split(',')[0]
        elif(symbol == 't2'):
            return symbol, answer.split(',')[-1]
        else:
            return symbol, answer
