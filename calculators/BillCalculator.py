# calculators/BillCalculator.py

def calculate_bill(consumption):
    # Ethiopian Electric Utility tiered pricing
    if consumption <= 50:
        rate = 0.5
    elif consumption <= 100:
        rate = 1.0
    else:
        rate = 1.5

    return consumption * rate

def save_bill_to_file(customer_name, total_bill):
    with open(f"{customer_name}_bill.txt", "w") as file:
        file.write(f"Customer: {customer_name}\n")
        file.write(f"Total Bill: {total_bill:.2f} ETB\n")
