from datetime import datetime
import matplotlib.pyplot as plt

readings = []
dates = []

try:
    with open("readings.csv", "r") as file:
        for line in file:
            date, unit = line.strip().split(",")

            dates.append(date)
            readings.append(float(unit))
except FileNotFoundError:
    pass

print("=" * 45)
print("Welcome to Smart Energy Meter Dashboard")
print("=" * 45)

while True:
    print("\n" + "=" * 45)
    print("      SMART ENERGY METER DASHBOARD")
    print("=" * 45)
    print("1. Add Today's Reading")
    print("2. View All Readings")
    print("3. Calculate Total Bill")
    print("4. Delete Reading")
    print("5. Edit Reading")
    print("6. Search Reading by Date")
    print("7. Generate Bill Report")
    print("8. Show Consumption Graph")
    print("9. Exit")
    print("=" * 45)

    choice = input("Enter your choice: ")

    if choice == "1":
        try:
            units = float(input("Enter today's electricity consumption (kWh): "))
        except ValueError:
            print("Please enter numbers only!")
            continue
        today = datetime.now().strftime("%d-%m-%Y")
        dates.append(today)
        readings.append(units)

        with open("readings.csv", "a") as file:
            file.write(today + "," + str(units) + "\n")

        print("Units entered:", units)

        print("✅ Reading added successfully!")

        if units > 25:
            print("Warning: High electricity consumption detected!")
    
    elif choice == "2":
        if len(readings) == 0:
            print("No readings found.")
        else:
            print("Dates:", dates)
            print("Number of dates:", len(dates))
            print("Readings:", readings)
            print("Number of readings:", len(readings))
            print("All Readings:")
            
            for i in range(len(readings)):
                print(i + 1, ".", dates[i], "-", readings[i], "kWh")    

    elif choice == "3":
        if len(readings) == 0:
            print("No readings available.")
        else:
            total = sum(readings)
            bill = total * 8.5
            highest = max(readings)
            lowest = min(readings)
            average = total / len(readings)

            if average < 15:
                level = "Low 🟢"
            elif average <= 25:
                level = "Moderate 🟡"
            else:
                level = "High 🔴"

            print("Total Consumption:", total, "kWh")
            print("Total Bill: ₹", bill)
            print("Highest Reading:", highest, "kWh")
            print("Lowest Reading:", lowest, "kWh")
            print("Average Reading:", round(average, 2), "kWh")
            print("Consumption Level:", level)

    elif choice == "4":
        if len(readings) == 0:
            print("No readings to delete.")
        else:
            print("Available Readings:")
            for i in range(len(readings)):
                print(i + 1, ".", dates[i], "-", readings[i], "kWh")

            delete = int(input("Enter reading number to delete: ")) - 1

            if 0 <= delete < len(readings):
                dates.pop(delete)
                readings.pop(delete)

                with open("readings.csv", "w") as file:
                    for i in range(len(readings)):
                        file.write(dates[i] + "," + str(readings[i]) + "\n")

                print("🗑 Reading deleted successfully!")
            
            else:
                print("Invalid reading number.")

    elif choice == "5":
        if len(readings) == 0:
            print("No readings available to edit.")
        else:
            print("Available Readings:")
            for i in range(len(readings)):
                print(i + 1, ".", dates[i], "-", readings[i], "kWh")

            edit = int(input("Enter reading number to edit: ")) - 1

            if 0 <= edit < len(readings):
                new_value = float(input("Enter new reading value (kWh): "))
                readings[edit] = new_value

                with open("readings.csv", "w") as file:
                    
                    for i in range(len(readings)):
                        file.write(dates[i] + "," + str(readings[i]) + "\n")

                print("✏ Reading updated successfully!")
            else:
                print("Invalid reading number.")
    
    elif choice == "6":
        if len(readings) == 0:
            print("No readings available.")
        else:
            search_date = input("Enter date (dd-mm-yyyy): ")

            found = False

            for i in range(len(dates)):
                if dates[i] == search_date:
                    print(search_date, "-", readings[i], "kWh")
                    found = True

            if not found:
                print("No reading found for this date.")
    
    elif choice == "7":
        if len(readings) == 0:
            print("No readings available.")
        else:
            total = sum(readings)
            bill = total * 8.5
            highest = max(readings)
            lowest = min(readings)
            average = total / len(readings)

            if average < 15:
                level = "Low"
            elif average <= 25:
                level = "Moderate"
            else:
                level = "High"

            with open("report.txt", "w", encoding="utf-8") as file:
                file.write("SMART ENERGY METER REPORT\n")
                file.write("=========================\n\n")
                file.write(f"Total Consumption : {total} kWh\n")
                file.write(f"Total Bill        : Rs. {bill}\n")
                file.write(f"Highest Reading   : {highest} kWh\n")
                file.write(f"Lowest Reading    : {lowest} kWh\n")
                file.write(f"Average Reading   : {round(average,2)} kWh\n")
                file.write(f"Consumption Level : {level}\n")

            print("📄 Report generated successfully!")
    
    elif choice == "8":
        if len(readings) == 0:
            print("No readings available to plot.")
        else:
            plt.figure(figsize=(8,5))
            plt.plot(dates, readings, marker="o")
            plt.title("Smart Energy Meter Dashboard")
            plt.xlabel("Date")
            plt.ylabel("Units (kWh)")
            plt.grid(True)
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.grid(True)
            plt.tight_layout()
            plt.show()
    
    elif choice == "9":
        print("Thank you!")
        break

    else:
        print("Invalid choice!")