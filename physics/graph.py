from termcolor import colored # coloured standard output
from rocket import rocket
import matplotlib.pyplot as plt # module used for graphing
class graph:
    # uses the rocket helper functions to make lists of x2, a2, v2 and values, which will be eventually displayed on graphs with time.
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

            fuelLeft = rocket().fuelRemaining(time,specs['fuelAmount'],specs['ejectionRate'])
            if fuelLeft == 0: thrust = 0
            totalMass = m + fuelLeft * specs['fuelMass']

            gravAcc = rocket().accDueToGravity(vectors['x2'])
            vectors['a2'] = rocket().acceleration(time,thrust,totalMass,gravAcc)
            aList.append(vectors['a2'])

            vectors.pop('x2',None)
            vectors['x2'] = rocket().position(time,vectors)
            if vectors['x2'] < 0:
                print colored("Your craft has collided with the ground.\n", 'red')
                crashed = True
                break
            posList.append(vectors['x2'])
            vectors['v2'] = rocket().velocity(time,vectors['v2'],vectors['a2'],vectors['a1'])
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
