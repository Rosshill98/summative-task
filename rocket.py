import matplotlib.pyplot as plt
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

    def fuelRemaining(self,time,initialFuel,ejectionRate):
        return max([initialFuel - (ejectionRate * time),0])

    def position(self,time,vectors):
        return vectors['v1'] * time + 0.5 * vectors['a1'] * time**2 + 1/6 * (vectors['a2'] - vectors['a2']) * time**2


    def velocity(self,time,v,a2,a1):
        return v + a2 * time + 1/2 * (a2-a1) * time # only works if t1 and v1 = 0

    def acceleration(self,time,thrust,m,g):
        return (thrust - g*m)/m

    def drawGraph(self,vectors,specs):
        thrust = specs['thrust']
        g = specs['gravity']
        m = specs['baseMass']
        vectors['t2'] = 0
        vectors['v2'] = 0
        increment = 1
        #outputted values
        tList = []
        posList = []
        aList = []
        vList = []
        #instantiating...
        fuelLeft = totalMass = time = 0
        while vectors['t2'] < 1000:
            vectors['t2'] += increment
            time = vectors['t2']
            tList.append(vectors['t2'])

            fuelLeft = self.fuelRemaining(time,specs['fuelAmount'],specs['ejectionRate'])
            if fuelLeft == 0: thrust = 0
            totalMass = m + fuelLeft * specs['fuelMass']

            vectors['a2'] = self.acceleration(time,thrust,totalMass,9.8)
            aList.append(vectors['a2'])

            vectors.pop('x2',None)
            vectors['x2'] = self.position(time,vectors)
            posList.append(vectors['x2'])

            vectors['v2'] = self.velocity(time,vectors['v2'],vectors['a2'],vectors['a1'])
            vList.append(vectors['v2'])
        # print(aList, tList)
        plt.plot(tList,vList)
        plt.show()
