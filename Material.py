import os.path

class Material:
    def __init__(self, name, params):
        self.name = name
        self.youngsModulus = params[0]
        self.poissonRatio = params[1]
        self.density = params[2]

class MaterialManager:
    def __init__(self, path):
        if not os.path.isfile(path):
            with open(path, 'x') as file:
                pass

        self.materials = []
        self.read_file(path)

    def read_file(self, path):
        """Read material catalogue file into internal materials list.

        Args:
            path (string): path of the catalogue text file being read from
        """
        with open(path) as file:
            for row in file:
                if row:
                    rowArray = row.split(';')

                    currentMaterial = Material(rowArray[0], [float(param) for param in rowArray[1:]])

                    self.materials.append(currentMaterial)

    def write_catalogue(self, path):
        """Write current material list to file.

        Args:
            path (string): path of the catalogue text file being written to
        """
        with open(path, 'w') as file:
            for material in self.materials:
                currentLine = ";".join([material.name, 
                    str(material.youngsModulus), 
                    str(material.poissonRatio), 
                    str(material.density)])
                currentLine += '\n'
                file.write(currentLine)
    
    def add_material(self):
        """Allow user to input a material to the internal catalogue.
        """
        name = input('Please enter the name of the material: ')
        youngsModulus = float(input('Please enter the youngs modulus of the material: '))
        poissonRatio = float(input('Please enter the poisson ratio of the material: '))
        density = float(input('Please enter the density of the material: '))

        material = Material(name, [youngsModulus, poissonRatio, density])
        self.materials.append(material)
    
    def count(self):
        return len(self.materials)
