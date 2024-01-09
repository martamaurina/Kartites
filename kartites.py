from tkinter import*
from PIL import ImageTk, Image
import random
from tkinter import messagebox
gameWindow=Tk()
gameWindow.title("Matching game")

bgImg=ImageTk.PhotoImage(Image.open('a.jpg').resize((150,250)))

count=0
correctAnswers=0
answers=[]
answer_dict={}

def btnClick(btn,number):
    global count, correctAnswers, answers, answer_dict
    if btn['image']=='pyimage6'and count<2:
        btn['image']=ImageList[number]
        count+=1
        answers.append(number)
        answer_dict[btn]=ImageList[number]
    if len(answers)==2: #Ja atverās divas kartītes
        if ImageList[answers[0]]==ImageList[answers[1]]:
            for key in answer_dict:
                key["state"]=DISABLED
            correctAnswers+=2
            if correctAnswers==2: 
                messagebox.showinfo("Matching images", "You've guessed correctly")
                correctAnswers=0
            else:
                messagebox.showinfo("No matching images","You've guessed incorrectly")
                for key in answer_dict:
                     key['image']="pyimage1"
    count=0
    answers=[]
    answer_dict={}

    return 0

btn0=Button(width=150, height=250, image=bgImg, command=lambda:btnClick(btn0,0))
btn1=Button(width=150, height=250, image=bgImg, command=lambda:btnClick(btn1,1))
btn2=Button(width=150, height=250, image=bgImg, command=lambda:btnClick(btn2,2))
btn3=Button(width=150, height=250, image=bgImg, command=lambda:btnClick(btn3,3))
btn4=Button(width=150, height=250, image=bgImg, command=lambda:btnClick(btn4,4))
btn5=Button(width=150, height=250, image=bgImg, command=lambda:btnClick(btn5,5))
btn6=Button(width=150, height=250, image=bgImg, command=lambda:btnClick(btn6,6))
btn7=Button(width=150, height=250, image=bgImg, command=lambda:btnClick(btn7,7))
btn8=Button(width=150, height=250, image=bgImg, command=lambda:btnClick(btn8,8))
btn9=Button(width=150, height=250, image=bgImg, command=lambda:btnClick(btn9,9))
btn10=Button(width=150, height=250, image=bgImg, command=lambda:btnClick(btn10,10))
btn11=Button(width=150, height=250, image=bgImg, command=lambda:btnClick(btn11,11))



btn0.grid(row = 0, column = 0)
btn1.grid(row = 0, column = 1)
btn2.grid(row = 0, column = 2)
btn3.grid(row = 0, column = 3)
btn4.grid(row = 1, column = 0)
btn5.grid(row = 1, column = 1)
btn6.grid(row = 1, column = 2)
btn7.grid(row = 1, column = 3)
btn8.grid(row = 2, column = 0)
btn9.grid(row = 2, column = 1)
btn10.grid(row = 2, column = 2)
btn11.grid(row = 2, column = 3)


myImg1=ImageTk.PhotoImage(Image.open("1.png").resize((150,150)))
myImg2=ImageTk.PhotoImage(Image.open("2.webp").resize((130,130)))
myImg3=ImageTk.PhotoImage(Image.open("3.webp").resize((140,140)))
myImg4=ImageTk.PhotoImage(Image.open("4.webp").resize((150,150)))
myImg5=ImageTk.PhotoImage(Image.open("5.png").resize((170,170)))
myImg6=ImageTk.PhotoImage(Image.open("6.webp").resize((190,190)))


ImageList=[myImg1,myImg1,myImg2,myImg2,myImg3,myImg3,myImg4,myImg4,myImg5,myImg5,myImg6,myImg6]
random.shuffle(ImageList)

gameWindow.mainloop()
