import prompt
import random


def num_games(player_name):
    print('Answer "yes" if the number is even, otherwise answer "no".')
    correct_answers = 0

    while correct_answers < 3:
        random_num = random.randint(0, 100)
        print(f"Question: {random_num}")
        ans = ans = prompt.string("Answer: ").strip().lower()

        is_even = random_num % 2 == 0
        cor_ans = "yes" if is_even else "no"

        if ans == cor_ans:
            print(f"Your answer: {ans}")
            print("Correct!")
            correct_answers += 1
        else:
            print(f"{ans} is wrong answer ;( Correct answer was '{cor_ans}'.")
            print(f"Let's try again, {player_name}!")
            break

    if correct_answers == 3:
        print(f"Congratulations, {player_name}!")


def main():
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}")

    num_games(name)


if __name__ == "__main__":
    main()
