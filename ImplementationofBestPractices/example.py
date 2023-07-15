import math

def calculate_circle_area(radius):
    """
    Calculate the area of a circle.

    Args:
        radius (float): The radius of the circle.

    Returns:
        float: The area of the circle.
    """
    if radius <= 0:
        raise ValueError("Radius should be a positive number.")
    
    area = math.pi * radius ** 2
    return area

def main():
    try:
        radius = float(input("Enter the radius of the circle: "))
        area = calculate_circle_area(radius)
        print(f"The area of the circle is: {area:.2f}")
    except ValueError as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()