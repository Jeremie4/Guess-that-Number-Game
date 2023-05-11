import random

ran_num = 12 #random.randint(1,10)
num_of_guesses = 0


try:
    with open('C:/Users/azzrrhk/Desktop/Python/Guess-that-Number-Game/high_scores.txt', 'r') as f:
        high_scores_list = [line.strip() for line in f]
    
    high_scores_list.remove("")
    high_scores = high_scores_list

except:
    high_scores = "Couldn't get high scores."
    high_scores_list = []


user_num = int(input("Welcome to the Guessing Game\nHigh scores: " + str(high_scores) + "\nThe Computer has picked a number from 1 - 100. Try to match it.\nWhat number do you choose (1-100): "))

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
    if high_scores_list == []:
        high_scores_list.append(num_of_guesses)
    
    else:
        for item in high_scores_list:
            if num_of_guesses < item:
                high_scores_list.append(num_of_guesses)

    high_scores_list.sort()

except:
    pass
    #high_scores_list.append(num_of_guesses)

try:
    file = open("C:/Users/azzrrhk/Desktop/Python/Guess-that-Number-Game/high_scores.txt", "w")
    file.close()
except:
    pass


file = open("C:/Users/azzrrhk/Desktop/Python/Guess-that-Number-Game/high_scores.txt", "a")

#high_scores_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

for item in high_scores_list[:10]:
    file.write("\n" + str(item))

file.close()

print(high_scores_list)