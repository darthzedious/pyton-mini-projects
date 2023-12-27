import json
from difflib import get_close_matches


def load_data_knowledge(file_path: str) -> dict:
    with open(file_path, 'r') as file:
        data: dict = json.load(file)
    return data


def save_data_knowledge(file_path: str, data: dict):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)


def find_best_match(user_question: str, questions: list[str]) -> str | None:
    matches = list(get_close_matches(user_question, questions, n=1, cutoff=0.6))
    return matches[0] if matches else None


def get_answer_for_question(question: str, knowledge_base: dict) -> str | None:
    for database_question in knowledge_base["questions"]:
        if database_question["question"] == question:
            return database_question["answer"]


def generate_response():
    data_knowledge: dict = load_data_knowledge("data_knowledge.json")

    while True:
        user_input: str = input("User: ")
        if user_input.lower() == "quit":
            break

        best_match: str | None = find_best_match(user_input,
                                                 [database_question["question"] for database_question
                                                  in data_knowledge["questions"]])
        if best_match:
            answer = get_answer_for_question(best_match, data_knowledge)
            print(f"Bot: {answer}")
        else:
            print("This question is too hard for me :(. Please teach me the answer!")
            new_answer = input("Write the right answer ot type next to continue: ")
            if new_answer.lower() != "next":
                data_knowledge["questions"].append({"question": user_input, "answer": new_answer})
                save_data_knowledge('data_knowledge.json', data_knowledge)
                print("I learned something new! Thank you :)")


generate_response()
