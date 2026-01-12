def calculate_usage_score(number_of_vehicles, hours_per_day):
    return number_of_vehicles * hours_per_day


def get_utilization_status(usage_score):
    if usage_score >= 90:
        return "Over-Utilized Parking Area"
    elif 50 <= usage_score <= 89:
        return "Optimally Utilized Parking Area"
    else:
        return "Under-Utilized Parking Area"


def parking_utilization():
    # Predefined values
    parking_area_name = "Central Parking"
    vehicle_type = "Car"
    number_of_vehicles = 10
    hours_per_day = 6

    usage_score = calculate_usage_score(number_of_vehicles, hours_per_day)
    status = get_utilization_status(usage_score)

    print("The program displays a detailed summary of parking resource utilization.")
    print(f"It shows that the parking area name is {parking_area_name} and the vehicle type is {vehicle_type}.")
    print(f"The number of vehicles using the parking is {number_of_vehicles}, and the parking hours per day are {hours_per_day}.")
    print(f"Based on these values, the system calculates the usage score as {usage_score}.")
    print(f"Since the usage score falls between 50 and 89, the parking area is classified as an")
    print(f"{status}.")


if __name__ == "__main__":
    parking_utilization()

