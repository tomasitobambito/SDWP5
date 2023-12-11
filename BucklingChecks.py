from math import pi as pi
from math import exp, sqrt

def euler_buckling(youngsModulus, momentOfInertia, area, length):
    """Calculates critical buckling stress for Euler Column Buckling.

    Args:
        youngsModulus (num): Young's modulus of material in question
        momentOfInertia (num): Area moment of inertia of the tank
        area (num): Cross-sectional area of the tank
        length (num): Length of the tank

    Returns:
        num: critical buckling stress
    """
    return ((pi**2)*youngsModulus*momentOfInertia)/(area*(length**2))

def shell_buckling(pressure, youngsModulus, wallThickness, radius, poissonRatio, length):
    """Calculates critical buckling stress for Shell buckling.

    Args:
         pressure (num): Internal pressure of the tank
        youngsModulus (num): Young's modulus of material in question 
        wallThickness (num): Thickness of the tanks cylindrical wall
        radius (num): Radius of the tank
        poissonRatio (num): Poisson ratio of the material in question
        length (num): Length of the tank

    Returns:
        num: critical buckling stress
    """
    # determine needed variables
    expQ = find_exp(pressure, youngsModulus, wallThickness, radius)
    # temporary
    halfWaveConst = find_halfWaveConst(length, radius, wallThickness, poissonRatio)
    constk = find_k(halfWaveConst, length, radius, wallThickness, poissonRatio)

    # calculate stress
    critStress = (1.983-(0.983*exp(-23.14*expQ)))
    critStress *= constk
    critStress *= ((pi**2)*youngsModulus)/(12*(1-(poissonRatio**2)))
    critStress *= ((wallThickness/length)**2)

    return critStress



def find_exp(pressure, youngsModulus, wallThickness, radius):
    """Finds exponent Q needed for shell buckling.

    Args:
        pressure (num): Internal pressure of the tank
        youngsModulus (num): Young's modulus of material in question 
        wallThickness (num): Thickness of the tanks cylindrical wall
        radius (num): Radius of the tank

    Returns:
        num: the exponent Q needed for shell buckling
    """
    return (pressure/youngsModulus)*((radius/wallThickness)**2)

def find_halfWaveConst(length, radius, wallThickness, poissonRatio):
    """Finds the half wave constant lambda needed for shell buckling.

    Args:
        length (num): Length of the tank
        radius (num): Radius of the tank
        wallThickness (num): Thickness of the tanks cylindrical wall
        poissonRatio (num): Poisson ratio of the material in question

    Returns:
        num: the constant lambda needed for shell buckling.
    """
    k = 12/(pi**4)
    k *= (length**4)/((radius**2)*(wallThickness**2))
    k *= (1-(poissonRatio**2))
    
    return sqrt(k)

def find_k(halfWaveConst, length, radius, wallThickness, poissonRatio):
    """Finds the constant k needed for shell buckling.

    Args:
        halfWaveConst (num): constant lambda, to be optimised   
        length (num): Length of the tank
        radius (num): Radius of the tank
        wallThickness (num): Thickness of the tanks cylindrical wall
        poissonRatio (num): Poisson ratio of the material in question

    Returns:
        num: the constant k needed for shell buckling.
    """

    # math is split into steps to make it easier to follow (and so I don't fuck up typing)
    k = 12/(pi**4)
    k *= (length**4)/((radius**2)*(wallThickness**2))
    k *= (1-(poissonRatio**2))
    k *= 1/halfWaveConst
    k += halfWaveConst

    return k

def determine_stress(area, mass, launchAccel):
    """Determines the stresses experienced by the cylindrical section of the fuel tanks during launch.

    Args:
        area (num): cross-sectional area of the cylinder
        mass (num): wet mass of the spacecraft at take off
        launchAccel (num): acceleration (in g) of the spacecraft at takeoff

    Returns:
        num: stress experienced by the cylindrical section of the fuel tanks during takeoff
    """
    force = mass*launchAccel*9.80665

    return force/area