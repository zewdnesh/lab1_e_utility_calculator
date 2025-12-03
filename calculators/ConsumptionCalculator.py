# calculators/ConsumptionCalculator.py

def calculate_consumption(wattage, hours_per_day, days_per_month):
    kW = wattage / 1000  # Convert wattage to kilowatts
    monthly_kWh = kW * hours_per_day * days_per_month
    return monthly_kWh
