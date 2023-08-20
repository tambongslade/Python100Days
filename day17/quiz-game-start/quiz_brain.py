class QuizBrain:
    def __init__(self,q_list):
        self.question_number=0
        self.question_list=q_list
        self.score=0

    def nextquestion(self):
        current_question=self.question_list[self.question_number]
        self.question_number+=1
        useranswer=input(f"Q. {self.question_number} {current_question.text} (true/false): ")
        self.check_answer(useranswer,current_question.answer)
    def  stillhasquestion(self):
        return self.question_number<len(self.question_list)
        
    def check_answer(self,user_answer,correct_answer):
        if user_answer.lower()==correct_answer.lower():
            self.score+=1
            print("you got it right")
        else:
            print("that's wrong")
        print(f"{correct_answer}")
        print(f"your current score is {self.score}/{self.question_number}")
        print("\n\n")