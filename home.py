from tkinter import *
import tkinter as tk
import tkinter.messagebox
import tkinter.font as tkFont
from PIL import Image,ImageTk
import sys
import time
from datetime import date

time1 = ''
def run_home(user):

	t=tk.Tk()
	t.title('HOME')
	t.configure(background = 'grey')
	w, h = t.winfo_screenwidth(), t.winfo_screenheight()
	t.geometry("1200x700")
	t.minsize(1000,600)
	t.resizable(0, 0)

	if 1==1:
		t.maxsize(1000, 600)
		def tick():
		    global time1
		    time2 = time.strftime('%H:%M:%S')
		    if time2 != time1:
		        time1 = time2
		        clock.config(text=time2)
		    clock.after(200, tick)
		
		clock = Label(t, font=('times', 20, 'bold'), bg='grey')
		clock.place(x=750, y=0, width=150, height=50)
		date1=Label(t,text=date.today(), font=('times', 20, 'bold'), bg='grey')
		date1.place(x=600, y=0, width=150, height=50)
		tick()

		def image_update():
			return

		def run_notepad():
			import notepad as tty
			notepad = tty.Notepad(width=600,height=400) 
			notepad.run() 

		t.load = Image.open('Notepadicon.png')
		t.load = t.load.resize((70,70), Image.ANTIALIAS)
		t.photo = ImageTk.PhotoImage(t.load,master=t)
		t.img = Button(t, image=t.photo,command=run_notepad)
		t.img.image = t.photo
		t.img.place(x=10, y=60, width=70, height=70)

		def run_calc():
			import calc as tty 
			obj=tty.calc()

		t.load1 = Image.open('Calculator.png')
		t.load1 = t.load1.resize((70,70), Image.ANTIALIAS)
		t.photo1 = ImageTk.PhotoImage(t.load1,master=t)
		t.img1 = Button(t, image=t.photo1,command=run_calc)
		t.img1.image = t.photo1
		t.img1.place(x=10, y=150, width=70, height=70)

		def run_file():
			import subprocess
			subprocess.Popen('explorer "C:\"')
			#import filemanager as tty
			#ob=tty.filemanager()

		t.load2 = Image.open('file.png')
		t.load2 = t.load2.resize((70,70), Image.ANTIALIAS)
		t.photo2 = ImageTk.PhotoImage(t.load2,master=t)
		t.img2 = Button(t, image=t.photo2,command=run_file)
		t.img2.image = t.photo2
		t.img2.place(x=10, y=250, width=70, height=70)


		def run_terminal():
			import terminal as tty
			ob=tty.run()

		t.load3 = Image.open('terminal.png')
		t.load3 = t.load3.resize((70,70), Image.ANTIALIAS)
		t.photo3 = ImageTk.PhotoImage(t.load3,master=t)
		t.img3 = Button(t, image=t.photo3,command=run_terminal)
		t.img3.image = t.photo3
		t.img3.place(x=10, y=350, width=70, height=70)


		def run_music():
			import music as tty
			ob=tty.MusicPlayer()

		t.load4 = Image.open('music.png')
		t.load4 = t.load4.resize((70,70), Image.ANTIALIAS)
		t.photo4 = ImageTk.PhotoImage(t.load4,master=t)
		t.img4 = Button(t, image=t.photo4,command=run_music)
		t.img4.image = t.photo4
		t.img4.place(x=10, y=450, width=70, height=70)


	if user=='root':
		t.maxsize(1200,700)
		def run_sjf():
			import sjf as tty
			ob=tty.shortestjob(t)
		t.load5 = Image.open('process.jpg')
		t.load5 = t.load5.resize((70,70), Image.ANTIALIAS)
		t.photo5 = ImageTk.PhotoImage(t.load5,master=t)
		t.img5 = Button(t, image=t.photo5,command=run_sjf)
		t.img5.image = t.photo5
		t.img5.place(x=1120, y=150, width=70, height=70)

		def run_best():
			import bestfit as tty
			ob=tty.memory()

		t.load6 = Image.open('memory.png')
		t.load6 = t.load6.resize((70,70), Image.ANTIALIAS)
		t.photo6 = ImageTk.PhotoImage(t.load6,master=t)
		t.img6 = Button(t, image=t.photo6,command=run_best)
		t.img6.image = t.photo6
		t.img6.place(x=1120, y=250, width=70, height=70)

		def run_filemgmt():
			import filemgmt as tty
			ob=tty.run_file()

		t.load8 = Image.open('filemgmt.png')
		t.load8 = t.load8.resize((70,70), Image.ANTIALIAS)
		t.photo8 = ImageTk.PhotoImage(t.load8,master=t)
		t.img8 = Button(t, image=t.photo8,command=run_filemgmt)
		t.img8.image = t.photo8
		t.img8.place(x=1120, y=350, width=70, height=70)


	def shut():
		sys.exit()

	t.load9 = Image.open('power.png')
	t.load9 = t.load9.resize((70,70), Image.ANTIALIAS)
	t.photo9 = ImageTk.PhotoImage(t.load9,master=t)
	t.img9 = Button(t, image=t.photo9, command=shut)
	t.img9.image = t.photo9
	t.img9.place(x=940, y=0, width=50, height=50)
	t.mainloop()

#run_home('root')