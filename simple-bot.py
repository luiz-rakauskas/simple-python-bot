def greet(bot_name, birth_year):
    print('Hello! My name is ' + bot_name + '.')
    print('I was created in ' + birth_year + '.')


def remind_name():
    print('Please, remind me your name.')
    name = input()
    print('What a great name you have, ' + name + '!')


def guess_age():
    print('Let me guess your age.')
    print('Enter remainders of dividing your age by 3, 5 and 7.')

    rem3 = int(input())
    rem5 = int(input())
    rem7 = int(input())
    age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105

    print("Your age is " + str(age) + "; that's a good time to start programming!")


def count():
    print('Now I will prove to you that I can count to any number you want.\nType a number!')

    num = int(input())
    curr = 0
    while curr <= num:
        print(curr, '!')
        curr = curr + 1

def end():
    print('Have a nice day!')
    
def quiz():
    print("I have a question for you. What is the most abundant element on Earth?")
    print("1. CO2")
    print("2. O2")
    print("3. Fluor")
    print("4. H2O")
    answer = (int(input("Enter the correct number: ")))
    answer_problem = 2
    while answer != answer_problem:
        answer = int(input("Try again! "))
        if answer == answer_problem:
            print("Correct!")
   
greet('Bob', '2021')
remind_name()
guess_age()
count()
quiz()
end()
