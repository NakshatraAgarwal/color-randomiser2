from tkinter import *
import random

root = Tk()
root.geometry("500x500")
root.config(bg="cyan")

label = Label(root,font=("times",30),bg="cyan")
label.place(relx=0.5,rely=0.4,anchor=CENTER)

l_score = Label(root,text="Score: 0",bg="cyan")
l_score.place(relx=0.1,rely=0.1,anchor=W)

input_value = Entry(root)
input_value.place(relx=0.5,rely=0.5)

class game():
    def __init__(self):
        self.__score = 0
        
    def updateGame(self):
        self.text = ["green","black","yellow","red","pink",""]
        self.random_no = random.randint(0,3)
        self.color = ["green","black","yellow","red"]
        self.random_color = random.randint(0,3)
        label["text"] = self.text[self.random_no]
        label["fg"] = self.color[self.random_color]
        
    def __update_score(self,input_value):
        if(input_value == self.color[self.random_color]):
            print(self.color[self.random_color])
            self.__score = self.__score + random.randint(0,10)
            l_score["text"] = "Score: " + str(self.__score)
    
    def getUserValue(self,input_value):
        self.__update_score(input_value)
        
obj = game()
def getInput():
    value = input_value.get()
    obj.getUserValue(value)
    obj.updateGame()
    input_value.delete(0,END)
    
    
btn = Button(root,text="Start",command=obj.updateGame)
btn.place(relx=0.4,rely=0.7,anchor=CENTER)
btn2 = Button(root,text="Check",command=getInput)
btn2.place(relx=0.5,rely=0.7,anchor=CENTER)

root.mainloop()
    
        
            
            
        