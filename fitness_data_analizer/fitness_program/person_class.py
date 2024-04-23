class Person:
    CALORIES_BURNED_PER_MIN = 5
    BMR_CONST_FOR_MEN = 66.47
    BMR_CONST_FOR_WOMAN = 655.1
    ACTIVITY_LEVEL_TYPES = ["Sedentary", "Light activity", "Moderate", "Active", "Very active"]

    def __init__(self, name, gender, age, weight, height, exercise_duration, activity_level):
        self.name = name
        self.gender = gender
        self.age = age
        self.weight = weight
        self.height = height
        self.exercise_duration = exercise_duration
        self.activity_level = activity_level
        self.amr_index = self.determinate_amr_index(self.activity_level)
        self.bmi = self.calculate_bmi(weight, height)
        self.burned_calories = self.calculate_calories_burned(exercise_duration)
        self.bmr = self.calculate_basal_metabolic_rate(weight, height, gender, age)
        self.amr = self.calculate_active_metabolic_rate(self.bmr, self.amr_index)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.strip():
            raise ValueError("Enter valid name.")
        self.__name = value

    @property
    def gender(self):
        return self.__gender

    @gender.setter
    def gender(self, value):
        if value not in ["male", "female"]:
            raise ValueError('The optional picks for gender are "male" and "female"!')
        self.__gender = value

    @property
    def activity_level(self):
        return self.__activity_level

    @activity_level.setter
    def activity_level(self, value):
        """Sedentary (little or no exercise): AMR = BMR x 1.2
        Lightly active (exercise 1–3 days/week): AMR = BMR x 1.375
        Moderately active (exercise 3–5 days/week): AMR = BMR x 1.55
        Active (exercise 6–7 days/week): AMR = BMR x 1.725
        Very active (hard exercise 6–7 days/week): AMR = BMR x 1.9"""
        if value not in self.ACTIVITY_LEVEL_TYPES:
            raise ValueError(f"You must enter a valid activity level status! Allowed status: {', '.join(self.ACTIVITY_LEVEL_TYPES)}.")
        self.__activity_level = value

    def determinate_amr_index(self, activity_level):
        amr_index = 0
        if activity_level == "Sedentary":
            amr_index = 1.2
        elif activity_level == "Light activity":
            amr_index = 1.375
        elif activity_level == "Moderate":
            amr_index = 1.55
        elif activity_level == "Active":
            amr_index = 1.725
        elif activity_level == "Very active":
            amr_index = 1.9
        return amr_index

    def calculate_basal_metabolic_rate(self, weight, height, gender, age):
        """This method calculates the needed calories for the person
        just to exist without any activity.The method takes the person's gender, weight in kg,
         height in cm and age in years. """
        if gender == "male":
            bmr = self.BMR_CONST_FOR_MEN + (13.75 * weight) + (5.003 * height) - (6.755 * age)
            return bmr
        else:
            bmr = self.BMR_CONST_FOR_WOMAN + (9.563 * weight) + (1.850 * height) - (4.676 * age)
            return bmr

    def calculate_active_metabolic_rate(self, bmr, amr_index):
        amr = bmr * amr_index
        return amr

    def calculate_bmi(self, weight_kg, height_meters):
        """Calculate the Body Mass Index (BMI)."""
        bmi_formula = (weight_kg / (height_meters ** 2)) * 10000  # works in centimeters
        return bmi_formula

    def calculate_calories_burned(self, exercise_duration):
        """Calculate the estimated number of calories burned during exercise."""
        total_burned_calories = exercise_duration * self.CALORIES_BURNED_PER_MIN
        return total_burned_calories

    # can add a email checked by a regex
