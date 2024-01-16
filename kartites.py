from tkinter import* #savādāk nevar izveidot rāmi
from PIL import ImageTk, Image #nodrošina attēlu ievietošanu
import random #sajauc bildes
from tkinter import messagebox
MansLogs=Tk()
MansLogs.title("Matching game")

bgImg=ImageTk.PhotoImage(Image.open('7.jpg').resize((150,250))) #fona attēls

count=0
correctAnswers=0
answers=[] #masīvs
answer_dict={} #vārdnīca
answerCount=0

def btnClick(btn,number): #šī funkcija tiek pielikta klāt pogām
    global count, correctAnswers, answers, answer_dict
    if btn['image']=='pyimage1'and count<2:
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
                #answerCount+=1
        else:
            messagebox.showinfo("No matching images","You've guessed incorrectly")
            for key in answer_dict:
                key['image']="pyimage1"
        count=0
        answers=[]
        answer_dict={}
    #if answerCount==6: #1
        #messagebox.showinfo("Wow","You win!")
    #reset()
    return 0

def infoLogs(): #izvēles logs
    newLogs=Toplevel()
    newLogs.title('Info par programmu') #loga nosaukums
    newLogs.geometry("665x240") #loga imērs
    desc=Label(newLogs, text='')
    desc.grid(row=0, column=0) #atrašanās vieta
    desc=Label(newLogs, text=' SPĒLES NOTEIKUMI',bg = "#FAE7CC", font=('Helvica 10 bold') ) #Teksts
    desc.grid(row=1, column=0)
    desc=Label(newLogs, text='')
    desc.grid(row=2, column=0)
    desc=Label(newLogs, text=' Spēles sākumā visas kārtis tiek sajauktas un izliktas kolonnās un rindās ar seju uz leju.')
    desc.grid(row=3, column=0)
    desc=Label(newLogs, text=' Spēlētājs sāk spēli un apgriež divas kārtis. Gadījumā, ja kārtis nesakrīt, tas nav pāris, tāpēc viņas tiek apgrieztas atpakaļ.')
    desc.grid(row=4, column=0)
    desc=Label(newLogs, text=' Spēle visu laiku atkārtojās, kamēr spēlētājs uzmin divas kārtis vai atcerās kāršu novietojumu un apgriež abas identiskās kārtis.')
    desc.grid(row=5, column=0)
    desc=Label(newLogs, text=' Abas kārtis sakrīt, tas ir pāris! Abas kārtis ir atrastas un tās vairs nevar apgriest.')
    desc.grid(row=6, column=0)
    desc=Label(newLogs, text=' Spēli var turpināt tālāk, kamēr visi kāršu pāri ir atrasti.')
    desc.grid(row=7, column=0)
    desc=Label(newLogs, text=' ')
    desc.grid(row=8, column=0)
    desc=Label(newLogs, text=' Opcijās ir iespēja spēli aizvērt vai sākt spēli pa jaunam.',bg = "#FAE7CC")
    desc.grid(row=9, column=0)
    
    return 0

def reset(): #spēli atsāk no sākuma
    global count, correctAnswers, answers, answer_dict
    btn0.config(state=NORMAL) #pogu stāvoklis, kad ir gatavs darbam
    btn1.config(state=NORMAL)
    btn2.config(state=NORMAL)
    btn3.config(state=NORMAL)
    btn4.config(state=NORMAL)
    btn5.config(state=NORMAL)
    btn6.config(state=NORMAL)
    btn7.config(state=NORMAL)
    btn8.config(state=NORMAL)
    btn9.config(state=NORMAL)
    btn10.config(state=NORMAL)
    btn11.config(state=NORMAL)
    btn0['image']='pyimage1' # visām bildēm priekšā ir fona attēls
    btn1['image']='pyimage1'
    btn2['image']='pyimage1'
    btn3['image']='pyimage1'
    btn4['image']='pyimage1'
    btn5['image']='pyimage1'
    btn6['image']='pyimage1'
    btn7['image']='pyimage1'
    btn8['image']='pyimage1'
    btn9['image']='pyimage1'
    btn10['image']='pyimage1'
    btn11['image']='pyimage1'
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



btn0.grid(row = 0, column = 0) #pogu atrašanās vieta
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


myImg1=ImageTk.PhotoImage(Image.open("1.jpg").resize((150,150)))
myImg2=ImageTk.PhotoImage(Image.open("2.jpg").resize((130,130)))
myImg3=ImageTk.PhotoImage(Image.open("3.jpg").resize((140,140)))
myImg4=ImageTk.PhotoImage(Image.open("4.jpg").resize((150,150)))
myImg5=ImageTk.PhotoImage(Image.open("5.jpg").resize((170,170)))
myImg6=ImageTk.PhotoImage(Image.open("6.jpg").resize((190,190)))


ImageList=[myImg1,myImg1,myImg2,myImg2,myImg3,myImg3,myImg4,myImg4,myImg5,myImg5,myImg6,myImg6]
random.shuffle(ImageList)


galvenaIzvelne=Menu(MansLogs)#izveido galveno izvelni
MansLogs.config(menu=galvenaIzvelne)

opcijas=Menu(galvenaIzvelne, tearoff=False)#maza izvēlne
galvenaIzvelne.add_cascade(label="Opcijas", menu=opcijas)#lejupkritošais  saraksts

opcijas.add_command(label="Jauna spēle", command=reset)
opcijas.add_command(label="Iziet", command=MansLogs.quit)
galvenaIzvelne.add_command(label="Par programmu", command=infoLogs)


MansLogs.mainloop()
