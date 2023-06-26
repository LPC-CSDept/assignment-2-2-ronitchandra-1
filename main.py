def main():

    celsius = int(input("Enter the temperature in Celcius: "))
    fahrenheit = (celsius * 9 / 5) + 32
    print(f"Fahrenheit: {fahrenheit:.2f}°")

    return celsius, fahrenheit


if __name__ == '__main__':
    main()
