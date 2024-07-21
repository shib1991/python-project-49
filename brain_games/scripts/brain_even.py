import prompt
import random


def main():
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}")

    def num_games():
        print('Answer "yes" if the number is even, otherwise answer "no".')
        i = 0
        while i < 3:
            random_num = random.randint(0, 100)
            print(f"Question: {random_num}")
            answer = prompt.string("Answer: ")
            if random_num % 2 == 0:
                if answer == "Yes" or answer == "yes":
                    print(f"Your answer: {answer}")
                    print("Correct!")
                    i += 1
                else:
                    print(
                        f"{answer} is wrong answer ;( Correct answer was 'no'. \nLet's try again, {name}!'"
                    )
                    break
            if random_num % 2 != 0:
                if answer == "No" or answer == "no":
                    print(f"Your answer: {answer}")
                    print("Correct!")
                    i += 1
                else:
                    print(
                        f"{answer} is wrong answer ;( Correct answer was 'no'. \nLet's try again, {name}!'"
                    )
                    break
        if i == 3:
            print(f"Congratulations, {name}!")

    num_games()


if __name__ == "__main__":
    main()
