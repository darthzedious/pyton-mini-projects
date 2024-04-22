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
        print()
        result = tabulate(filtered_people, headers="keys", tablefmt="heavy_grid")
        return result
        # grid and heavy_outline are also a okay options

    def sort_by_bmi_and_calories_burned(self):
        """"can be used either tabulate or prettytable library
                 to display the information about the registered users in out data base"""
        data = self.load_data_from_db("user_db.json")
        users_info = data.get("users")
        sorted_people = sorted(users_info, key=lambda p: (-p["BMI"], -p["Calories burned"]))
        print()
        result = tabulate(sorted_people, headers="keys", tablefmt="heavy_grid")
        return result
        # grid and heavy_outline are also a okay options

    def load_workout_plan(self):
        """This method takes the information about the work out plan from the db and displays it in table format"""
        data = self.load_data_from_db("user_db.json")
        workout_plan_data = data.get("workout plan")

    # Initialize an empty dictionary to store all workout plans
        all_workout_plans = {}

        # Loop through each key in the workout plan data and add it to the new dictionary
        for key, value in workout_plan_data[0].items():
            all_workout_plans[key] = value

        workout_plan_as_table = tabulate(all_workout_plans, headers="keys", tablefmt="heavy_grid")
        return workout_plan_as_table

    @staticmethod
    def calculate_needed_calories_for_mild_weight_loss(amr):
        calories = amr - 500
        return calories

    @staticmethod
    def calculate_needed_calories_for_mild_weight_gain(amr):
        calories = amr + 200
        return calories

    def get_specific_username_info(self, username):
        data = self.load_data_from_db("user_db.json")
        users = data.get("users")

        for user in users:
            if user["Name"] == username:
                user_data = [[key, value] for key, value in user.items()]
                return tabulate(user_data, headers=["Category", "User"], tablefmt="heavy_grid")
        return f"{username} not found. Please try again."
