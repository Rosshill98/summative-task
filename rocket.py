class rocket:
    def getSpecs(self):
        baseMass = raw_input("Enter the base mass (without fuel) of the rocket (kg): ")
        thrust = raw_input("Enter the thrust of the rocket (kj): ")
        fuelAmount = raw_input("Enter the amount of rocket fuel (L): ")
        fuelMass = raw_input("Enter the mass of the fuel, per litre (kg): ")
        ejectionRate = raw_input("Enter the rate at which the fuel is ejected from the rocket (L/s): ")
        gravity = raw_input("Enter acceleration due to gravity, a planet name, or leave blank for Earth: ")
        return {'baseMass':baseMass,'thrust':thrust,'fuelAmount':fuelAmount,'fuelWeight':fuelWeight,'ejectionRate':ejectionRate,'gravity':gravity}
    def deriveVectors(self,specs):
        thrust = specs['thrust']
        g = specs['gravity']
        m = specs['baseMass']
        fm = specs['fuelMass'] * specs['fuelAmount']
        a1 = (thrust - g*(m+fm))/(m+fm)
        a2 = (thrust - g*m)/m
        
