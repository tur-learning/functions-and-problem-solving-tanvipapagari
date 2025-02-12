from problemsolving import BMRCalculator 
from problemsolving import TemperatureConverter 
from problemsolving import TimeConverter

# BMR
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in cm: "))
age = int(input("Enter your age in years: "))

bmr_calculator = BMRCalculator(weight, height, age)
bmr_men = bmr_calculator.calculate_bmr_men()
bmr_women = bmr_calculator.calculate_bmr_women()

print(f"Men's bmr: {bmr_men} calories, Chocolate Bars: {bmr_calculator.chocolate_bars_needed(bmr_men)}")
print(f"Women's bmr: {bmr_women} calories, Chocolate Bars: {bmr_calculator.chocolate_bars_needed(bmr_women)}")

# Temp
celsius = float(input("Enter temperature in Celsius: "))
temp_converter = TemperatureConverter()
fahrenheit = temp_converter.celsius_to_fahrenheit(celsius)
print(f"{celsius}°C is {fahrenheit}°F")

# Time
seconds = int(input("Enter time in seconds: "))
time_converter = TimeConverter()
hours, minutes, remaining_seconds = time_converter.convert_seconds(seconds)
print(f"{seconds} seconds = {hours} hours, {minutes} minutes, {remaining_seconds} seconds")
