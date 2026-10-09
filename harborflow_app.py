# Task1
def task_2_function():
    handle_validate_reference()


def task_3_mission():
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