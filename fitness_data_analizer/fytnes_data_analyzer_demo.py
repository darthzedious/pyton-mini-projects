def calculate_bmi(weight_kg, height_meters):
    """Calculate the Body Mass Index (BMI)."""
    bmi_formula = weight_kg / (height_meters ** 2)
    return bmi_formula


def calculate_calories_burned(duration):
    """Calculate the estimated number of calories burned during exercise."""
    calories_burned_per_min = 5
    total_burned_calories = duration * calories_burned_per_min
    return total_burned_calories


def filter_overweight_people(people_data):
    """Filter overweight people based on BMI.
    people_data is a list of dictionaries => [{'name': 'John', 'weight': 80, 'height': 1.75}]"""
    #overweight_people = []

    filtered_people_data = filter(lambda p: calculate_bmi(p['weight'], p['height']) >= 25, people_data)

    # for person in people_data:
    #     bmi = calculate_bmi(person['weight'], person['height'])
    #
    #     if bmi >= 25:
    #         overweight_people.append(person)
    return filtered_people_data


def sort_by_bmi_and_calories_burned(people_data):
    sorted_people_data = sorted(people_data, key=lambda p: (-p["BMI"], p['Calories burned']))
    return sorted_people_data


def fitness_analysis(people_data):
    print("\nFitness Analysis:")
    people_data = sort_by_bmi_and_calories_burned(people_data)

    for person in people_data:
        print(f"{person['name']}: BMI = {person['BMI']:.2f}, Calories burned = {person['Calories burned']}")

    overweight_people = filter_overweight_people(people_data)
    overweight_people = sort_by_bmi_and_calories_burned(overweight_people)

    print("\nOverweight People:")
    for person in overweight_people:
        print(f"{person['name']}: BMI = {person['BMI']:.2f}")


people_data = []


# Main program
def main():
    print("Enter fitness data for each person (Enter a blank name to finish):")
    while True:
        name = input("Enter person's name: ").strip()
        if not name:
            break
        weight = float(input("Enter person's weight in kilograms: "))
        height = float(input("Enter person's height in meters(example: 1.75): "))
        duration = float(input("Enter exercise duration in minutes: "))
        bmi = calculate_bmi(weight, height)
        calories_burned = calculate_calories_burned(duration)
        person = {'name': name,
                  'weight': weight,
                  'height': height,
                  'duration': duration,
                  'BMI': bmi,
                  "Calories burned": calories_burned}
        people_data.append(person)

    fitness_analysis(people_data)


if __name__ == "__main__":
    main()
