def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def celsius_to_kelvin(c):
    return c + 273.15

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def fahrenheit_to_kelvin(f):
    return fahrenheit_to_celsius(f) + 273.15

def kelvin_to_celsius(k):
    return k - 273.15

def kelvin_to_fahrenheit(k):
    return celsius_to_fahrenheit(kelvin_to_celsius(k))

def convert_temperature(temp, unit):
    unit = unit.strip().upper()
    
    if unit == 'C':
        f = celsius_to_fahrenheit(temp)
        k = celsius_to_kelvin(temp)
        print(f"\n--- Conversion Results ---")
        print(f"Celsius:    {temp:.2f} °C")
        print(f"Fahrenheit: {f:.2f} °F")
        print(f"Kelvin:     {k:.2f} K")

    elif unit == 'F':
        c = fahrenheit_to_celsius(temp)
        k = fahrenheit_to_kelvin(temp)
        print(f"\n--- Conversion Results ---")
        print(f"Fahrenheit: {temp:.2f} °F")
        print(f"Celsius:    {c:.2f} °C")
        print(f"Kelvin:     {k:.2f} K")

    elif unit == 'K':
        if temp < 0:
            print("Error: Kelvin cannot be negative.")
            return
        c = kelvin_to_celsius(temp)
        f = kelvin_to_fahrenheit(temp)
        print(f"\n--- Conversion Results ---")
        print(f"Kelvin:     {temp:.2f} K")
        print(f"Celsius:    {c:.2f} °C")
        print(f"Fahrenheit: {f:.2f} °F")

    else:
        print("Invalid unit! Please enter C, F, or K.")

def main():
    print("=" * 35)
    print("   Temperature Conversion Program")
    print("=" * 35)
    
    while True:
        print("\nOptions:")
        print("  C - Celsius")
        print("  F - Fahrenheit")
        print("  K - Kelvin")
        print("  Q - Quit")
        
        unit = input("\nEnter the unit of your temperature: ").strip().upper()
        
        if unit == 'Q':
            print("Exiting program. Goodbye!")
            break
        
        if unit not in ['C', 'F', 'K']:
            print("Invalid choice. Please enter C, F, K, or Q.")
            continue
        
        try:
            temp = float(input("Enter temperature value: "))
        except ValueError:
            print("Invalid input! Please enter a numeric value.")
            continue
        
        convert_temperature(temp, unit)
        
        again = input("\nConvert another? (Y/N): ").strip().upper()
        if again != 'Y':
            print("Exiting program. Goodbye!")
            break

if __name__ == "__main__":
    main()