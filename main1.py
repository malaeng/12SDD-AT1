from tkinter import *
from tkinter import ttk
import json
import random

class Page(Frame):
    def __init__(self, master, pagenumber):
        Frame.__init__(self)

        file = open("./questions.json")
        question_bank = json.load(file)
        self.questiondata = question_bank[pagenumber]
        print(self.questiondata)

        self.questiongroup1 = {
            self.questiondata[1][0]: "Correct",
            self.questiondata[1][1]: "Incorrect0",
            self.questiondata[1][2]: "Incorrect1",
            self.questiondata[1][3]: "Incorrect2"  
        }

        correct_answer = self.questiondata[1][0]
        file.close()
        self.masterframe = Frame(master)
        self.masterframe.pack()
        self.masterframe.grid_columnconfigure(0, weight=1)
        self.masterframe.grid_columnconfigure(1, weight=5)
        self.masterframe.grid_columnconfigure(2, weight=1)

        self.leftframe = Frame(self.masterframe, background='pink')
        self.leftframe.grid(row=1, column=0, sticky="nsew")

        self.questionframe = Frame(self.masterframe, bg='bisque')
        self.questionframe.grid(row=0, column=1, sticky="nsew")

        self.answerframe = Frame(self.masterframe, bg='cyan')
        self.answerframe.grid(row=1, column=1, sticky="nsew")

        self.rightframe = Frame(self.masterframe, background='pink')
        self.rightframe.grid(row=1, column=2, sticky="nsew")



        self.question = Label(self.questionframe, text=self.questiondata[0], font=("Ariel", 22), pady=80)
        self.question.pack()




        self.radiogroup1 = StringVar()

        self.row=1
        self.column=0
        for (text, value) in self.questiongroup1.items():
            Radiobutton(
                self.answerframe, 
                indicatoron=False, 
                text=text, 
                variable=self.radiogroup1, 
                value=value,
                padx=100,
                pady=10
                ).grid(row=self.row, column=self.column, padx=20, pady=20)
            if self.column == 0: self.column = 1; 
            elif self.column == 1: self.column = 0; self.row = 2



        self.leftbutton = Button(self.leftframe, text=" < ")
        self.leftbutton.pack(padx=70, pady=70, expand=True  )

        self.rightbutton = Button(self.rightframe, text=" > ", command=lambda : App.next(App, master))
        self.rightbutton.pack(padx=70, pady=70)

    def show(self):
        self.lift()


class App():
    
    def __init__(self, master):
        #Frame.__init__(self)
        super(App, self).__init__()
        self.style = ttk.Style(master)
        self.style.theme_use('default')
        self.style.configure('TRadiobutton', indicatoron=0, background="blue")
        
        questionbook = ttk.Notebook(master)
        questionbook.pack()

        file = open("./questions.json")
        question_bank = json.load(file)
        d = {}
        for i in range(len(question_bank)):
            d[f"questionframe{i}"] = Frame(questionbook)
            print(d)
            questionbook.add(d.get(i))

        print(d)
        file.close()

        

    def next(self, master):
        App.currentpage.forget()
        self.currentquestion += 1
        self.currentpage = Page(master, self.currentquestion)
        self.currentpage.place(in_=self.container, x=0, y=0, relwidth=1, relheight=1)

def main():

    root = Tk()
    root.geometry("960x640")
    app = App(root)
    root.mainloop()

if __name__ == "__main__": main()