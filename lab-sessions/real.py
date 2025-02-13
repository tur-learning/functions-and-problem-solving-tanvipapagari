def calculate_bmr(weight, height, age):
    bmr_men = (13.7516 * weight) + (5.0033 * height) - (6.755 * age) + 66.473
    bmr_women = (9.5634 * weight) + (1.8496 * height) - (4.6765 * age) + 655.0955
    
    chocolate_bars_men = bmr_men / 214
    chocolate_bars_women = bmr_women / 214
    
    return bmr_men, bmr_women, chocolate_bars_men, chocolate_bars_women


def convert_celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32


def convert_seconds(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    remaining_seconds = seconds % 60
    
    return hours, minutes, remaining_seconds


# Ask user for input
weight = float(input("Enter your weight (kg): "))
height = float(input("Enter your height (cm): "))
age = int(input("Enter your age: "))

bmr_men, bmr_women, bars_men, bars_women = calculate_bmr(weight, height, age)
print(f"BMR (Men): {bmr_men}, BMR (Women): {bmr_women}")
print(f"Chocolate Bars (Men): {bars_men}, Chocolate Bars (Women): {bars_women}")

temp_celsius = float(input("Enter temperature in Celsius: "))
print(f"{temp_celsius}°C in Fahrenheit: {convert_celsius_to_fahrenheit(temp_celsius)}°F")

total_seconds = int(input("Enter time in seconds: "))
hours, minutes, seconds = convert_seconds(total_seconds)
print(f"{total_seconds} seconds -> {hours} hours, {minutes} minutes, {seconds} seconds")

