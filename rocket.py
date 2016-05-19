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
        vectors['t2'] = 0
        increment = 0.1
        yList = []
        posList = []
        aList = []
        vList = []
        while vectors['t2'] < 1000:
            vectors['t2'] += increment
            fuelRemaining = fuelRemaining(time,specs['fuelAmount'],specs['ejectionRate'])
            totalMass = m + fuelRemaining * specs['fuelMass']
            vectors['a2'] = acceleration(time,thrust,totalMass)
            time = vectors['t2']
            vectors['x2'] = position(time)
            vectors['v2'] = velocity(time)
            vectors['m'] = mass(time)
    def fuelRemaining(time):
        return initialFuel - (ejectionRate * time)

    def position(time):

    def velocity(time):
        pass
    def acceleration(time):
        

    def mass(time):
        pass
