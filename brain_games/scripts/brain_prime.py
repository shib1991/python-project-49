import prompt
import random
import math


def is_prime(number):
    if number <= 1:
        return False
    for element in range(2, int(math.sqrt(number)) + 1):
        if number % element == 0:
            return False
    return True


def main():
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}")

    def prime_game():
        print('Answer "yes" if given number is prime. Otherwise answer "no".')
        correct_answers = 0

        while correct_answers < 3:
            num = random.randint(0, 1000)
            print(f"Question: {num}")
            ans = prompt.string("Your answer: ").lower()

            cor = "yes" if is_prime(num) else "no"

            if ans == cor:
                print("Correct!")
                correct_answers += 1
            else:
                print(f"{ans} is wrong answer ;( Correct answer was '{cor}'.")
                print(f"Let's try again, {name}!")
                break
        else:
            print(f"Congratulations, {name}!")

    prime_game()


if __name__ == "__main__":
    main()
