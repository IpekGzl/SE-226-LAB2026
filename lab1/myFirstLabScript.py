import math

class myFirstLabScript:

    def run(self):


        name = input("What is your name? ")
        print("Hello", name)

        sid = input("What is your Student ID? ")
        print("Your ID is", sid)

        sec = int(input("Enter total seconds: "))
        hour = sec // 3600
        sec = sec % 3600
        minute = sec // 60
        sec = sec % 60
        print(hour, "hours,", minute, "minutes,", sec, "seconds")

        x1 = float(input("x1: "))
        y1 = float(input("y1: "))
        x2 = float(input("x2: "))
        y2 = float(input("y2: "))
        d = math.sqrt((x2-x1)**2 + (y2-y1)**2)
        print("Distance:", d)

        print("*******\n *****\n  ***\n   *")


lab = myFirstLabScript()
lab.run()
