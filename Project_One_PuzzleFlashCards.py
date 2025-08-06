# Puzzle Project 1
import random
# 2.append in file take user input for QA
# 3. take user input for QA
# 4. append this QA in filecmp
# 5.store in numberwise
# 6. only one Question should be dsiplayed on screen at a time
# 7. answer can be entered by user
# 8. check in file if ans is correct
# 9. if yes/no update score
# 10. score can be displayed at the end
# 11. correct ans should be displayed at the end of each question with test as correct/incorrect
# 12. question can be randomly displayed from the file
# 13. updated check user attempt and at the last print attempt too
# 14. Adding question can be accessable for admins only
# 15. check for repetation . using random

# adding new questions to flashcard and stored in dict .This function helps the admin user add new questions to a dictionary (dic_new), which will later be saved to a text file.
# Prompts the user to input a question
# Prompts the user to input the answer for the above question. Uses f-string for cleaner formatting
# Stores the new question-answer pair in the global dictionary dic_new.
# Confirms to the user that, user wants to add more question.

def add_question_functn():
    add_Q = input("Enter Question: ")
    add_A = input("Enter correct Answer for" + f"[{add_Q}] " + "is : ")
    dic_new[add_Q] = add_A
    print("Question added successfully !!!!\n")
    more = input("want to add more??? (Y/N)").lower()
    if more == 'y':
        add_question_functn()
    return dic_new

#newly created dic with new ques now appended to existing dic present in text file
# Takes a dictionary as input and writes it to the text file in append mode.
# Opens the quiz file in append mode.
# Iterates over the dictionary and writes each question-answer pair in the format:
# Question:Answer (one per line).
# Confirms successful file update.
def addNew_Question_txt(dic_new_updated):
    open_file = open("C:\\Users\\Admin\\PycharmProjects\\FlashCardQuiz.txt", 'a')
    for key, value in dic_new_updated.items():
        open_file.write(f"{key}:{value}\n")
    print("Data successfully Updated!!!!!")

#read the data from dict
# This function reads all existing questions and answers from the file and loads them into a dictionary
# Opens the file in read mode and creates an empty dictionary to store the parsed data.
# Loops through each line, splits it at the first :, and adds the pair to the result dictionary.
# strip() removes newline or trailing spaces.
# Returns the complete dictionary.
def toRead_txtDic():
    open_file = open("C:\\Users\\Admin\\PycharmProjects\\FlashCardQuiz.txt", 'r')
    result = {}
    for line in open_file:
        if ':' in line:
            key, value = line.strip().split(':', 1)
            result[key] = value
    return result

# Main logic for the quiz gameplay.
# Counters to track correct and incorrect answers.
# Converts dictionary keys (questions) into a list, shuffles them, and selects the desired number to ask.
# Iterates over each question, takes the user's answer, and also fetches the correct one from the dictionary.
# Compares user’s input with the correct answer (both lowercase + stripped), updates counters, and gives feedback.
# returns final score
def QA_Verify(result,number_questions):
    correct = 0
    incorrect =0
    questions = list(result.keys())
    random.shuffle(questions)
    question_to_ask = questions[:number_questions]
    for question in question_to_ask:
        print("\nQuestion is:",question)
        user_answer = input("Enter answer:")
        correct_answer = result[question].strip().lower()
        if user_answer.strip().lower() == correct_answer:
            correct+=1
            print("Correct Answer!!!\n")
        else:
            incorrect += 1
            print("Incorrect answer !!! Correct answer was:", result[question] + "\n")

    return correct, incorrect



# 1.create textfile
open_file = open("C:\\Users\\Admin\\PycharmProjects\\FlashCardQuiz.txt",'a')
#2. Asks the user whether to play the quiz or add questions.
input_choice= int(input("""\n 1.Play \t 2.Add questions to quiz\n
Enter Your Choice: """))
if input_choice == 2:
    username =input("Username: ").lower()
    password= input("Password: ").lower()                         #made it lower just bcz for my use , to make it easy
    if username == 'admin' and password == 'admin':
        open_file = open("C:\\Users\\Admin\\PycharmProjects\\FlashCardQuiz.txt", 'a')
        dic_new = {}        # new dict for new questions
        userNew_questionDic= add_question_functn()
        print(userNew_questionDic)                          #prints newly added QA dict
        addNew_Question_txt(userNew_questionDic)
        open_file.close()
    else:
        print("Sorry, You dont have access to add questions to Game.")
    # dic_fromTXT.update(Usernew_questionDic)             #if we print this it will print none as dic new will get blank after sending data to dic txt
    # print(dic_fromTXT)                              # bcz dict txt will get updated so we have to print this one only

   #  whatever new updated dic we have , we need to add it to txt file first
   #  then on dic_frmTXT we can apply random and fetch que to user and check
   #  for ans
elif input_choice == 1:
   # print(toRead_txtDic())                   just printed dic to cross verify answers logic is running correct
     print("\n\n-----Lets Start the Game ------")
     result = toRead_txtDic()
     number_questions =4                       #how many questions we want in game , we can set it
     correct_score,incorrect_score= QA_Verify(result,number_questions)
     print("Game Over !!!! Your Game score is: ",correct_score)
     open_file.close()



########################################################################


