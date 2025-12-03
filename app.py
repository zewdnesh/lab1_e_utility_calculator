from customers.CustomerService import register_customer, list_customers
from appliances.ApplianceService import register_appliance, list_appliances
from calculators.ConsumptionCalculator import calculate_consumption
from calculators.BillCalculator import calculate_bill, save_bill_to_file


def main():
    while True:
        print("\nElectricity Consumption and Bill Calculator")
        print("1. Register Customer")
        print("2. List Customers")
        print("3. Register Appliance")
        print("4. List Appliances")
        print("5. Calculate Consumption and Bill")
        print("6. Exit")

        choice = input("Select an option: ")

        if choice == '1':
            name = input("Enter customer name: ")
            if register_customer(name):
                print(f"Customer '{name}' registered.")
            else:
                print("Invalid customer name or already exists.")

        elif choice == '2':
            print("Registered Customers:", list_customers())

        elif choice == '3':
            name = input("Enter appliance name: ")
            try:
                wattage = float(input("Enter appliance wattage (in watts): "))
                if register_appliance(name, wattage):
                    print(f"Appliance '{name}' registered.")
                else:
                    print("Invalid appliance name or wattage.")
            except ValueError:
                print("Please enter a valid number for wattage.")

        elif choice == '4':
            print("Registered Appliances:", list_appliances())

        elif choice == '5':
            if not list_customers() or not list_appliances():
                print("Please register at least one customer and one appliance first.")
                continue

            customer_name = input("Enter customer name for billing: ")

            if customer_name not in list_customers():
                print("Customer not found!")
                continue

            total_consumption = 0
            days_per_month = 30

            for appliance in list_appliances():
                try:
                    hours = float(input(f"Enter hours per day for {appliance['name']}: "))
                    consumption = calculate_consumption(appliance['wattage'], hours, days_per_month)
                    total_consumption += consumption
                    print(f"{appliance['name']} consumes {consumption:.2f} kWh/month.")
                except ValueError:
                    print("Invalid number for hours.")

            total_bill = calculate_bill(total_consumption)

            print(f"\nTotal Consumption: {total_consumption:.2f} kWh")
            print(f"Total Bill: {total_bill:.2f} ETB")

            save_option = input("Do you want to save the bill to a file? (yes/no): ").strip().lower()
            if save_option == 'yes':
                save_bill_to_file(customer_name, total_bill)
                print(f"Bill saved to {customer_name}_bill.txt")

        elif choice == '6':
            print("Exiting the program.")
            break

        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
