from program_class import FitnessProgram


def main():
    while True:
        command = int(input(f"Enter a random number to continue, enter 1 to quit: "))

        if command == 1:
            break
        app = FitnessProgram()
        name = input("Enter username: ")
        gender = input(f"Enter gender(male/female): ")
        age = int(input(f"Enter your age: "))
        weight = float(input(f"Enter your weight in kg: "))
        height = int(input(f"Enter your height in cm: "))
        exercise_duration = int(input(f"Enter exercise duration in minutes: "))
        activity_level = input(f"Enter your weekly activity level\n"
                               f"=> Sedentary (little or no exercise),\n"
                               f"=> Light activity (exercise 1–3 days/week),\n"
                               f"=> Moderate (exercise 3–5 days/week),\n"
                               f"=> Active (exercise 6–7 days/week),\n"
                               f"=> Very active (hard exercise 6–7 days/week): ")

        print(app.register_user(name, gender, age, weight, height, exercise_duration, activity_level))
        # print("Display all users:")
        # app.display_data_base()
        print()
        print("Overweight people:")
        app.filter_overweight_people()
        print()
        print("Display all users sorted users by BMI and Burned calories:")
        app.sort_by_bmi_and_calories_burned()


if __name__ == "__main__":
    main()
