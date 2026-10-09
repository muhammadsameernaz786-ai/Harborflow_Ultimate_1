
# TASK 7: Produce the weekly dispatch report

def produce_weekly_report(deliveries_str, target):
    """
    Processes 7 daily delivery counts and a target value.
    For ties, the LAST day with the highest/lowest value is reported.
    """

    days = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday"
    ]

    # Convert comma-separated string into integers
    parts = deliveries_str.split(",")
    deliveries = []

    for part in parts:
        deliveries.append(int(part.strip()))

    total_deliveries = 0
    days_meeting_target = 0

    highest_val = deliveries[0]
    highest_day_idx = 0

    lowest_val = deliveries[0]
    lowest_day_idx = 0

    for i in range(len(deliveries)):
        value = deliveries[i]

        total_deliveries += value

        if value >= target:
            days_meeting_target += 1

        # >= keeps the LAST occurrence when there is a tie
        if value >= highest_val:
            highest_val = value
            highest_day_idx = i

        # <= keeps the LAST occurrence when there is a tie
        if value <= lowest_val:
            lowest_val = value
            lowest_day_idx = i

    average_per_day = total_deliveries / len(deliveries)

    print("\nWeekly dispatch report")
    print(f"Total deliveries: {total_deliveries}")
    print(f"Average per day: {average_per_day:.2f}")
    print(f"Highest day: {days[highest_day_idx]} ({highest_val})")
    print(f"Lowest day: {days[lowest_day_idx]} ({lowest_val})")
    print(f"Days meeting target: {days_meeting_target}")


# TASK 8: Input Validation Functions

def get_valid_menu_option(max_option=8):
    """Validates main menu selections."""

    while True:
        try:
            choice = int(input("Select service: "))

            if 1 <= choice <= max_option:
                return choice

            print(f"Error: Select a service from 1 to {max_option}.")

        except ValueError:
            print(f"Error: Select a service from 1 to {max_option}.")


def get_valid_positive_float(prompt):
    """Validates numeric values that must be greater than 0."""

    while True:
        try:
            value = float(input(prompt))

            if value > 0:
                return value

            print("Error: Value must be greater than zero.")

        except ValueError:
            print("Error: Value must be greater than zero.")


def get_valid_service_code():
    """Validates service codes S, X, or P."""

    while True:
        code = input("Service code: ").strip().upper()

        if code in ["S", "X", "P"]:
            return code

        print("Error: Service code must be S, X or P.")


def get_valid_non_negative_int(prompt):
    """Validates integers that must be 0 or greater."""

    while True:
        try:
            value = int(input(prompt))

            if value >= 0:
                return value

            print("Error: Value must be non-negative.")

        except ValueError:
            print("Error: Value must be non-negative.")


def get_valid_weekly_deliveries():
    """Validates exactly 7 non-negative delivery counts."""

    while True:
        raw_input = input(
            "Completed deliveries "
            "(Monday to Sunday, separated by commas): "
        )

        parts = raw_input.split(",")

        if len(parts) != 7:
            print("Error: Weekly report requires 7 delivery counts.")
            continue

        valid = True

        for part in parts:
            part = part.strip()

            try:
                value = int(part)

                if value < 0:
                    valid = False
                    break

            except ValueError:
                valid = False
                break

        if valid:
            return raw_input

        print("Error: Weekly report requires 7 non-negative integers.")


def get_valid_capacity_weights():
    """Validates parcel weights. All weights must be greater than 0."""

    while True:
        raw_input = input("Parcel weights (kg): ")
        parts = raw_input.split(",")

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
            return raw_input

        print("Error: All parcel weights must be greater than zero.")


