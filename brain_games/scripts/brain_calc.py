import prompt
import random


def main():
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}")

    def calc_games():
        expressions = ["+", "-", "*"]
        print("What is the result of the expression?")
        i = 0
        while i < 3:
            random_num1 = random.randint(0, 100)
            random_num2 = random.randint(0, 100)
            operator = random.choice(expressions)
            result = eval(f"{random_num1}{operator}{random_num2}")
            print(f"Question: {random_num1} {operator} {random_num2}")
            answ = prompt.string("Answer: ")
            if result == int(answ):
                print(f"Your answer: {answ}")
                print("Correct!")
                i += 1
            else:
                print(f"{answ} is wrong answer ;( Correct answer was {result}.")
                print(f"Let's try again, {name}!'")
                break
        if i == 3:
            print(f"Congratulations, {name}!")

    calc_games()


if __name__ == "__main__":
    main()
