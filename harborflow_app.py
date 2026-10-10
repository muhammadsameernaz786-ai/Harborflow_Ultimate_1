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
