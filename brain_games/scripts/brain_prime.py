import random, prompt, math

def is_prime(number):
    if number <= 1:
        return False
    number_sqrt = int(math.sqrt(number)) 
    divisors = range(2, (number_sqrt + 1))
    for element in divisors:
        if number % element == 0:
            return False
    return True

def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
    def prime_game():
        print('Answer "yes" if given number is prime. Otherwise answer "no".')
        i=0
        while i < 3:
            num=random.randint(0,1000)
            print(f'Question:{num}')
            answer = prompt.string('Your answer: ')
            if is_prime(num) == True:
                if answer == 'Yes' or answer == 'yes':
                    print('Correct!')
                    i +=1
                else:
                    print (f"{answer} is wrong answer ;( Correct answer was 'Yes'. \nLet's try again, {name}!'")
                    break
            if is_prime(num) == False:
                if answer == 'No' or answer == 'no': 
                    print('Correct!')
                    i +=1
                else:
                    print (f"{answer} is wrong answer ;( Correct answer was 'no'. \nLet's try again, {name}!'")
                    break
        if i==3:
            print (f'Congratulations, {name}!')
    prime_game()



if __name__ == '__main__':
    main()