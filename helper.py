from math import pi as pi

def find_cross_section(radius, thickness):
    """Returns the cross sectional area of a hollow cylinder.

    Args:
        radius (num): Radius of the cylinder
        thickness (num): Thickness of the cylinder

    Returns:
        num: Cross sectional area of the cylinder.
    """
    innerArea = pi*((radius-thickness)**2)
    outerArea = pi*(radius**2)

    return outerArea-innerArea

def find_mmoi(radius, thickness):
    """Returns the area moment of inertia of a thin tube, needed for column buckling.

    Args:
        radius (num): Radius of the cylinder
        thickness (num): Thickness of the cylinder

    Returns:
        num: Area moment of inertia of the cylinder.
    """
    return pi*(radius**3)*thickness