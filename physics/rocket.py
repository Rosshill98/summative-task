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
