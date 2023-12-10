def draw_hangman(guess_counter):
    if guess_counter == 6:
        draw_hangman_step_one()
    elif guess_counter == 5:
        draw_hangman_step_two()
    elif guess_counter == 4:
        draw_hangman_step_three()
    elif guess_counter == 3:
        draw_hangman_step_four()
    elif guess_counter == 2:
        draw_hangman_step_five()
    elif guess_counter == 1:
        draw_hangman_step_six()
    elif guess_counter == 0:
        draw_hangman_step_seven()


def draw_hangman_step_one():
    print("___|___")


def draw_hangman_step_two():
    print(
        "   |/\n"
        "   |\n"
        "   |\n"
        "   |\n"
        "   |\n"
        "___|___")


def draw_hangman_step_three():
    print(
        "   _______\n"
        "   |/ \n"
        "   |\n"
        "   |\n"
        "   |\n"
        "   |\n"
        "___|___")


def draw_hangman_step_four():
    print(
        "   _______\n"
        "   |/    |\n"
        "   |\n"
        "   |\n"
        "   |\n"
        "   |\n"
        "___|___")


def draw_hangman_step_five():
    print(
        "   _______\n"
        "   |/    |\n"
        "   |    (_)\n"
        "   |\n"
        "   |\n"
        "   |\n"
        "___|___")


def draw_hangman_step_six():
    print(
        "   _______\n"
        "   |/    |\n"
        "   |    (_)\n"
        "   |    \|/\n"
        "   |\n"
        "   |\n"
        "___|___")


def draw_hangman_step_seven():
    print(
        "   _______\n"
        "   |/    |\n"
        "   |    (_)\n"
        "   |    \|/\n"
        "   |     |\n"
        "   |    / \\\n"
        "___|___")
