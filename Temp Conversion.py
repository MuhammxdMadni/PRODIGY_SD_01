def convert_temperature(temp, from_unit):

    """Convert temperature between Celsius, Fahrenheit, and Kelvin"""
    if from_unit.upper() == 'C':
        celsius = temp
    elif from_unit.upper() == 'F':
        celsius = (temp - 32) * 5/9
    elif from_unit.upper() == 'K':
        celsius = temp - 273.15
    else:
        raise ValueError("Unit must be 'C', 'F', or 'K'")
    
    fahrenheit = (celsius * 9/5) + 32
    kelvin = celsius + 273.15
    
    return {
        'celsius': round(celsius, 2),
        'fahrenheit': round(fahrenheit, 2),
        'kelvin': round(kelvin, 2)
    }

def main():

    """Main function to run the temperature converter"""
    print("=== Temperature Converter ===")
    
    try:
        temp = float(input("Enter temperature: "))
        unit = input("Enter unit (C/F/K): ").strip()
        
        result = convert_temperature(temp, unit)
        
        print(f"\nResults for {temp}°{unit.upper()}:")
        print(f"Celsius:    {result['celsius']}°C")
        print(f"Fahrenheit: {result['fahrenheit']}°F")
        print(f"Kelvin:     {result['kelvin']}K")
        
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()
