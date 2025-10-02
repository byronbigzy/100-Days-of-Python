#TODO: asking the qeustions
#TODO: checking if the answer was correct
#TODO: checking if we're the end of the quiz

class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.questions_list = q_list
        self.score = 0

    def next_question(self):
        current_question = self.questions_list[self.question_number]
        self.question_number += 1
        userAnswer = input(f"Q.{self.question_number}: {current_question.text} ('True' or 'False') ")
        self.check_answer(userAnswer, current_question.answer)

    def still_has_questions(self):
        return self.question_number < len(self.questions_list)

        
    def check_answer(self, userAnswer, correctAnswer):
        if userAnswer == correctAnswer:
            self.score += 1
            print("You've got it correct.")
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correctAnswer}")
        print(f"Your current score is: {self.score}/{self.question_number}.")
        print("\n\n")