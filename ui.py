THEME_COLOR = "#375362"
from quiz_brain import QuizBrain
from tkinter import *

class QuizInterface:

    def __init__(self,quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(pady= 20, padx= 20,bg=THEME_COLOR)
        self.score = Label(fg="white",text=f"Score: {0}",font=("Nunito",14,"normal"),bg= THEME_COLOR)
        self.score.grid(row = 0, column = 1)

        self.canvas = Canvas(bg="white",height=250,width=300)
        self.question_txt = self.canvas.create_text(150,125, text="Some Question Text",fill=THEME_COLOR,font=("Arial",20,"italic"),width=260)
        self.canvas.grid(row = 1, column = 0,columnspan = 2,pady =50 )

        image = PhotoImage(file="./images/true.png")
        self.true_button = Button(image=image, height= 150,width=150,fg=THEME_COLOR,bg=THEME_COLOR,border=0,highlightthickness= 0,command= self.check_true)
        self.true_button.grid(row = 2, column = 0)
        self.true_button.config(pady=50,padx=20)

        fimage = PhotoImage(file="./images/false.png")
        self.wrong_button = Button(image=fimage, height=150, width=150, fg=THEME_COLOR, bg=THEME_COLOR, border=0,highlightthickness=0,command= self.check_false)
        self.wrong_button.grid(row=2, column=1)
        self.wrong_button.config(pady=50, padx=20)

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():


            q_text = self.quiz.next_question()
            self.score.config(text=f"Score: {self.quiz.score}")
            self.canvas.itemconfig(self.question_txt, text = q_text)
        else:
            self.canvas.itemconfig(self.question_txt,text= "You've reached the end of the Quiz")
            self.true_button.config(state = "disabled")
            self.wrong_button.config(state="disabled")

    def check_true(self):
        self.give_feedback(self.quiz.check_answer("true"))

    def check_false(self):
        self.give_feedback(self.quiz.check_answer("false"))


    def give_feedback(self, is_right):

        if is_right:
            self.canvas.config(bg = "green")
        else:
            self.canvas.config(bg = "red")


        self.window.after(1000,self.get_next_question)





