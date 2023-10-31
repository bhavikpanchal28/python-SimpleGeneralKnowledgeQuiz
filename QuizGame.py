def newgame():
    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("-----------------------")
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input("Enter (A, B, C or D): ")
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key),guess)
        question_num +=1

    display_score(correct_guesses, guesses)


def check_answer(answer, guess):

    if answer == guess:
        print("CORRECT!")
        return 1
    else:
        print("Wrong :(")
        return 0

def display_score(correct_guesses, guesses):

    print("-------------------")
    print("Results")
    print("-------------------")

    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("Guesses: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()

    score = int((correct_guesses/len(questions))*100)
    print("Your score is: "+str(score)+"%")

def play_again():

     response = input("Do you want to play again? (yes or no): ")
     response = response.upper()

     if response == "YES":
        return True
     else:
        return False

questions = {
    "Best Superhero?: ": "A",            #Captain America
    "Who is the soccer GOAT?: ": "B",        #Messi
    "Who is the basketball GOAT?: ": "C",
    "Greatest QB of all time?: ": "D"
}

options = [["A. Captain America","B. Iron-Man","C. Superman","D. Batman"],
           ["A. Pele","B. Messi","C. Ronaldo","D. Maradona"],
           ["A. MJ","B. Kareem","C. Lebron","D. Magic"],
           ["A. Brady","B. Montana","C. Mahomes","D. Manning"]]

newgame()

while play_again():
    newgame()

print("Byeeee!")
