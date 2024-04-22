import json
from person_class import Person
from tabulate import tabulate


class FitnessProgram:

    def __init__(self):
        self.users = []

    @staticmethod
    def load_data_from_db(file_path):
        with open(file_path, "r") as users_file:
            data = json.load(users_file)
            return data

    @staticmethod
    def save_data_to_db(file_path, data):
        with open(file_path, "w") as users_file:
            json.dump(data, users_file, indent=2)
            # info_dict["Password"] = get_password_hash(info_dict["Password"])

    # def display_data_base(self):
    #     """"can be used either tabulate or prettytable library
    #      to display the information about the registered users in out data base"""
    #     data = self.load_data_from_db("user_db.json")
    #     users_info = data.get("users")
    #     print(tabulate(users_info, headers="keys", tablefmt="grid"))

    def register_user(self, name, gender, age, weight, height, exercise_duration, activity_level):
        """In this method we check if the users is already registered,
        if not user is being created, added to the data base and the changes are saved."""

        user_db = self.load_data_from_db("user_db.json")
        try:
            next(filter(lambda u: u.name == name, self.users))
            return f"{name} is already taken."
        except StopIteration:
            new_user = Person(name, gender, age, weight, height, exercise_duration, activity_level)
            self.users.append(new_user)
            user_info = {
                "Name": name,
                "Gender": gender,
                "Age": age,
                "Weight": weight,
                "Height": height,
                "Exercise duration": exercise_duration,
                "Activity level": activity_level,
                "BMI": new_user.bmi,
                "Calories burned": new_user.burned_calories,
                "Calories needed for existing without any activity": new_user.bmr,
                "Calories needed for weight maintenance based on activity level": new_user.amr,
                "Calories on being on a deficit for 0.5kg per week weight loss":
                    self.calculate_needed_calories_for_mild_weight_loss(new_user.amr),
                "Calories on being on a calories surplus for minimal fat(may increase with weight gain)":
                    self.calculate_needed_calories_for_mild_weight_gain(new_user.amr),
            }
            user_db["users"].append(user_info)
            self.save_data_to_db("user_db.json", user_db)
            return f"{name} registered successfully as a new user."

    def filter_overweight_people(self):
        data = self.load_data_from_db("user_db.json")
        users_info = data.get("users")

        filtered_people = filter(lambda p: p["BMI"] >= 25, users_info)
        print(tabulate(filtered_people, headers="keys", tablefmt="grid"))

    def sort_by_bmi_and_calories_burned(self):
        """"can be used either tabulate or prettytable library
                 to display the information about the registered users in out data base"""
        data = self.load_data_from_db("user_db.json")
        users_info = data.get("users")
        sorted_people = sorted(users_info, key=lambda p: (-p["BMI"], -p["Calories burned"]))
        print(tabulate(sorted_people, headers="keys", tablefmt="grid"))

    @staticmethod
    def calculate_needed_calories_for_mild_weight_loss(amr):
        calories = amr - 500
        return calories

    @staticmethod
    def calculate_needed_calories_for_mild_weight_gain(amr):
        calories = amr + 200
        return calories


# def main():
#     while True:
#         command = int(input(f"Enter a random number to continue, enter 1 to quit: "))
#
#         if command == 1:
#             break
#         app = FitnessProgram()
#         name = input("Enter username: ")
#         gender = input(f"Enter gender(male/female): ")
#         age = int(input(f"Enter your age: "))
#         weight = float(input(f"Enter your weight in kg: "))
#         height = int(input(f"Enter your height in cm: "))
#         exercise_duration = int(input(f"Enter exercise duration in minutes: "))
#         activity_level = input(f"Enter your weekly activity level\n"
#                                f"(=> Sedentary (little or no exercise),\n"
#                                f"=> Light activity (exercise 1–3 days/week),\n"
#                                f"=> Moderate (exercise 3–5 days/week),\n"
#                                f"=> Active (exercise 6–7 days/week),\n"
#                                f"=> Very active (hard exercise 6–7 days/week)): ")
#
#         print(app.register_user(name, gender, age, weight, height, exercise_duration, activity_level))
#         # print("Display all users:")
#         # app.display_data_base()
#         print()
#         print("Overweight people:")
#         app.filter_overweight_people()
#         print()
#         print("Display all users sorted users by BMI and Burned calories:")
#         app.sort_by_bmi_and_calories_burned()
#
#
# if __name__ == "__main__":
#     main()
