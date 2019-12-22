#---------------------------------------
#=======================================
#
# Scientific electricity equation solver
# by Renaud Recerf
#=======================================
#---------------------------------------





# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt


choice = None
while choice != "0":
    print("==========================================================")
    print("==========================================================")
    print("..................ELECTRICITY CALCULATION.................")
    print("==========================================================")
    print("==========================================================")
    print("""






    """)
    print("1 - Calculate Current: ")
    print("2 - Calculate Voltage: ")
    print("3 - Calculate Resistance: ")
    print("4 - Calculate Power: ")
    print("0 - Stop programme: ")
    print("""

    """)
    choice = input("Please make a selection: ")
    print("""


    """)

    if choice == "0":
        print("......THANK YOU FOR USING OUR SOFTWARE......")

    elif choice == "1":
        def current():
            print("===INITIALISING CURRENT CALCULATION===")
            print('')
            while True:
                try:
                    v = float(input("Enter Voltage in Volts: "))
                    break
                except ValueError:
                    print("..... WARNING ..... DATA MUST BE INTEGER, please try again ...")

            while True:
                try:
                    r = float(input("Enter Resistance in Ohms: "))
                    break
                except ValueError:
                    print("..... WARNING ..... DATA MUST BE INTEGER, please try again ...")

            i = v / r
            print('')
            result = "Resulting Current is {} Amperes".format(i)
            print(result)
            return
        current()

    elif choice == "2":
        def voltage():
            print("===INITIALISING VOLTAGE CALCULATION===")
            print('')
            while True:
                try:
                    r = float(input("Enter Resistance in Ohms: "))
                    break
                except ValueError:
                    print("..... WARNING ..... DATA MUST BE INTEGER, please try again ...")

            while True:
                try:
                    i = float(input("Enter Current in Amperes: "))
                    break
                except ValueError:
                    print("..... WARNING ..... DATA MUST BE INTEGER, please try again ...")

            v = r * i
            print('')
            result = "Resulting Voltage is {} Volts".format(v)
            print(result)
            return
        voltage()

    elif choice == "3":
        def resistance():
            print("===INITIALISING RESISTANCE CALCULATION===")
            print('')
            while True:
                try:
                    v = float(input("Enter Voltage in Volts: "))
                    break
                except ValueError:
                    print("..... WARNING ..... DATA MUST BE INTEGER, please try again ...")

            while True:
                try:
                    i = float(input("Enter Current in Amperes: "))
                    break
                except ValueError:
                    print("..... WARNING ..... DATA MUST BE INTEGER, please try again ...")
            r = v / i
            print('')
            result = "Resistance is {} Ohms".format(r)
            print(result)
            return
        resistance()

    elif choice == "4":
        def power():
            print("===INITIALISING POWER CALCULATION===")
            print('')
            while True:
                try:
                    v = float(input("Enter Voltage in Volts: "))
                    break
                except ValueError:
                    print("..... WARNING ..... DATA MUST BE INTEGER, please try again ...")

            while True:
                try:
                    i = float(input("Enter Current in Amperes: "))
                    break
                except ValueError:
                    print("..... WARNING ..... DATA MUST BE INTEGER, please try again ...")

            p = v * i
            kw = p / 1000
            print('')
            result = "Power is {} Watts or {} kW".format(p, kw)
            print(result)
            print("")
            print("")
            
            while True:
                try:
                    h = float(input("Enter hours for the appliance used per day: "))
                    if h <= 24:  # condition for 24 hours in a day
                        break
                except ValueError:
                    print("..... WARNING ..... DATA MUST BE INTEGER, please try again ...")
                    # following lines codes TBC for formula result
            kwh = kw * h
            #joule = 3600000 * kwh
            timeSecond = h * 3600           # E(joule) = P(watt) * t(second)
            joule = p * timeSecond
            print("")
            result1 = "Energy used for {} hours will be {} kWh or {} joules".format(h, kwh, joule)
            print(result1)
            print("")
            print("")

            while True:
                try:
                    rate = float(input("Enter the rate of electricity per kWh: "))
                    break
                except ValueError:
                    print("..... WARNING ..... DATA MUST BE INTEGER, please try again ...")
            cost = rate * kwh
            print("")
            resultcost = "Running cost of the appliance is: {} pounds".format(cost)
            print(resultcost)
            return
        power()

    else:
        print("Try again")
