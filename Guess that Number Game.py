import random

try:
    file = open("C:/Users/azzrrhk/Desktop/Python/Guess-that-Number-Game/high_scores.txt", "r")
    high_scores = file.read()
    file.close()
    print("current high scores: \n" + high_scores)

except:
    print("Couldn't get high scores.")


ran_num = 12 #random.randint(1,10)
num_of_guesses = 0
user_num = int(input("Welcome to the Guessing Game\nThe Computer has picked a number from 1 - 100. Try to match it.\nWhat number do you choose (1-100): "))
high_scores_list = []


while True:

    num_of_guesses += 1

    if user_num == ran_num:
        print("correct!    Number of guesses: " + str(num_of_guesses))
        break
    elif user_num > ran_num:
        msg = "Too high!"
    elif user_num < ran_num:
        msg = "Too low!"

    print(msg)
    user_num = int(input("Try again: "))


try:
    file = open("C:/Users/azzrrhk/Desktop/Python/Guess-that-Number-Game/high_scores.txt", "r")
    high_scores_list.append(int(file.read()))
    high_scores_list.sort()
    file.close()

except:
    pass


try:
    if num_of_guesses < int(high_scores_list[:10]):
        high_scores_list.append(num_of_guesses)
        high_scores_list.sort()

except:
    high_scores_list.append(num_of_guesses)
    high_scores_list.sort()

file = open("C:/Users/azzrrhk/Desktop/Python/Guess-that-Number-Game/high_scores.txt", "w")
file.close()
file = open("C:/Users/azzrrhk/Desktop/Python/Guess-that-Number-Game/high_scores.txt", "a")

for item in high_scores_list[:10]:
    file.write("\n" + str(item))

file.close()

print(high_scores_list)