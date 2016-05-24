import matplotlib.pyplot as plt # module used for graphing
from termcolor import colored # coloured standard output
class rocket:
    def getSpecs(self): # gets the rocket's specifications, and returns them to class main
        print colored("\nThis planet has the same mass and radius of earth, but no atmosphere.\n",'green')
        baseMass = raw_input("Enter the base mass (without fuel) of the rocket (kg): ")
        thrust = raw_input("Enter the thrust of the rocket (N): ")
        fuelAmount = raw_input("Enter the amount of rocket fuel (L): ")
        fuelMass = raw_input("Enter the mass of the fuel, per litre (kg): ")
        ejectionRate = raw_input("Enter the rate at which the fuel is ejected from the rocket (L/s): ")
        length = raw_input("How long should the program simulate? (s) ")
        print("") # line break
        specs = {'baseMass':baseMass,'thrust':thrust,'fuelAmount':fuelAmount,'fuelMass':fuelMass,'ejectionRate':ejectionRate,'length':length}
        for key in specs: specs[key] = float(specs[key])
        return specs

    # from the rocket's specifications, derives the rocket's initial vectors. Most will be 0, except acceleration which starts as non-zero.
    def deriveVectors(self,specs):
        thrust = specs['thrust']
        m = specs['baseMass']
        fm = specs['fuelMass'] * specs['fuelAmount']
        a1 = (thrust - self.accDueToGravity(0)*(m+fm))/(m+fm)
        values = {'v1':0,'t1':0,'a1':a1,'x1':0,'t2':0,'v2':0,'x2':0}
        return values

    #given time, initialFuel, and ejectionRate, returns the amount of remaining fuel
    def fuelRemaining(self,time,initialFuel,ejectionRate):
        return max([initialFuel - (ejectionRate * time),0]) # lowest value it returns will be 0. No negatives.

    # acceleration do to gravity changes based on the rocket's displacement
    def accDueToGravity(self,d):
        mass = 5.972*10**24 # the earth's mass
        r = 6.371*10**6 + d # the earth's radius + displacement
        G = 6.67408*10**-11 # the gravitational constant
        return (G * mass)/(r*r)

    def position(self,time,vectors):
        return vectors['v1'] * time + 0.5 * vectors['a1'] * time**2 + 1/6 * (vectors['a2'] - vectors['a1']) * time**2 # time = 0

    def velocity(self,time,v,a2,a1):
        return v + a2 * time + 1/2 * (a2-a1) * time # only works if t1 and v1 = 0

    # where g is acceleration do to gravity, and m is total current mass
    def acceleration(self,time,thrust,m,g):
        return (thrust - g*m)/m

    # uses the above helper functions to make lists of x2, a2, v2 and values, which will be eventually displayed on graphs with time.
    def drawGraph(self,vectors,specs):
        crashed = False
        thrust = specs['thrust']
        m = specs['baseMass']
        increment = 1 # how many seconds pass every iteration
        tList = []
        posList = []
        aList = []
        vList = [] #outputted values
        #instantiating...
        fuelLeft = 0
        totalMass = 0
        time = 0
        while vectors['t2'] < specs['length']: #How many seconds the program lasts for.
            vectors['t2'] += increment
            time = vectors['t2']
            tList.append(vectors['t2'])

            fuelLeft = self.fuelRemaining(time,specs['fuelAmount'],specs['ejectionRate'])
            if fuelLeft == 0: thrust = 0
            totalMass = m + fuelLeft * specs['fuelMass']

            gravAcc = self.accDueToGravity(vectors['x2'])
            vectors['a2'] = self.acceleration(time,thrust,totalMass,gravAcc)
            aList.append(vectors['a2'])

            vectors.pop('x2',None)
            vectors['x2'] = self.position(time,vectors)
            if vectors['x2'] < 0:
                print colored("Your craft has collided with the ground.\n", 'red')
                crashed = True
                break
            posList.append(vectors['x2'])
            vectors['v2'] = self.velocity(time,vectors['v2'],vectors['a2'],vectors['a1'])
            vList.append(vectors['v2'])
        if crashed == False:
            self.display('Acceleration','M/S^2',aList,tList)
            self.display('Displacement','M',posList,tList)
            self.display('Velocity','M/S',vList,tList)
            plt.show()
    def display(self,s,unit,variable,time):
        fig = plt.figure()
        plt.plot(time,variable)
        fig.suptitle('{0} vs. Time'.format(s), fontsize=18)
        plt.xlabel('Time ($s$)', fontsize=14)
        plt.ylabel("{0} (${1}$)".format(s,unit), fontsize=14)
        ax = plt.gca()
        ax.minorticks_on()
        plt.grid(b=True, which='major', color='0.7', linestyle='-')
        plt.grid(b=True, which='minor', color='0.9', linestyle='-')
        plt.draw()
