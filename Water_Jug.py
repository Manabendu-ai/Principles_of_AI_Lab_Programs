
class WaterJug:

    def __init__(self, jug1 : int, jug2: int, goal : int):
        self.__jug1 = jug1
        self.__jug2 = jug2
        self.__goal = goal
        self.__a = 0
        self.__b = 0

    def gcd(self, a, b):
        while b != 0:
            a, b, = b, a%b
        return a
    
    def run(self):
        if(self.__goal % self.gcd(self.__jug1, self.__jug2) != 0):
            print("No Soultion Exists!")
            return
        a = self.__a
        b = self.__b

        goal = self.__goal
        jug1 = self.__jug1
        jug2 = self.__jug2

        while a != goal and b != goal:
            if a == 0:
                a = jug1
                print(f"Fill Jug1 -> ({a}, {b})")

            if b==jug2:
                b = 0
                print(f"Empty Jug2 -> ({a}, {b})")

            else:
                transfer = min(a, jug2 - b)
                a -= transfer
                b += transfer
                print(f"Pour Jug1 -> Jug2 -> ({a}, {b})")

        print("\nGoal Achieved!")


if __name__ == "__main__":
    jug1, jug2, goal = map(int, input("Enter Jug1, Jug2 and Goal: ").split(","))
    water = WaterJug(jug1, jug2, goal)
    water.run()