customers = []

def register_customer(name):
    if name and name not in customers:
        customers.append(name)
        return True
    return False

def list_customers():
    return customers
