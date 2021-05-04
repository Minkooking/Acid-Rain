from tkinter import *
from tkinter.messagebox import *
import random
import time
import csv
import operator

color1='#9be7f0' #연한 하늘색.
color2='#9be7f0'

class mainUI():
    def __init__(self,parent):
        self.parent=parent
        self.initUI()
        
    def initUI(self):
        global nameselect
        #메인 윈도
        self.parent.geometry('500x550+650+300')
        self.parent.resizable(width=FALSE,height=FALSE)
        self.parent.title('오지는 타자연습')
        
        # 라벨1
        self.ptitle=PhotoImage(file="./title.gif")
        self.label11=Label(self.parent,image=self.ptitle,bg='white')
        self.label11.place(relx=-.03,rely=.1)


        # 라벨2
        self.pset=PhotoImage(file="./dss.gif")
        self.label21=Label(self.parent,image=self.pset,bg='white')
        self.label21.place(relx=.1,rely=.345)

        # 단어세트 listbox

        self.menubt11=Listbox(self.parent, width=32,height=0,selectmode=SINGLE)
        i=0
        for j in dataset:
            self.menubt11.insert(i+1,j)
            i+=1
        self.menubt11['bg']=color1
        self.menubt11.select_set(wordselect)
        self.menubt11.place(relx=.35,rely=.35)
        self.menubt11.bind('<<ListboxSelect>>',self.word_select)

        # 사용자이름 & 빈칸
        namelist=history()[0]
        self.psa = PhotoImage(file="./uns.gif")
        self.name11=Label(self.parent,image=self.psa,bg='white')
        variable = StringVar(self.parent)
        if len(namelist):
            variable.set(namelist[0])
            nameselect=namelist[0]
            self.nameet11=OptionMenu(self.parent,variable,*namelist,command=self.name_select)
            self.nameet11['bg']=color1
            self.nameet11.tk_strictMotif(boolean=1)
        else:
            self.nameet11=OptionMenu(self.parent,variable,"")
            self.nameet11['bg']=color1
            self.nameet11.tk_strictMotif(boolean=1)
            nameselect=""
        self.nameet11.config(width=26)
        self.namesubmit=Entry(self.parent,width=12,font=('',16))
        self.namesubmit['bg']=color1
        self.name11.place(relx=.1,rely=.55)
        self.nameet11.place(relx=.35,rely=.53)
        self.namesubmit.place(relx=.355,rely=.6)

        # 중복확인 버튼
        self.dr=PhotoImage(file='./dr.gif')
        self.check11=Button(self.parent,text='등록',command=self.namecheck,image=self.dr)
        self.check11.place(relx=.644,rely=.595)
        self.sj=PhotoImage(file='./sj.gif')
        self.check21=Button(self.parent,text='삭제',command=self.nameremove,image=self.sj)
        self.check21.place(relx=.745,rely=.595)

        # 게임 방법
        self.imghtp = PhotoImage(file="./gb.gif")
        self.howtoplay11=Button(self.parent,command=self.howtoplay,image=self.imghtp,highlightthickness = 0, bd = 0)
        self.howtoplay11.place(relx=.03,rely=.73)
        
        # 시작 버튼
        self.gs=PhotoImage(file='./gs.gif')
        self.start11=Button(self.parent,command=self.start,image=self.gs,highlightthickness = 0, bd = 0)
        self.start11.place(relx=.359,rely=.73)

        # 종료 버튼
        self.gj=PhotoImage(file="./gj.gif")
        self.quit11=Button(self.parent,command=self.quit,image=self.gj,highlightthickness = 0, bd = 0)
        self.quit11.place(relx=.68,rely=.73)

        # 저작권 라벨3
        self.copyright=PhotoImage(file='./copyright.gif')
        self.label131=Label(self.parent,image=self.copyright,bg='white')
        self.label131.pack(side='bottom',anchor='se')

    def word_select(self,event):
        global wordselect
        if len(event.widget.curselection()):
            wordselect=event.widget.curselection()[-1]
        window11.destroy()
        main()                           
        
    def name_select(self,value):
        global nameselect
        nameselect = value
        
    def namecheck(self):
        global userdata
        namelist=history()[0]
        inputname=self.namesubmit.get()
        tf=inputname in namelist
        if inputname=='':
            showerror('중복확인','이름은 필수 값입니다.')
        else:
            if tf==False:
                nameyn=askyesno('중복확인','해당 이름은 사용 가능합니다.\n해당 이름을 등록하시겠습니까?')
                if nameyn:
                    userdata[0].append(inputname)
                    userdata[0].append(0)
                    userdata[0].append(time.time())
                    i=1
                    while i<len(userdata):
                        userdata[i].append(1)
                        userdata[i].append(1)
                        userdata[i].append("")
                        i+=1
                    save()
                    window11.destroy()
                    main()                    
                    
            else:
                showerror('중복확인','해당 이름은 사용할 수 없습니다.\n다른 이름을 사용해주세요.')
                
    def nameremove(self):
        global userdata
        temp=userdata[0].index(nameselect)
        i=0
        while i<len(userdata):
            del userdata[i][temp:temp+3]
            i+=1


        save()
        window11.destroy()
        main() 
    
    def howtoplay(self):
        self.popup11=Toplevel(self.parent)
        self.popup11.title('게임 방법')
        self.popup11.geometry('595x760+200+200')
        
        img11=PhotoImage(file='./howtoplay.gif')
        lbl11=Label(self.popup11,image=img11)
        lbl11.place(x=0,y=0)
        self.popup11.mainloop()

    def start(self):
        global main_2
        if nameselect!="":
            main_2=1
            self.parent.destroy()
        else:
            showerror("","이름을 설정해주세요")            
            self.parent.destroy()
            main()
        

    def quit(self):
        global stop
        yn=askyesno('게임종료','게임을 종료하시겠습니까?')
        if yn==1:
            self.parent.destroy()
            stop=1

def main():
    global window11
    window11=Tk()
    window11['bg']='white'
    mainUI(window11)
    window11.after(0, lambda: window11.focus_force())
    window11.mainloop()

class outputUI():
    def __init__(self,parent):
        self.parent=parent
        self.initUI()
        
    def initUI(self):
        #결과 윈도
        self.parent.geometry('600x700+650+300')
        self.parent.resizable(width=FALSE,height=FALSE)
        self.parent.title('결과')

        #결과라벨 순위표
        self.ranking=PhotoImage(file='./wideranking.gif')
        self.lbl33=Label(self.parent,image=self.ranking,bg='white')
        self.lbl33.pack(side='top',pady=30)

        #데이터에서 순위 가져오는 라벨
        self.rank1=Label(self.parent,text=scoretemp,bg='white',justify=LEFT)
        self.rank1.config(font=('',18,'bold'))
        self.rank1.place(relx=.1,rely=.275)

        Label(self.parent,text='%s'%dataset[wordselect],bg='white',font=('',20,'bold')).place(relx=.717,rely=.11)
        
        #처음으로 버튼
        self.gofirst=PhotoImage(file='./gofirst.gif')
        self.tomain=Button(self.parent,command=self.tomain,image=self.gofirst,highlightthickness = 0, bd = 0)
        self.tomain.place(relx=.03,rely=.845)

        #다시하기 버튼
        self.dodo=PhotoImage(file='./dodo.gif')
        self.restart=Button(self.parent,command=self.restart,image=self.dodo,highlightthickness = 0, bd = 0)
        self.restart.place(relx=.359,rely=.845)
        
        #종료 버튼
        self.nodo=PhotoImage(file='./nodo.gif')
        self.quit31=Button(self.parent,command=self.quit,image=self.nodo,highlightthickness = 0, bd = 0)
        self.quit31.place(relx=.68,rely=.845)


    def rank():
        global totalrank
        global scoretemp
        totalrank=history()

        
        sorter=sorted(list(zip(totalrank[0],totalrank[1],totalrank[2])),key=operator.itemgetter(1),reverse=True)
        i=0
        scoretemp=""
        while i<len(sorter) and i<3:
            scoretemp+='\n\n%d등 %13s'%(i+1,sorter[i][0])+'         %s'%str(sorter[i][1]*10)+'    %s'%time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(sorter[i][2]))+'\n\n'
            i+=1

    def tomain(self):
        global main_1
        main_1=1
        self.parent.destroy()
        
    def restart(self):
        global main_2
        main_2=1
        self.parent.destroy()
        
    def quit(self):
        global stop
        yn=askyesno('게임종료','게임을 종료하시겠습니까?')
        if yn==1:
            self.parent.destroy()
            stop=1

           
def run(): #게임 실행
    global wordcount
    global word
    global wordin
    global wordout
    global display
    global sec
    global score
    global now
    global health
    global wrong, combo
    global userdata,wordnum

    timelabel1.configure(text='게임진행시간 \n\n'+str(int((time.time()-start)/60))+"분 "+str(int(time.time()-start)%60)+'초')

    wordout = random.randint(1, 8) #단어 등장 빈도수 조정 1~10 범위의 난수 생성
    if wordout==1: #10%의 확률로 1이 나오면~
        i=0
        while i<8:
            word[i]="\n"+word[i] #~모든 열에 줄 하나씩 추가 후~
            i+=1
        word[display]=worddata[wordcount]+word[display] #~랜덤한 열에 단어를 하나 배치
        wordcount+=1
    else: #90%확률로 1이 안나오면~
        i=0
        while i<8:
            word[i]="\n"+word[i] #~모든 열에 줄 하나씩 추가 
            i+=1

    i=0
    while i<8:
        if word[i].count("\n")==30: #한 열의 줄이 30줄이 되면
            if word[i][word[i].rfind("\n")+1:]!="": #30번째 줄에 단어가 있으면
                weight[worddata.index(word[i][word[i].rfind("\n")+1:])][1]+=1
                userdata[worddata.index(word[i][word[i].rfind("\n")+1:])+1][userdata[0].index(nameselect)+1]+=1
                health-=1 #체력 -1
                wrong+=1
                combo=0
            word[i]=word[i][0:word[i].rfind("\n")] #30번째줄 제거                
        i+=1    

    display=random.randint(1,8)-1 #다음 화면에서 어떤 열에 단어를 배출할지 랜덤으로 선택

    label112_1.configure(text=word[0])
    label112_2.configure(text=word[1])
    label112_3.configure(text=word[2])
    label112_4.configure(text=word[3])
    label112_5.configure(text=word[4])
    label112_6.configure(text=word[5])
    label112_7.configure(text=word[6])
    label112_8.configure(text=word[7])
    scorelabel1.configure(text="단어 맞춘 개수 : "+str(score)+"개")
    healthlabel1.configure(text="체력 : "+"■"*health+"□"*(maxhealth-health))
    combolabel.configure(text="COMBO x %2d !!" %combo)
    
    sectemp=(sec/wordinframe) #줄이 내려오는 시간 조정

    combocheck=0
    j=0
    while j<8: #사용자가 입력한 단어가 화면에 있는지 검색
        wordtemp=word[j].split("\n")
        k=0
        while k<len(wordtemp):
            wordtemp[k]=wordtemp[k].strip()
            k+=1
        if wordin!="" and wordin in wordtemp:
            wordtemp.remove(wordin)
            word[j]="\n".join(wordtemp)
            score+=1
            wordnum=worddata.index(wordin)
            weight[wordnum][1]+=1
            userdata[wordnum+1][userdata[0].index(nameselect)]+=1
            meantemp=wordin+'\n\n'+userdata[wordnum+1][1]
            meanlabel1.configure(text=meantemp+"\n\n\n")
            combo+=1
            combocheck+=1
        j+=1

    if combo==10:
        combo=0
        if random.random()>0.5:
            health=10
            meanlabel1.configure(text=meantemp+"\n\n\n*****체력 회복!*****")
        else:
            sec*=1.4
            meanlabel1.configure(text=meantemp+"\n\n\n*****속도 감소!*****")
        
        
    sec=sec-acc #가속도 조정

    if health<1:
        end()
    else:
        main2.after(int(sectemp),run)
        
def wordinput(event):
    global wordin
    global wordent
    wordin = wordent.get().strip()
    wordent.delete(0, END)
    
def wordinput2():
    global wordin
    global wordent
    wordin = wordent.get().strip()
    wordent.delete(0, END)

def end():
    global main_3
    global userdata
    main_3=1
    scoretemp=int(userdata[0][userdata[0].index(nameselect)+1])
    if score>scoretemp:
        userdata[0][userdata[0].index(nameselect)+1]=score
    userdata[0][userdata[0].index(nameselect)+2]=time.time()
    mix()    
    showerror("","       게임 오버!!       ")
    main2.destroy()

def wait():
    s=0
    waitsecond=showinfo("","       게임 시작!!       ")
    run()
    
def output():
    window31=Tk()
    window31['bg']='white'
    outputUI.rank()
    outputUI(window31)
    window31.mainloop()


def history():
    global userdata,lines
    f=open('./%s.csv' %dataset[wordselect],'r')
    reader=csv.reader(f)
    lines=[]
    for i in reader:
        lines.append(i)
    f.close()

    i=1
    while i<len(lines):
        j=0
        while j<(len(lines[0])-2)/3:
            lines[i][j*3+2]=int(lines[i][j*3+2])
            lines[i][j*3+3]=int(lines[i][j*3+3])
            j+=1
        i+=1
            
    userdata=lines
    

    i=0
    playername,writtenscore,writtentime=[],[],[]
    while i<len(lines[0]):
        if i>1:
            if i%3==2:
                playername.append(lines[0][i])
            elif i%3==0:
                writtenscore.append(int(lines[0][i]))
            elif i%3==1:
                writtentime.append(float(lines[0][i]))
        i+=1

    return [playername,writtenscore,writtentime]

def mix():
    global userdata
    colnum=userdata[0].index(nameselect)

    ordertemp=[0]
    i=1
    while i<len(userdata):
        ordertemp.append(userdata[i][colnum]/(userdata[i][colnum]+userdata[i][colnum+1])*random.random()+0.1)
        i+=1

    order=[None]*len(ordertemp)
    j=0
    for i in ordertemp[1:]:
        order[sorted(ordertemp[1:],reverse=True).index(i)+1]=j
        j+=1

    datatemp=[None]*len(order)
    i=1
    while i<len(order):
        datatemp[order[i]+1]=userdata[i]
        i+=1

    i=1
    while i<len(datatemp):
        userdata[i]=datatemp[i]
        i+=1
        
    update()
    save()

def update():
    global worddata,weight
    worddata=[]
    weight=[]
    for i in userdata[1:]:
        worddata.append(i[0])
        weight.append([int(i[userdata[0].index(nameselect)]),int(i[userdata[0].index(nameselect)+1])])

def save():
    f=open("./%s.csv" %dataset[wordselect],"w",newline='')
    writer=csv.writer(f,delimiter=',')
    for i in userdata:
        writer.writerow(i)
    f.close()

    
    
           










wordselect=0
main_1=1
main_2=0
main_3=0
stop=0
dataset=[ #데이터셋 등록
    "초등학교",
    "중학교",
    ]
datasetspeed=[
    5000.0,
    6000.0    
    ]
datasetacc=[
    2,
    2
    ]








while stop!=1:
    if main_1:
        main_1=0
        main()
        
    if main_2:
        main_2=0
        combo=0
        ##############옵션
        wordinframe=20 #1초에 단어 입력을 몇번 확인할 것인지 지정
        health=10 #체력
        maxhealth=10 #최대 체력

        word=[""]*8
        display=random.randint(1,8)-1 #게임 화면 세로 몇번째 줄에 단어를 띄울 것인지 지정하기 위해 난수를 생성
    
        wordcount=0 # 등장한 단어 갯수
        score=0 #맞춘 단어 갯수
        wrong=0 #틀린 단어 갯수
        sec=datasetspeed[wordselect] #시간 지연(기본 속도)
        acc=datasetacc[wordselect] #기본 1배 가속
        fontsize=15 #글자크기
        maxwordlength=13 #글자 칸 수 또는 게임 화면 열의 너비(단위 : 글자 수)

        start=time.time() #시작 시간

        wordin=""

        mix()            

        main2 = Tk()
        main2.after(0, lambda: main2.focus_force())
        main2.title("오지는 타자연습")
        main2.geometry("1550x800+200+180")
        main2.resizable(width=FALSE, height=FALSE)

        
        frame12=Frame(main2,width=1000,height=800,bg=color2)
        frame12_1=Frame(frame12,bg=color2)
        frame112=Frame(frame12_1,width=1000,height=600,bg=color2) ### 단어 나오는 곳

        label112_1=Label(frame112,text=word[0],font=("Arial",fontsize),width=maxwordlength,height=30,anchor=N,bg=color2) ###라벨에 텍스트를 입력하면 크기 단위가 픽셀이 아닌 글자 수로 변함
        label112_1.pack(side=LEFT)

        label112_2=Label(frame112,text=word[1],font=("Arial",fontsize),width=maxwordlength,height=30,anchor=N,bg=color2)
        label112_2.pack(side=LEFT)

        label112_3=Label(frame112,text=word[2],font=("Arial",fontsize),width=maxwordlength,height=30,anchor=N,bg=color2)
        label112_3.pack(side=LEFT)

        label112_4=Label(frame112,text=word[3],font=("Arial",fontsize),width=maxwordlength,height=30,anchor=N,bg=color2)
        label112_4.pack(side=LEFT)

        label112_5=Label(frame112,text=word[4],font=("Arial",fontsize),width=maxwordlength,height=30,anchor=N,bg=color2)
        label112_5.pack(side=LEFT)

        label112_6=Label(frame112,text=word[5],font=("Arial",fontsize),width=maxwordlength,height=30,anchor=N,bg=color2)
        label112_6.pack(side=LEFT)

        label112_7=Label(frame112,text=word[6],font=("Arial",fontsize),width=maxwordlength,height=30,anchor=N,bg=color2)
        label112_7.pack(side=LEFT)

        label112_8=Label(frame112,text=word[7],font=("Arial",fontsize),width=maxwordlength,height=30,anchor=N,bg=color2)
        label112_8.pack(side=LEFT)

        frame112.pack(pady=5)
        frame12_1.pack()



        frame122=Frame(frame12,bg='#4066E8',width=1000) ### 단어 입력하는 곳
        frame122_1=Frame(frame122)

        
        deletelinelabel1=Label(frame122,font=('Arial',fontsize),text=' '*maxwordlength*16,bg='#40CFE8').pack()
        
        wordent=Entry(frame122_1, bd =5)
        wordent.insert(13, "")
        wordent.bind("<Return>",wordinput)

        
        wordent.pack()
        wordent.focus_set()
        wordbutton=Button(frame122_1,text="단어 입력",width=20, bd=5, command=wordinput2)
        wordbutton.pack()

        frame122_1.pack()
        frame122.pack(expand=True,fill=BOTH)

        frame12.pack(side=LEFT)

        frame121=Frame(main2,bg='white',width=300)
        frame121.pack()

    
        frame124=Frame(main2,bg='white',width=300)
        frame124.pack()
        
        timelabel1=Label(frame124,text='게임진행시간 \n\n0분 0초',bg='white',width=300,font=('',20,'bold'))
        timelabel1.pack(pady=80)
        
        frame123=Frame(main2,bg="white",width=300,height=300) ### 정보 창 / 단어 맞춘개수,틀린 개수, 점수,단어 뜻
        frame123.pack(side=BOTTOM)

        scorelabel1=Label(frame123,text="단어 맞춘 개수 : 0개",font=('',15,'bold'),width=40,bg='white')
        scorelabel1.pack(padx=10,pady=20)

        healthlabel1=Label(frame123,text="체력 : "+"■"*health+"□"*(maxhealth-health),font=('',15,'bold'),width=40,bg='white')
        healthlabel1.pack(padx=10,pady=30)

        meanlabel1=Label(frame123,text='\n\n\n\n\n',font=('Arial',22,'bold'),bg='white')
        meanlabel1.pack(pady=20)

        combolabel=Label(frame123,text="COMBO x  0 !!",font=('Arial',22,'bold'),bg='white')
        combolabel.pack(pady=50)
        
        main2.after(0,wait)      
        main2.mainloop()

        if main_3:
            main_3=0
            output()


