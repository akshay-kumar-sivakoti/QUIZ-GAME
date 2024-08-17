#-------------
def new_game():
    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in question:
        print("--------------------------------")
        print(key)
        for i in options[question_num - 1]:
            print(i)
            
            guess = input("Enter (A,B,C,D):")
            guess = guess.upper()
            guesses.append(guess)

            correct_guesses += check_answer (question.get(key), guess)
            question_num += 1
            display_score (correct_guesses,guesses)
#--------------------------------

def check_answer(answer, guess):
    if guess == answer:
        print("Correct!")
        return 1
    else:
        print("Wrong!")
        print("Correct answer is:", answer)
        return 0
#-------------
def display_score(correct_guesses, guesses):
    print("--------------------------------")
    print("RESULTS")
    print("--------------------------------")

    print("Answers: ",end="")
    for i in question:
        print(question.get(i), end=" ")
        print()

        print("Guesses: ",end="")
    for i in guesses:
        print(i, end=" ")
        print()
        score = int((correct_guesses/len(question))*100)
        print("Your score: "+str(score)+"%")
    
    
#-------------
def play_again():
    response = input("Do you want to play again? (y/n): ")
    response = response.upper()

    if response == "Y":
        return True
        
    else:
        print("Goodbye!")
#-------------
question = {
    "Who created Python?": "A",
    "What Year was Python created?":"B",
    "Who is the current President of USA?":"C",
    "What is the capital of France?":"D",
}

options =     [["A. Guido van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Mark Zuckerburg"],
    ["A. 1989", "B. 1991", "C. 1994", "D. 1995"],
    ["A. George W. Bush", "B. Bill Clinton", "C. Donald Trump", "D. Joe Biden"],
    ["A. Paris", "B. Marseille", "C. Lisbon", "D. Berlin"]]


new_game()

while play_again():
    new_game()

    print("Byee!")
