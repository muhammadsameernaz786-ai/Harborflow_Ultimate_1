
# TASK 9 - Compare delivery scenarios

def compare_service_scenarios():
    # Reuse Task 8 validation
    distance = get_valid_positive_float("Distance (km): ")
    weight = get_valid_positive_float("Weight (kg): ")

    # Reuse Task 3 calculation function
    standard_price = calculate_quote(distance, weight, "S")
    express_price = calculate_quote(distance, weight, "X")
    priority_price = calculate_quote(distance, weight, "P")

    print("Service comparison")
    print(f"Standard: {standard_price:.2f} SEK")
    print(f"Express: {express_price:.2f} SEK")
    print(f"Priority: {priority_price:.2f} SEK")

    # Find cheapest service
    cheapest_service = "Standard"
    cheapest_price = standard_price

    if express_price < cheapest_price:
        cheapest_service = "Express"
        cheapest_price = express_price

    if priority_price < cheapest_price:
        cheapest_service = "Priority"

    # Find most expensive service
    most_expensive_service = "Standard"
    most_expensive_price = standard_price

    if express_price > most_expensive_price:
        most_expensive_service = "Express"
        most_expensive_price = express_price

    if priority_price > most_expensive_price:
        most_expensive_service = "Priority"

    print(f"Cheapest service: {cheapest_service}")
    print(f"Most expensive service: {most_expensive_service}")

# TASK 7 - Produce the weekly dispatch report

def produce_weekly_report(deliveries_str, target):
    days = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday"
    ]

    # Convert comma-separated input into integers
    parts = deliveries_str.split(",")
    deliveries = []

    for part in parts:
        deliveries.append(int(part.strip()))

    total_deliveries = 0
    days_meeting_target = 0

    highest_value = deliveries[0]
    highest_day_index = 0

    lowest_value = deliveries[0]
    lowest_day_index = 0

    # Manually process all 7 days
    for i in range(len(deliveries)):
        value = deliveries[i]

        total_deliveries += value

        if value >= target:
            days_meeting_target += 1

        # >= means LAST highest day wins a tie
        if value >= highest_value:
            highest_value = value
            highest_day_index = i

        # <= means LAST lowest day wins a tie
        if value <= lowest_value:
            lowest_value = value
            lowest_day_index = i

    average_per_day = total_deliveries / len(deliveries)

    print("Weekly dispatch report")
    print(f"Total deliveries: {total_deliveries}")
    print(f"Average per day: {average_per_day:.2f}")
    print(
        f"Highest day: "
        f"{days[highest_day_index]} ({highest_value})"
    )
    print(
        f"Lowest day: "
        f"{days[lowest_day_index]} ({lowest_value})"
    )
    print(f"Days meeting target: {days_meeting_target}")


def task_7_function():
    deliveries = get_valid_weekly_deliveries()
    target = get_valid_non_negative_int("Daily target: ")

    produce_weekly_report(deliveries, target)

# TASK 8 - Input validation function

def get_valid_menu_option():
    while True:
        try:
            choice = int(input("Select service: "))

            if 1 <= choice <= 8:
                return choice

            print("Error - Select a service from 1 to 8.")

        except ValueError:
            print("Error - Select a service from 1 to 8.")


def get_valid_positive_float(prompt):
    while True:
        try:
            value = float(input(prompt))

            if value > 0:
                return value

            print("Error - Value must be greater than zero.")

        except ValueError:
            print("Error - Value must be greater than zero.")


def get_valid_service_code():
    while True:
        code = input("Service code: ").strip().upper()

        if code == "S" or code == "X" or code == "P":
            return code

        print("Error - Service code must be S, X or P.")


def get_valid_non_negative_int(prompt):
    while True:
        try:
            value = int(input(prompt))

            if value >= 0:
                return value

            print("Error - Value must be non-negative.")

        except ValueError:
            print("Error - Value must be non-negative.")


def get_valid_weekly_deliveries():
    while True:
        deliveries_str = input("Completed deliveries: ")

        parts = deliveries_str.split(",")

        # Must have exactly 7 values
        if len(parts) != 7:
            print("Error - Weekly report requires 7 delivery counts.")
            continue

        valid = True

        for part in parts:
            try:
                value = int(part.strip())

                if value < 0:
                    valid = False
                    break

            except ValueError:
                valid = False
                break

        if valid:
            return deliveries_str

        print("Error - Weekly report requires 7 delivery counts.")


def get_valid_capacity_weights():
    while True:
        weights_str = input("Parcel weights (kg): ")
        parts = weights_str.split(",")

        valid = True

        for part in parts:
            try:
                weight = float(part.strip())

                if weight <= 0:
                    valid = False
                    break

            except ValueError:
                valid = False
                break

        if valid:
            return weights_str

        print("Error - Value must be greater than zero.")

# Started Task 5 ( Checking Van Capacity )

# Created a function named Check Van Capacity

def check_van_capacity():
    capacity = float(input("What is Van Capacity in KG: "))
    weights = input("Enter parcel weights in KG: ").split(",")

    remaining_capacity = capacity
    accepted_count = 0
    loaded_weight = 0

# Used For Lopp and If-Else statement

    for i in range(len(weights)):
        weight = float(weights[i])

        if weight <= remaining_capacity:
            print(f"Parcel {i + 1}: Accepted")
            accepted_count = accepted_count + 1
            loaded_weight = loaded_weight + weight
            remaining_capacity = remaining_capacity - weight
        else:
            print(f"Parcel {i + 1}: Rejected")

    print(f"Accepted Parcels: {accepted_count}")
    print(f"Loaded Weight: {loaded_weight:.2f} KG")
    print(f"Remaining Capacity: {remaining_capacity:.2f} KG")


# Started Task 6 ( Classify Service Performance )

# Created a function named Classify Performance

def classify_performance(promised, actual, damaged):
    delay = actual - promised

# Using If-Else Statements 

    if damaged > 0:
        status = "SERVICE FAILURE"
    elif delay <= 0:
        status = "ON TIME"
    elif delay <= 15:
        status = "MINOR DELAY"
    else:
        status = "MAJOR DELAY"

    return delay, status

# Created another function named Service Performance 

def service_performance():
    promised = int(input("Promised minutes: "))
    actual = int(input("Actual minutes: "))
    damaged = int(input("Damaged parcels: "))

    delay, status = classify_performance(promised, actual, damaged)

    print(f"Delay: {delay} minutes")
    print(f"Service status: {status}")
#Task 3
def calculate_quote(distance, weight, service_code):
    #Basic components for the quote and subtotal
    base_charge = 45.00
    distance = float(distance)
    weight = float(weight)
    service_code = service_code.upper()
    
    # Conditions for the service code
    if service_code == "S":
        service_multiplier = 1.0
    elif service_code == "X":
        service_multiplier = 1.25
    elif service_code == "P":
        service_multiplier = 1.6
    else:
        print("Invalid service code. Please enter S, X, or P.")
        return None

    # Calculation for subtotal and delivery quote
    subtotal = base_charge + (distance * 6.5) + (weight * 4)
    quote = subtotal * service_multiplier
    return quote

# Printing values for the quote and subtotal
distance = float(input("Distance (km): "))
weight = float(input("Weight (kg): "))
service_code = input("Service code: ")

quote = calculate_quote(distance, weight, service_code)
if quote is not None:
    print(f"Delivery quote: {quote:.2f} SEK")

#Task 4 - Consolidate parcel labels
# list, distinct label once, preserving the order, 
# splitting, loops, normalization, memberships checks, ordered output

scanned_labels = input("Scanned labels: ")
scanned_labels = scanned_labels.split(",")

unique_labels = []

for label in scanned_labels:
    label = label.upper()
    label = label.strip()
    if label not in unique_labels:
        unique_labels.append(label)

print(f"Unique load list:")

for number, label in enumerate(unique_labels, start = 1):
    print(f"{number}. {label}")

print(f"Total unique parcels: {len(unique_labels)}")
# Task1
def task_2_function():
    handle_validate_reference()


def task_3_function():
    # Placeholder for task 3
    print("Running: Calculate delivery quote")


def task_4_function():
    # Placeholder for task 4
    print("Running: Consolidate parcel labels")


def task_5_function():
    # Placeholder for task 5
    print("Running: Check van capacity")


def task_6_function():
    # Placeholder for task 6
    print("Running: Classify service performance")


def task_7_function():
    # Placeholder for task 7
    print("Running: Produce weekly dispatch report")

def task_8_function():
    # Placeholder for task 9
    print("Running: Compare service scenarios")

 # Task2


def validate_reference(reference):
    normalized = reference.strip().upper()

    # Rule 1: must be exactly 12 characters
    if len(normalized) != 12:
        return ""

    # Rule 2: hyphens must be in the right spots
    if normalized[3] != "-" or normalized[7] != "-":
        return ""

    prefix = normalized[0:3]
    customer_code = normalized[4:7]
    shipment_number = normalized[8:12]

    # Rule 3: prefix must be HFL
    if prefix != "HFL":
        return ""

    # Rule 4: customer code must be 3 letters
    if not customer_code.isalpha():
        return ""

    # Rule 5: shipment number must be 4 digits
    if not shipment_number.isdigit():
        return ""

    return normalized


def handle_validate_reference():
    reference = input("Booking reference: ")
    result = validate_reference(reference)

    if result != "":
        print("Valid reference:", result)
    else:
        print("Invalid booking reference.")
