import prompt
import random


def main():
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}")

    def progression_game():
        print("What number is missing in the progression?")
        i = 0
        while i < 3:
            list_length = random.randint(6, 10)
            num1 = random.randint(0, 100)
            step = random.randint(0, 20)
            arithmetic_progression = []
            for b in range(list_length):
                arithmetic_progression.append(num1)
                num1 = num1 + step
            value = arithmetic_progression.index(random.choice(arithmetic_progression))
            correct_value = arithmetic_progression[value]
            arithmetic_progression[value] = ".."
            print(f'Question: {" ".join(map(str, arithmetic_progression))}')
            answer = prompt.string("Your answer: ")
            if correct_value == int(answer):
                print("Correct!")
                i += 1
            else:
                print(
                    f"{answer} is wrong answer ;( Correct answer was {correct_value}. \nLet's try again, {name}!'"
                )
                break
        if i == 3:
            print(f"Congratulations, {name}!")

    progression_game()


if __name__ == "__main__":
    main()
