from program_class import FitnessProgram


def main():
    while True:
        print("Welcome to the fitness app! :)")
        print()
        print("You can choose from the following options:")
        print("1.Register yourself in the app.\n"
              "2.Calculate your calories.\n"
              "3.Workout split.\n"
              "4.Display all users data.\n"
              "5.Exit the app.")
        command = int(input(f"I choose option: "))

        if command == 5:
            print("Goodbye! :)")
            break

        app = FitnessProgram()
        if command == 1:
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

            print()
            print(app.register_user(name, gender, age, weight, height, exercise_duration, activity_level))
            print()
        elif command == 2:
            username = input("Enter your username: ")
            print(app.get_specific_username_info(username))
            print()

        elif command == 3:
            print("Display workout plan")
            print(app.load_workout_plan())
            print()

        elif command == 4:
            print("Display all users sorted users by BMI and Burned calories:")
            print(app.sort_by_bmi_and_calories_burned())
            print()
            print("Overweight people:")
            print(app.filter_overweight_people())
            print()


if __name__ == "__main__":
    main()
