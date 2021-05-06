#code to generate a strong password from keywords
#keywords: noun, word, number(date)
#options: sentence, jumbled(put all into a list and randomize), or just random with words, chars etc
#strong passwords contain: uppercase, lowercase, numbers, special characters, 8 chars or more  
#special characters: !@#$?*

import random
import tkinter as tk
from tkinter import *

window = tk.Tk() #open window
window.configure(bg = 'pink')
window.title('Password Generator')
#window.geometry("600x400") #size of window

#variables for entries
noun_var = tk.StringVar()
word_var = tk.StringVar()
num_var = tk.StringVar()


#convert from list to string 
def listToString(l):
	str1 = ""
	for item in l:
		str1 += item

	return str1

#convert a letter to upper case 
def randomUpper(s):
	strLength = len(s)
	randomIndex = random.randint(0, strLength-1)
	letter = s[randomIndex]
	s = s[:randomIndex] + letter.upper() + s[randomIndex + 1: ]
	return s

#generates the password
def getPass(noun, word, num):
	#list of special characters 
	specialC = ['!', '@', '#', '$', '?', '*']

	noun = randomUpper(noun)
	word = randomUpper(word)
	specialChar =  random.choice(specialC)

	#randomize order of words 
	password = [noun, word, num, specialChar]
	random.shuffle(password)
	index = random.randint(1,3)
	password.insert(index, '-')
	password = listToString(password)
	return password


#function to get variables 
def submit():
	noun = noun_var.get()
	word = word_var.get()
	num = num_var.get()

	finalPass = getPass(noun, word, num)
	generatedPassLbl.config(text = finalPass)

	print("Password: " + finalPass) #for debugging purposes

	
	noun_var.set(noun)  
	word_var.set(word)
	num_var.set(num)

def reset():
	noun_var.set("")  
	word_var.set("")
	num_var.set("")



#labels -- labels for each section 
instructions = Label(window, text="Instructions: Enter a noun, a random word, and a number to generate a password! ", 
	fg='black', font=("Helvetica", 16))
instructions.pack()

entryFrame = Frame(window)
entryFrame.pack(pady=20)

nounLbl=Label(entryFrame, text="Noun:", fg='black', font=("Helvetica", 16))
nounLbl.grid(row = 0, column = 0, padx = 20)

wordLbl=Label(entryFrame, text="Word:", fg='black', font=("Helvetica", 16))
wordLbl.grid(row = 1, column = 0, padx = 20 )

numLbl=Label(entryFrame, text="Number:", fg='black', font=("Helvetica", 16))
numLbl.grid(row = 2, column = 0, padx = 20 )

#button
btn = Button(window, text="Generate Password!", fg='black', command = submit)
btn.pack(pady = 20)

reset = Button(window, text="Reset Inputs", fg='black', command = reset)
reset.pack(pady = 20)

generatedPassLbl=Label(window, text="", fg='black', font=("Helvetica", 16))
generatedPassLbl.pack(pady = 20)


#entry -- where user will enter their words  
nounEntry=Entry(entryFrame, textvariable = noun_var, bd = 3)
nounEntry.grid(row = 0, column = 1, padx = 10)

wordEntry=Entry(entryFrame, textvariable = word_var, bd = 3)
wordEntry.grid(row = 1, column = 1, padx = 10)

numEntry=Entry(entryFrame, textvariable = num_var, bd = 3)
numEntry.grid(row = 2, column = 1, padx = 10)


#this is to remove the white background on all the text 
widget_list = [instructions, entryFrame, nounLbl, wordLbl, numLbl, btn, generatedPassLbl,
nounEntry, wordEntry, numEntry]
for wid in widget_list:
	wid.configure(bg = 'pink')


window.mainloop()

