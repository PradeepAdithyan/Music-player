from tkinter import *
import tkinter as tk
import smtplib
import random
import mysql.connector
import os
from pygame import mixer
import pygame
from PIL import ImageTk,Image
import tkinter.filedialog as fdialog

mydb_user=mysql.connector.connect(host="localhost",user="root",password="Your MYSQL password",auth_plugin='mysql_native_password',database="user_info")
Mycursor1=mydb_user.cursor()
Mycursor1.execute("CREATE TABLE IF NOT EXISTS user(id int primary key auto_increment not null,name varchar(20) not null,gender varchar(6) not null,age int not null,mail_id varchar(30) not null,passwd varchar(10) not null)")
    
def play():
    mydb=mysql.connector.connect(host="localhost",user="root",password="Admin@123",auth_plugin='mysql_native_password',database='test')
    Mycursor=mydb.cursor()
    Mycursor.execute("CREATE TABLE IF NOT EXISTS music (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,songs varchar(50) NOT NULL,song_name varchar(20) NOT NULL )")
    
    def songname(fn): 
        root=tk.Tk()
        root.geometry("400x250")
        root.title("SONG NAME")
        
        Canvas3 = Canvas(root)    
        Canvas3.config(bg="#00CED1")
        Canvas3.pack(expand=True,fill=BOTH)
        
        def submit():
            name=name_entry.get()
            data=(fn,name)
            print(data)
            if (fn!=""):
                sql="INSERT INTO music2 (songs,song_name) VALUES (%s,%s)"
                Mycursor.execute(sql,data)
                mydb.commit()
                messagebox.showinfo("SUCCESS !!","YOUR FILE HAS BEEN SAVED TO DATABASE")
            else:
                messagebox.showinfo("ERROR","PLEASE CHOOSE A VALID FILE LOCATION")
                
        name_lable=tk.Label(root,text="ENTER THE SONG NAME ",font=('calibre', 10, 'bold'))
        name_lable.place(x=10,y=70)
        name_entry=tk.Entry(root)
        sub_btn=tk.Button(root,text = 'Submit',command = submit,font=('calibre',10, 'bold'),bg='black',fg='white') 
        name_entry.place(x=200,y=70)
        sub_btn.place(x=130,y=100)
    
    def savedata():
        fn=fdialog.askopenfilename(filetype=(("Music Files","*.mp3"),("Music Files","*.mp4")),initialdir= "/", title='Please select a directory')
        songname(fn)
            
    def readdata():
        data=[]
        sql="SELECT songs FROM music2 "
        Mycursor.execute(sql)
        record = Mycursor.fetchall()
        for i in record:
            temp=i[0]
            data.append(temp)
            
        song_name=[]
        sql="select song_name from music2"
        Mycursor.execute(sql)
        record=Mycursor.fetchall()
        for i in record:
            temp=i[0]
            song_name.append(temp)
        
        root = Tk()
        root.geometry("450x350")
        root.title("MUSIC PLAYER")
        
        Canvas3 = Canvas(root)    
        Canvas3.config(bg="#00CED1")
        Canvas3.pack(expand=True,fill=BOTH)
        
        listofsongs = []
        
        index = 0  
        current_song=0 
        
        def directorychooser():
            
            for files in data:
                if files.endswith(".mp3"):
        
                    listofsongs.append(files)
                    
            pygame.mixer.init()
            for i in range (0,len(listofsongs)):
                pygame.mixer.music.load(listofsongs[i])
                pygame.mixer.music.play()
                current_song=i
            
        directorychooser()
        
        label = Label(root,text='Music Player')
        label.pack()
        
        listbox = Listbox(root)
        listbox.place(x=150,y=10)
        
        listofsongs.reverse()
        
        for items in song_name:
            listbox.insert(0,items)
        
        listofsongs.reverse()
        
        def pause():
            mixer.music.pause()
        
        def un_pause():
            mixer.music.unpause() 
        
        def stop():
            mixer.music.stop()
            
        def nextsong():
            i=current_song+1
            pygame.mixer.music.load(listofsongs[i])
            pygame.mixer.music.play()
            current_song+=1
                
        def previous_song():
                i=current_song-1
                pygame.mixer.music.load(listofsongs[i])
                pygame.mixer.music.play()
                current_song-=1
    
        pausebutton = Button(root,text = 'Pause',command=pause,bg='black', fg='white')
        pausebutton.place(x=160,y=190)
        
        un_pausebutton = Button(root,text='Un-Pause',command=un_pause,bg='black', fg='white')
        un_pausebutton.place(x=210,y=190)
        
        nextbutton = Button(root,text = 'Next Song',command=nextsong,bg='black', fg='white')
        nextbutton.place(x=180,y=220)
        
        previousbutton = Button(root,text='Previous Song',command=previous_song,bg='black', fg='white')
        previousbutton.place(x=180,y=250)
        
        stopbutton = Button(root,text='Stop music',command=stop,bg='black', fg='white')
        stopbutton.place(x=180,y=280)

    win=Tk()
    win.geometry("400x250")
    win.title("CHOOSE A PATH")
    
    
    Canvas2 = Canvas(win)    
    Canvas2.config(bg="#00CED1")
    Canvas2.pack(expand=True,fill=BOTH)
    
    savedata=Button(win,text="ADD SONGS",command=savedata)
    savedata.place(x=130,y=100)
    readdata=Button(win,text="PLAY SONGS",command=readdata)
    readdata.place(x=130,y=140)
    
    win.mainloop()

def new():
    try:
        check=("""create trigger mail_check 
            before insert on user
            for each row 
            begin 
            if (exists(select * from user where mail_id=new.mail_id)) 
            then 
            signal sqlstate '45000' 
            set message_text='ERROE! MAIL ID ALREADY EXIST';
            end if; 
            end;""")
        
        Mycursor1.execute(check)
        mydb_user.commit()
    
    except:
        pass

    tp=tk.Tk()
    tp.geometry("400x250")
    tp.title("NEW ACCOUNT")
    
    Canvas3 = Canvas(tp)    
    Canvas3.config(bg="#00CED1")
    Canvas3.pack(expand=True,fill=BOTH)
    
    def submit():
        name=a1.get()
        gender=b2.get()
        age=c3.get()
        mail_id=d4.get()
        password=e5.get
    
        user="Your mail id"
        password="Your mail id password"
        sender = 'Your mail id'
        receivers=[mail_id]
        otp=random.randint(1000,9999)
        message = """
        
        Dear user! Welcome to Music player project by Pradeep and Sathya your
        OTP code for registration is %s
        """%(otp)
        
        try:
            server = smtplib.SMTP("smtp.gmail.com",587)
            server.ehlo()
            server.starttls()
            server.login(user,password)
            server.sendmail(sender,mail_id, message)
            server.quit()         
            messagebox.showinfo("Success","OTP HAS BEEN SENT")
                
        except Exception:
            messagebox.showinfo("Error"," Unable to send mail")
            
        def submitotp():
            user_otp=otp_entry.get()
            #if(user_otp==otp):
            try:
                insert_val="insert into user(name,gender,age,mail_id,passwd) values(%s,%s,%s,%s,%s) "
                details=(name,gender,age,mail_id,password)
                Mycursor1.execute(insert_val,details)
                mydb_user.commit()
                messagebox.showinfo("Success","Your account has been created")
            except Exception:
                messagebox.showinfo("ERROR","This mail-id already exists ")
            #else:
             #   messagebox.showinfo("ERROR","Invalid OTP")
        tm=tk.Tk()       
        tm.geometry("400x250")
        tm.title("OTP VERIFICATION")
        
        Canvas1 = Canvas(tm)    
        Canvas1.config(bg="#00CED1")
        Canvas1.pack(expand=True,fill=BOTH)

        otp_grid=tk.Label(tm,text="Enter OTP :")
        otp_grid.place(x=30,y=30)
        otp_entry=tk.Entry(tm,width=20)
        otp_entry.place(x=100,y=30)
        submit_otp=tk.Button(tm,text="Submit",command  = submitotp,bg='black',fg='white')
        submit_otp.place(x=60,y=70)

        
    uname = tk.Label(tp, text = "NAME:",font=('calibre', 10, 'bold'))
    uname.place(x = 30,y = 30)
    gender_lable = tk.Label(tp, text = "GENDER:",font=('calibre', 10, 'bold'))
    gender_lable.place(x = 30,y = 70)
    age_lable = tk.Label(tp, text = "AGE:",font=('calibre', 10, 'bold'))
    age_lable.place(x = 30,y = 110)
    mailid_lable = tk.Label(tp, text = "MAIL.ID:",font=('calibre', 10, 'bold'))
    mailid_lable.place(x = 30,y = 150)
    password_lable = tk.Label(tp, text = "PASSWORD:",font=('calibre', 10, 'bold'))
    password_lable.place(x = 30,y = 190)
    sbmitbtn = tk.Button(tp, text = "Submit",command = submit,bg='black',fg='white',font=('calibre', 10, 'bold'))
    sbmitbtn.place(x=130, y=220)

    a1 = tk.Entry(tp,width = 20)
    a1.place(x = 100, y = 30)
    b2 = tk.Entry(tp,width = 20)
    b2.place(x = 100, y = 70)
    c3 = tk.Entry(tp,width = 20)
    c3.place(x = 100, y = 110)
    d4 = tk.Entry(tp,width = 20)
    d4.place(x = 100, y = 150)
    e5 = tk.Entry(tp,width = 20)
    e5.place(x = 120, y = 190)
        
def login():
    user_id=userid.get()
    passwd=passcode.get()
    
    try:
        command="select passwd from user where mail_id= %s"
        temp=user_id
        Mycursor1.execute(command,(user_id, ))
        record=Mycursor1.fetchall()
        for i in record:
            data=i[0]
        if(data==None):
            messagebox.showinfo("ERROR","Account does not exists")
        elif(data==passwd):
            play()
        else:
            messagebox.showinfo("ERROR","Incorrect password")
    except:
        messagebox.showinfo("ERROR","Enter a valid-id")
        
top = tk.Tk()

top.geometry("400x250")
top.title("Login Page")

Canvas1 = Canvas(top)    
Canvas1.config(bg="#00CED1")
Canvas1.pack(expand=True,fill=BOTH)
 
uname = tk.Label(top, text = "Username",font=('calibre', 10, 'bold'))
uname.place(x = 30,y = 50)  
  
password = tk.Label(top, text = "Password",font=('calibre', 10, 'bold'))
password.place(x = 30, y = 90)
  
userid = tk.Entry(top,width = 20)
userid.place(x = 110, y = 50)
  
passcode = tk.Entry(top, width = 20)
passcode.place(x = 100, y = 90)

login =tk.Button(top, text = "LOGIN",command = login,font=('calibre', 10, 'bold'),bg='black',fg='white')
login.place(x=130, y=130)

newuser= tk.Button(top, text = "NEWUSER",command = new,font=('calibre', 10, 'bold'),bg='black',fg='white')
newuser.place(x=130, y=170)

top.mainloop()
