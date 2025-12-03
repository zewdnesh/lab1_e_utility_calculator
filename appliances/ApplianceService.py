appliances = []

def register_appliance(name, wattage):
    if name and wattage > 0:
        appliances.append({"name": name, "wattage": wattage})
        return True
    return False

def list_appliances():
    return appliances
