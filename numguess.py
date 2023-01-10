from random import randint
from time import sleep

# Generate answer
answer = randint(1,100)

# Print answer for debugging
print(answer)

# User interaction
username = input("Hi there, What is your name?")
print(f"Hi,{username}! Please be my guest!!")
guess = int(input(f"So {username}, Guess the number(1-100): "))
print(f'Well choice {username}~~ You picked {guess}!!')

# Compare answer with user's guess
if guess==answer:
    print('**************')
    sleep(1)
    print('**************')
    sleep(1)
    print('**************')
    sleep(1)
    print('**************')
    sleep(1)
    print(f'You got it right!! The answer is {answer}!!')
elif guess>answer:
    print(f'Keep going, man~! That was too high, {username}..')
elif guess<answer:
    print(f'keep going, man~! That was too low, {username}..')
else:
    print(f'Wrong answer!! The answer was {answer}, {username}..')


