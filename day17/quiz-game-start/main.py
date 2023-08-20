from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

Question_Bank=[]
for question in question_data:
    question_Text=question["text"]
    question_answer=question["answer"]
    newQuestion=Question(question_Text,question_answer)
    Question_Bank.append(newQuestion)
print(Question_Bank[0].text)

quiz= QuizBrain(Question_Bank)
while quiz.stillhasquestion():

    quiz.nextquestion()

print("You've completed the quiz")
print(f"Your final score is {quiz.score}/{len(Question_Bank)}")