import random
from drawing_settings import draw_hangman


def main():
    guess_counter = 7
    needed_word = []
    searched_word = random_words()
    for i in searched_word:
        needed_word.append("_")
    word_output(needed_word, guess_counter)
    while True:
        if "_" not in needed_word or guess_counter <= 0:
            win_or_lose(guess_counter)
            break
        user_guess = input("Guess a letter, please: ")
        if user_guess not in searched_word:
            guess_counter -= 1
            draw_hangman(guess_counter)
        for letter in range(len(searched_word)):
            if user_guess == searched_word[letter]:
                needed_word[letter] = user_guess
        word_output(needed_word, guess_counter)


def random_words():
    words_to_choose_from = ["house", "mouse", "server", "request"]
    secret_word = random.choice(words_to_choose_from)
    return secret_word


def word_output(word, counter):
    print("\n********************************")
    print("The word you are searching for:")
    print("".join(word))
    print(f"You can try {counter} more times.")
    print("********************************\n")


def win_or_lose(counter):
    if counter <= 0:
        print("You lose!\n"
              "Better luck next time.")
    else:
        print("You win!\n"
              "Congratulations!")


main()
