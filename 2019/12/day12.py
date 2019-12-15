class Moon:

    def __init__(self, position):
        self.position = position
        self.velocity = [0, 0, 0]

    def applyVelocity(self):
        self.position[0] += self.velocity[0]
        self.position[1] += self.velocity[1]
        self.position[2] += self.velocity[2]
    
    def applyGravity(self, otherMoon):
        for i in range(3):
            if self.position[i] < otherMoon.position[i]:
                self.velocity[i] += 1
            elif self.position[i] > otherMoon.position[i]:
                self.velocity[i] -= 1
    
    def getEnergy(self):
        pot = abs(self.position[0]) + abs(self.position[1]) + abs(self.position[2])
        kin = abs(self.velocity[0]) + abs(self.velocity[1]) + abs(self.velocity[2])
        return pot*kin

    def print(self):
        print(self.position, self.velocity, self.getEnergy())

def gcd(a, b) :
    while b > 0:
        c = a % b
        a = b
        b = c
    return a

def lcm(a, b):
    return a*b / gcd(a,b)

# i assume, that the moons are already on their circular motion. So the first state they will pass again is the initial state.
# the assumption has to be proven
def getPeriods(moons):

    initialStates = ["", "", ""]
    periods = [0, 0, 0]

    steps = 0
    while periods[0] == 0 or periods[1] == 0 or periods[2] == 0:
        for moon in moons:
            for otherMoon in moons:
                moon.applyGravity(otherMoon)
        
        for moon in moons:
            moon.applyVelocity()

        stateX = ""
        stateY = ""
        stateZ = ""
        for moon in moons:
            stateX += str(moon.position[0]) + "|" + str(moon.velocity[0]) + "|"
            stateY += str(moon.position[1]) + "|" + str(moon.velocity[1]) + "|"
            stateZ += str(moon.position[2]) + "|" + str(moon.velocity[2]) + "|"

        if(steps == 0):
            initialStates[0] = stateX
            initialStates[1] = stateY
            initialStates[2] = stateZ
        else:
            if periods[0] == 0 and stateX == initialStates[0]:
                periods[0] = steps
            if periods[1] == 0 and stateY == initialStates[1]:
                periods[1] = steps
            if periods[2] == 0 and stateZ == initialStates[2]:
                periods[2] = steps

        steps += 1
    
    return periods


#moon1 = Moon([-1, 0, 2])
#moon2 = Moon([2, -10, -7])
#moon3 = Moon([4, -8, 8])
#moon4 = Moon([3, 5, -1])
#
#moon1 = Moon([-8, -10, 0])
#moon2 = Moon([5, 5, 10])
#moon3 = Moon([2, -7, 3])
#moon4 = Moon([9, -8, -3])

moon1 = Moon([5, -1, 5])
moon2 = Moon([0, -14, 2])
moon3 = Moon([16, 4, 0])
moon4 = Moon([18, 1, 16])

moons = [moon1, moon2, moon3, moon4]

periods = getPeriods(moons)
print(periods)
print(lcm(periods[0], lcm(periods[1], periods[2])))
