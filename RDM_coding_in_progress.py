

'''RDM (RESISTANCE DES MATERIAUX) or (STRENGTH OF MATERIALS/MECHANICS OF MATERIALS)
# TRACTION AND COMPRESSION
# FLEXION
# SHEAR
# TORSION
'''
# CASE STUDY FOR TRACTION
# formula => σ(MPa or N/mm2 = force(N)/section(mm2)

# Re => yield strength(limite elastique)

# Reg => shear stress(resistante elastique au cisaillement ou glissement)
# Reg for soft metal: 		Re <= 250 MPa             			Reg = 0.5 Re
# Reg for half soft meta: 320 MPa <= Re <= 500 MPa				Reg = 0.7 Re
# Reg for hard:						Re >= 600 MPa and cast-iron			Reg = 0.8 Re
# formula => Rpe = Re/s, Re = (yield strength, s = (security factor)
# formula => yield condition = σ maxi <= Rpe for Rpe = Re/s OR σ maxi=N/S<=Rpe
import os
import math
# import matplotlib.pyplot as plt
# import numpy as np

def cls(): #function to clear screen on beginning of new calculation
    os.system('cls')
cls()

def mainMenu():

    print('========================================')
    print('========================================')
    print('\n 1: TRACTION & COMPRESSION')
    print(' 2: SHEAR STRESS')
    print(" 3: FLEXION")
    # add more menu option
    print(' 100: QUIT PROGRAM')
    print('\n=========================================')
    print('=========================================')
  
    while True:
        try:
            choice = int(input('\nEnter choice of calculation: '))
            
            if choice == 1:
                traction_compression()
                break

            elif choice == 2:
                shear()
                break

            elif choice == 3:
                flexion()
                break

            elif choice >= 100:
                break

            else:
                print('\nInvalid choice, enter 1-100')
                break

        except ValueError:
            print('Invalid choice, enter 1-100')
cls()

def traction_compression():
    # sigma = N(newton)/S(mm2)
    print('\n')
    print('='*45)
    print('TRACTION & COMPRESSION CALCULATION INITIATED')
    print('='*45)

    while True:
        try:
            f_comp= float(input('\nEnter compression force in Newton here: '))
            break
        except ValueError:
            print("!!!... Invalid input, it must be a number ...!!!")

    while True:
        try:
            s_comp = float(input('\nEnter material section in mm2 here: '))
            break
        except ValueError:
            print("!!!... Invalid input, it must be a number ...!!!")
    
    sigma = f_comp / s_comp
    print('\nStrain on material is: {0} MPa or N/mm2'.format(sigma))

    while True:
        try:
            re = float(input('\nEnter Re of the designated material in Newton: '))
            break
        except ValueError:
            print("!!!... Invalid input, it must be a number ...!!!")

    while True:
        try:
            coef_secu = float(input('\nEnter security coefficient: '))
            break
        except ValueError:
            print("!!!... Invalid input, it must be a number ...!!!")

# condition of resistance
# sigma=N/S <= rpe = re/coef security
    rpe_max = re / coef_secu

    if sigma <= rpe_max:

        print('\nSTRAIN ACCEPTED, σ ({})MPa <= rpe_max({})MPa'.format(sigma,rpe_max))

    elif sigma > rpe_max:
           print('\nSTRAIN DENIED, σ ({})MPa > rpe_max({})MPa'.format(sigma,rpe_max))
    else:
        pass
    anykey = input('\nType any key to return to menu')
    cls()
    mainMenu()



def shear():
    # Tau = T(newton)/S(mm2)
    f_shear = float(input('\nEnter shear force in Newton here: '))
    s_shear = float(input('\nEnter material section in mm2 here: '))
    tau = f_shear / s_shear
    print('\nStrain on material is: {0} MPa or N/mm2'.format(tau))
    print('''
# Reg => shear stress(resistante elastique au cisaillement ou glissement)
# Reg for soft metal: 		                 Re <= 250 MPa             			  Reg = 0.5 Re
# Reg for half soft meta:       320 MPa <= Re <= 500 MPa				            Reg = 0.7 Re
# Reg for hard metal:				               Re >= 600 MPa and cast-iron			Reg = 0.8 Re
# formula => Rpe = Re/s, Re = (yield strength, s = (security factor))''')
    re_shear = float(input('\nEnter Reg of the designated material in Newton: '))
    coef_secu = float(input('\nEnter security coefficient: '))

# condition of resistance
# Tau = N/S <= rpg = reg/coef security
    rpg = re_shear / coef_secu

    if tau <= rpg:
        print('\nSTRAIN ACCEPTED, τ ({})MPa <= rpg ({})MPa'.format(tau,rpg))

    elif tau > rpg:
        print('\nSTRAIN DENIED, τ ({})MPa > rpg ({})MPa'.format(tau,rpg))

    else:
        pass
    anykey = input('\nType any key to return to menu')
    cls()
    mainMenu()

def flexion():
    print("coding in progress ............")

    anykey = input('\nType any key to return to menu')
    cls()
    mainMenu()
mainMenu()


