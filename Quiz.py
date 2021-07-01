import requests
import json
import random
import html

score_correct = 0
score_incorrect = 0

url = "https://opentdb.com/api.php?amount=1"
end_game = ""

while end_game != "quit":
    r = requests.get(url)
    if(r.status_code != 200):
        end_game =  input("Sorry, there was a problem retrieving the question. Press enter to try again or type 'quit' to quit the game.")
    else:
        answer_validity = False
        answer_num = 1
        data = json.loads(r.text)
        question = data['results'][0]['question']
        answers = data['results'][0]['incorrect_answers']
        correct_answer = data['results'][0]['correct_answer']
        answers.append(correct_answer)
        random.shuffle(answers)

        print("\n" + html.unescape(question))

        for answer in answers:
            print(chr(64 + answer_num) + ") " + html.unescape(answer))
            answer_num += 1

        while answer_validity == False:
            user_answer = str(input("\nChoose the correct answer: "))
            user_answer = int(ord(user_answer.upper()) - 64)
            if user_answer > len(answers) or user_answer <= 0:
                print("Invalid answer")
            else:
                answer_validity = True

        user_answer = answers[int(user_answer)-1]

        if user_answer == correct_answer:
            print("Congratulations! You answered correctly!")
            score_correct += 1
        else:
            print("Sorry, " + html.unescape(user_answer) + " is incorrect. The correct answer is: " + html.unescape(correct_answer))
            score_incorrect += 1

        end_game = input("\nPress enter to play again or type 'quit' to quit the game.").lower()

print("\n------ Score Board ------")
print("Correct answers: " + str(score_correct))
print("Incorrect answers: " + str(score_incorrect))
print("-------------------------")
print("\nThanks for playing 🌝")