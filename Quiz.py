import requests
import json
import random
import html

# ANSI color codes
Color_Off="\033[0m"     # Color Reset
IRed="\033[0;91m"       # Intense Red
IGreen="\033[0;92m"     # Intense Green
IBlue="\033[0;94m"      # Intense Blue
IWhite="\033[0;97m"     # Intense White
BIRed="\033[1;91m"      # Bold Intense Red
BIGreen="\033[1;92m"    # Bold Intense Green
BIBlue="\033[1;94m"     # Bold Intense Blue
BIWhite="\033[1;97m"    # Bold Intense White

score_correct = 0
score_incorrect = 0

url = "https://opentdb.com/api.php?amount=1"
end_game = ""

while end_game != "quit":
    request = requests.get(url)
    if(request.status_code != 200):
        end_game =  input(IRed + "Sorry, there was a problem retrieving the question. Press enter to try again or type 'quit' to quit the game." + Color_Off)
    else:
        answer_validity = False
        answer_num = 1
        data = json.loads(request.text)
        question = data['results'][0]['question']
        answers = data['results'][0]['incorrect_answers']
        correct_answer = data['results'][0]['correct_answer']
        answers.append(correct_answer)
        random.shuffle(answers)

        print("\n"+ IWhite + html.unescape(question))
        for answer in answers:
            print(chr(64 + answer_num) + ") " + html.unescape(answer))
            answer_num += 1
        print()

        while answer_validity == False:
            try:
                user_answer = str(input(IWhite + "Select the correct option: " + Color_Off))
                user_answer = int(ord(user_answer.upper()) - 64)
                if user_answer > len(answers) or user_answer <= 0:
                    print(IRed + "Invalid option" + Color_Off)
                else:
                    answer_validity = True
            except:
                print(IRed + "Input can't be empty. Please enter valid input." + Color_Off)

        user_answer = answers[int(user_answer)-1]

        if user_answer == correct_answer:
            print(IGreen + "Congratulations! You answered correctly!" + Color_Off)
            score_correct += 1
        else:
            print(IWhite + "Sorry, "+ IRed + html.unescape(user_answer) + Color_Off + IWhite + " is incorrect. The correct answer is: " + IGreen + html.unescape(correct_answer) + Color_Off)
            score_incorrect += 1

        end_game = input(IWhite + "\nPress enter to play again or type 'quit' to quit the game." + Color_Off).lower()

print(BIWhite +"\n------- Score Board -------")
print(BIGreen +"  Correct answers   : " + str(score_correct))
print(BIRed +"  Incorrect answers : " + str(score_incorrect))
print(BIWhite +"--------------------------- " + Color_Off)

print(BIBlue + "\nThanks for playing 🌝" + Color_Off)
