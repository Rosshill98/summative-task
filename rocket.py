import matplotlib.pyplot as plt
from solve import solve
class rocket:
    def getSpecs(self):
        baseMass = raw_input("Enter the base mass (without fuel) of the rocket (kg): ")
        thrust = raw_input("Enter the thrust of the rocket (kj): ")
        fuelAmount = raw_input("Enter the amount of rocket fuel (L): ")
        fuelMass = raw_input("Enter the mass of the fuel, per litre (kg): ")
        ejectionRate = raw_input("Enter the rate at which the fuel is ejected from the rocket (L/s): ")
        gravity = raw_input("Enter acceleration due to gravity, a planet name, or leave blank for Earth: ")
        specs = {'baseMass':baseMass,'thrust':thrust,'fuelAmount':fuelAmount,'fuelMass':fuelMass,'ejectionRate':ejectionRate,'gravity':gravity}
        for key in specs: specs[key] = float(specs[key])
        return specs

    def deriveVectors(self,specs):
        thrust = specs['thrust']
        g = specs['gravity']
        m = specs['baseMass']
        fm = specs['fuelMass'] * specs['fuelAmount']
        a1 = (thrust - g*(m+fm))/(m+fm)
        values = {'v1':0,'t1':0,'a1':a1,'x1':0}
        return values

    def drawGraph(self,vectors,specs):
        thrust = specs['thrust']
        g = specs['gravity']
        m = specs['baseMass']
        answer = 0
        vectors['t2'] = 0
        equation = solve().findEquation(vectors.keys(),3) # find usable equation
        x = []
        y = []
        increment = 0.1
        while float(answer) < 1000 and float(answer) > -1000:
            vectors['t2'] += increment
            specs['fuelAmount'] -= specs['ejectionRate'] * increment
            fm = specs['fuelMass'] * specs['fuelAmount']
            vectors['a2'] = (thrust - g*(m+fm))/(m+fm)
            x.append(vectors['t2'])
            symbol, answer = solve().solveEq(equation[0],equation[1],vectors) # Solve for the 1 unknown
            y.append(answer)
            print(answer)
        plt.plot(x,y)
        plt.show()
