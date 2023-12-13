from BucklingChecks import euler_buckling, shell_buckling, determine_stress
from Material import MaterialManager, Material
from helper import find_cross_section, find_mmoi

materialCataloguePath = './materials.txt'

# get different starting variables from user
pressure = float(input('Please input the pressure inside of the tank: '))
length = float(input('Please input the length of the tank: '))
radius = float(input('Please input the radius of the tank: '))
thickness = float(input('Please input the thickness of the tank: '))
spaceCraftMass = float(input('Please input the wet mass of the spacecraft: '))
launchAccel = float(input('Please input the launch acceleration of the spacecraft in g: '))

# initialize matereial catalogue
matMan = MaterialManager(materialCataloguePath)

print('**-----------------------------------------------------**')
print('If you would like to enter new materials, enter mat.')
print('If you would like to run the computation, enter run.')

# loop allows user to input materials multiple times, and allows for correction of typos in commands
while True:
    userIn = input('Enter your choice here: ')
    if userIn == 'mat':
        matMan.add_material()
        print('you can now enter another material or run the calculation')
    elif userIn == 'run':
        crossSection = find_cross_section(radius, thickness)
        mmoi = find_mmoi(radius, thickness)
        stress = determine_stress(crossSection, spaceCraftMass, launchAccel)

        print(f"the stress experienced by the tanks is {stress}")

        # run calculation for all materials
        for material in matMan.materials:
            print(f'\nCalculation results for {material.name}')
            
            critEulerBuckling = euler_buckling(material.youngsModulus, mmoi, crossSection, length)
            print(f'The critical column buckling load is {critEulerBuckling}')

            critShellBuckling = shell_buckling(pressure, material.youngsModulus, thickness, 
                radius, material.poissonRatio, length)
            print(f'The critical shell buckling load is {critShellBuckling}')

        break
    else: 
        print('That is not a valid input, try again')

    print('**-----------------------------------------------------**')

# save updated material catalogue to file
matMan.write_catalogue('./materials.txt')