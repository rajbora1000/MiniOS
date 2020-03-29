# importing Tkinter and math 
from tkinter import *
import math 

# calc class 
class calc: 
	

	def getandreplace(self): 

		"""replace x with * and ÷ with /"""
		self.expression = self.e.get() 
		self.newtext=self.expression.replace('/','/') 
		self.newtext=self.newtext.replace('x','*') 


	def equals(self): 
		"""when the equal button is pressed"""
		self.getandreplace() 
		try: 
			# evaluate the expression using the eval function 
			self.value= eval(self.newtext) 
		except SyntaxError or NameError: 
			self.e.delete(0,END) 
			self.e.insert(0,'Invalid Input!') 
		else: 
			self.e.delete(0,END) 
			self.e.insert(0,self.value) 

	def squareroot(self): 
		"""squareroot method"""
		self.getandreplace() 
		try: 
			# evaluate the expression using the eval function 
			self.value= eval(self.newtext) 
		except SyntaxError or NameError: 
			self.e.delete(0,END) 
			self.e.insert(0,'Invalid Input!') 
		else: 
			self.sqrtval=math.sqrt(self.value) 
			self.e.delete(0,END) 
			self.e.insert(0,self.sqrtval) 

	def square(self): 
		"""square method"""
		self.getandreplace() 
		try: 
			#evaluate the expression using the eval function 
			self.value= eval(self.newtext) 
		except SyntaxError or NameError: 
			self.e.delete(0,END) 
			self.e.insert(0,'Invalid Input!') 
		else: 
			self.sqval=math.pow(self.value,2) 
			self.e.delete(0,END) 
			self.e.insert(0,self.sqval) 

	def clearall(self): 
			"""when clear button is pressed,clears the text input area"""
			self.e.delete(0,END) 

	def clear1(self): 
			self.txt=self.e.get()[:-1] 
			self.e.delete(0,END) 
			self.e.insert(0,self.txt) 

	def action(self,argi): 
			"""pressed button's value is inserted into the end of the text area"""
			self.e.insert(END,argi) 

	def __init__(self):
		root = Tk()
		"""Constructor method"""
		root.title('Calulator') 
		root.geometry() 
		self.e = Entry( root) 
		self.e.grid(row=0,column=0,columnspan=6,pady=3) 
		self.e.focus_set() #Sets focus on the input text area 

		# Generating Buttons 
		Button( root,text="=",width=11,height=3,  
			 command=lambda:self.equals()).grid( 
								row=4, column=4,columnspan=2) 

		Button( root,text='AC',width=5,height=3, 
					    
		command=lambda:self.clearall()).grid(row=1, column=4) 

		Button( root,text='C',width=5,height=3, 
			   
			command=lambda:self.clear1()).grid(row=1, column=5) 

		Button( root,text="+",width=5,height=3, 
			   
			command=lambda:self.action('+')).grid(row=4, column=3) 

		Button( root,text="x",width=5,height=3, 
				   
				command=lambda:self.action('x')).grid(row=2, column=3) 

		Button( root,text="-",width=5,height=3, 
				   
				command=lambda:self.action('-')).grid(row=3, column=3) 

		Button( root,text="÷",width=5,height=3, 
			   
			command=lambda:self.action('/')).grid(row=1, column=3) 

		Button( root,text="%",width=5,height=3, 
			   
			command=lambda:self.action('%')).grid(row=4, column=2) 

		Button( root,text="7",width=5,height=3, 
			   
			command=lambda:self.action('7')).grid(row=1, column=0) 

		Button( root,text="8",width=5,height=3, 
			   
			command=lambda:self.action(8)).grid(row=1, column=1) 

		Button( root,text="9",width=5,height=3, 
			   
			command=lambda:self.action(9)).grid(row=1, column=2) 

		Button( root,text="4",width=5,height=3, 
			   
			command=lambda:self.action(4)).grid(row=2, column=0) 

		Button( root,text="5",width=5,height=3, 
			   
			command=lambda:self.action(5)).grid(row=2, column=1) 

		Button( root,text="6",width=5,height=3, 
			   
			command=lambda:self.action(6)).grid(row=2, column=2) 

		Button( root,text="1",width=5,height=3, 
			   
			command=lambda:self.action(1)).grid(row=3, column=0) 

		Button( root,text="2",width=5,height=3, 
			   
			command=lambda:self.action(2)).grid(row=3, column=1) 

		Button( root,text="3",width=5,height=3, 
			   
			command=lambda:self.action(3)).grid(row=3, column=2) 

		Button( root,text="0",width=5,height=3, 
			   
			command=lambda:self.action(0)).grid(row=4, column=0) 

		Button( root,text=".",width=5,height=3, 
			   
			command=lambda:self.action('.')).grid(row=4, column=1) 

		Button( root,text="(",width=5,height=3, 
			   
			command=lambda:self.action('(')).grid(row=2, column=4) 

		Button( root,text=")",width=5,height=3, 
			  
			command=lambda:self.action(')')).grid(row=2, column=5) 

		Button( root,text="?",width=5,height=3, 
			  
			command=lambda:self.squareroot()).grid(row=3, column=4) 

		Button( root,text="x²",width=5,height=3, 
			  
			command=lambda:self.square()).grid(row=3, column=5) 
#------------------------------------------------------------------------------