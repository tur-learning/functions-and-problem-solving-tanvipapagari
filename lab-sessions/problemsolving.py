class BMRCalculator:
    def __init__(self, weight, height, age):
        self.weight = weight
        self.height = height
        self.age = age
    
    def calculate_bmr_men(self):
        return (13.7516 * self.weight) + (5.0033 * self.height) - (6.755 * self.age) + 66.473
    
    def calculate_bmr_women(self):
        return (9.5634 * self.weight) + (1.8496 * self.height) - (4.6765 * self.age) + 655.0955
    
    def chocolate_bars_needed(self, bmr):
        return bmr / 214

class TemperatureConverter:
    def celsius_to_fahrenheit(self, celsius):
        return (celsius * 9/5) + 32

class TimeConverter:
    def convert_seconds(self, seconds):
        hours = seconds // 3600
        minutes = (seconds % 3600) // 60
        remaining_seconds = seconds % 60
        return hours, minutes, remaining_seconds