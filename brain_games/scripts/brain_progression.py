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
            ar_progression = []
            for b in range(list_length):
                ar_progression.append(num1)
                num1 = num1 + step
            value = ar_progression.index(random.choice(ar_progression))
            cor_val = ar_progression[value]
            ar_progression[value] = ".."
            print(f'Question: {" ".join(map(str, ar_progression))}')
            ans = prompt.string("Your answer: ")
            if cor_val == int(ans):
                print("Correct!")
                i += 1
            else:
                print(f"{ans} is wrong answer ;( Correct answer was {cor_val}.")
                print(f"Let's try again, {name}!'")

                break
        if i == 3:
            print(f"Congratulations, {name}!")

    progression_game()


if __name__ == "__main__":
    main()
