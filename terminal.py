from tkinter import *
import tkinter as tk
import tkinter.messagebox
import tkinter.font as tkFont
from PIL import Image,ImageTk
import os

def run():
	t=Tk()
	t.title('Terminal')
	t.configure(background = 'grey')
	w, h = t.winfo_screenwidth(), t.winfo_screenheight()
	t.geometry("400x150")
	path=os.getcwd()
	data='MiniOS/DRS:> '
	def check():

		def res(wide):
			if wide+50>400:
				line1.place(x=0, y=0, width=wide+50, height=50)
			line2.place(x=0, y=50, width=150, height=50)
			if wide-100>150:
				e.place(x=100, y=50, width=wide-50, height=50)
			if wide>400:
				submit.place(x=0, y=100, width=wide+50, height=50)
			t.geometry("400x150")
			t.geometry("%dx150" % (wide+50))
			t.minsize(400,150)
			t.maxsize(1000,150)
			return

		print(t.winfo_width())
		if e.get()!='':
			if e.get()=='cwd':
				temp=data+''+os.getcwd()
				line1.configure(text=temp)
				res(len(temp)*5)
			elif e.get()=='hostname':
				temp=data+''+os.environ['COMPUTERNAME']
				line1.configure(text=temp)
				res(len(temp)*5)
			elif e.get()=='who':
				temp=data+''+os.getlogin()
				line1.configure(text=temp)
				res(len(temp)*5)
			elif e.get()=='ls':
				temp=data+''+(' , '.join(map(str, (os.listdir(os.getcwd())))))
				line1.configure(text=temp)
				res(len(temp)*5)
			elif e.get()=='shutdown':
				sys.exit()
			else:
				temp=data+"'"+e.get()+"'"+" is not recognized as an internal or external command, operable program or batch file."
				line1.configure(text=temp)
				res(len(temp)*5)
			e.delete(0,'end')

	line1=Label(t, text=data, bg='black', fg='white', font=tkFont.Font(family="Times New Roman", size=10), anchor='w')
	line2=Label(t, text= data, bg='black', fg='white', font=tkFont.Font(family="Times New Roman", size=10), anchor='w')
	e=Entry(t, bg='black', fg='white', font=tkFont.Font(family="Times New Roman", size=10))
	submit=Button(t, text='RUN', command=check, anchor='w')
	line1.place(x=0, y=0, width=400, height=50)
	line2.place(x=0, y=50, width=100, height=50)
	e.place(x=100, y=50, width=300, height=50)
	submit.place(x=0, y=100, width=400, height=50)
	t.mainloop()
		
run()
'''
			elif e.get()=='ls':
				temp=data+''+(' , '.join(map(str, (os.listdir(os.getcwd())))))
				line1.configure(text=temp)
				res(len(temp)*5)
				os.rename(src, dst)
'''