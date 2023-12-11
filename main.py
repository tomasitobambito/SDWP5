from BucklingChecks import euler_buckling, shell_buckling
from Material import MaterialManager, Material

# pressure = float(input('Please input the pressure inside of the tank'))
# length = float(input('Please input the length of the tank'))
# radius = float(input('Please input the radius of the tank'))

manager = MaterialManager('./materials.txt')

for material in manager.materials:
    print(material.youngsModulus, material.name)

test = Material('gold', [5.0, 5.0, 5.0])
manager.materials.append(test)

manager.write_catalouge('./materials.txt')