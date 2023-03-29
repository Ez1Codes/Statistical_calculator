import tkinter as tk
import numpy as np
from tkinter import messagebox
import statistics as st
import random


root = tk.Tk()

# clear the textbox where the data is entered
def clear():
	textbox.delete('1.0', tk.END)

#clear the answer textbpx
def clearans():
	textbox2.configure(state=tk.NORMAL)
	textbox2.delete('1.0', tk.END)
	textbox2.configure(state=tk.DISABLED)


#functions for the various operations 

def mean():
	textbox2.configure(state=tk.NORMAL)
	textbox2.delete('1.0', tk.END)
	strng = textbox.get('1.0', tk.END)
	lst = list(map(float,strng.split()))
	mn = np.mean(lst)
	textbox2.insert('1.0',mn)
	textbox2.configure(state=tk.DISABLED)

def mode():
	textbox2.configure(state=tk.NORMAL)
	textbox2.delete('1.0', tk.END)
	strng = textbox.get('1.0', tk.END)
	lst = list(map(float,strng.split()))
	md = st.mode(lst)
	textbox2.insert('1.0',md)
	textbox2.configure(state=tk.DISABLED)

def variance():
	textbox2.configure(state=tk.NORMAL)
	textbox2.delete('1.0', tk.END)
	strng = textbox.get('1.0', tk.END)
	lst = list(map(float,strng.split()))
	var = st.variance(lst)
	textbox2.insert('1.0',var)
	textbox2.configure(state=tk.DISABLED)

def standard_diviation():
	textbox2.configure(state=tk.NORMAL)
	textbox2.delete('1.0', tk.END)
	strng = textbox.get('1.0', tk.END)
	lst = list(map(float,strng.split()))
	std = st.stdev(lst)
	textbox2.insert('1.0',std)
	textbox2.configure(state=tk.DISABLED)

def wmean():
	textbox2.configure(state=tk.NORMAL)
	textbox2.delete('1.0', tk.END)
	strng = textbox.get('1.0', tk.END)
	data = list(map(float, strng.split()))
	data_range = len(data)
	randlist = []
	wieght = 100
	for i in range(0,data_range):
		n = random.randfloat(1,wieght)
		randlist.append(n)

	w_mean = np.average(data, weights=randlist)
	textbox2.insert('1.0',w_mean)
	textbox2.configure(state=tk.DISABLED)


def median():
	textbox2.configure(state=tk.NORMAL)
	textbox2.delete('1.0', tk.END)
	strng = textbox.get('1.0', tk.END)
	lst = list(map(float,strng.split()))
	med = st.median(lst)
	textbox2.insert('1.0',med)
	textbox2.configure(state=tk.DISABLED)

def Range():
	textbox2.configure(state=tk.NORMAL)
	textbox2.delete('1.0', tk.END)
	strng = textbox.get('1.0', tk.END)
	lst = list(map(float,strng.split()))
	max_num = max(lst)
	min_num = min(lst)
	rng = (max_num - min_num)
	textbox2.insert('1.0',rng)
	textbox2.configure(state=tk.DISABLED)

def quadiv():
	textbox2.configure(state=tk.NORMAL)
	textbox2.delete('1.0', tk.END)
	strng = textbox.get('1.0', tk.END)
	lst = list(map(float,strng.split()))
	Q1 = np.quantile(lst, [0.25])
	Q3 = np.quantile(lst ,[0.75])
	quad = ((Q3-Q1)/2)
	textbox2.insert('1.0',quad)
	textbox2.configure(state=tk.DISABLED)

def meandiv():
	textbox2.configure(state=tk.NORMAL)
	textbox2.delete('1.0', tk.END)
	strng = textbox.get('1.0', tk.END)
	lst = list(map(float,strng.split()))
	res = []
	mn = st.mean(lst)
	for ele in lst:
		res.append(abs(ele - mn)/(len(lst)))
	ans = sum(res)
	textbox2.insert('1.0',ans)
	textbox2.configure(state=tk.DISABLED)

def co_var():
	textbox2.configure(state=tk.NORMAL)
	textbox2.delete('1.0', tk.END)
	strng = textbox.get('1.0', tk.END)
	lst = list(map(float,strng.split()))
	sd = st.stdev(lst)
	mean = st.mean(lst)
	cv = (sd / mean)
	textbox2.insert('1.0',cv)
	textbox2.configure(state=tk.DISABLED)

# size of the applicain window 
root.geometry("500x400")

# title of the applicaiton window 
root.title("Statistics ")

# background of the application window 
root.configure(bg='#b5a6d1')

# lable for the first textbox
label = tk.Label(root, text='Enter data here', font=('arial', 14),bg='#b5a6d1')
label.pack(padx=3)

# initialize the first textbox to accept user input 
textbox = tk.Text(root, height=1.5, font=('Arial', 14))
textbox.pack(padx=10)

# lable for the second textbox
label = tk.Label(root, text='solution', font=('arial', 14),bg='#b5a6d1')
label.pack(padx=3)

# initialize the second textbox to accept user input
textbox2 = tk.Text(root, height=1.5, font=('Arial', 14))
textbox2.pack(padx=10)

# initialize a button frame to contain all the buttons 
buttonFrame = tk.Frame(root)
buttonFrame.columnconfigure(0,weight=1)
buttonFrame.columnconfigure(1,weight=1)
buttonFrame.columnconfigure(2,weight=1)
buttonFrame.configure(bg='#4d6a8a')

#declaration of the buttons and assigning them to the  various functions
btn1 = tk.Button(buttonFrame, text='Mean', font=('Arial', 13), bg='#97e7f1',command=mean)
btn1.grid(row=0, column=0, sticky=tk.W+tk.E)

btn2 = tk.Button(buttonFrame, text='Median', font=('Arial', 13), bg='#97e7f1', command=median)
btn2.grid(row=0, column=1, sticky=tk.W+tk.E)

btn3 = tk.Button(buttonFrame, text='Mode', font=('Arial', 13), bg='#97e7f1',command=mode)
btn3.grid(row=0, column=2, sticky=tk.W+tk.E)

btn4 = tk.Button(buttonFrame, text='Variance', font=('Arial', 13), bg='#97e7f1', command=variance)
btn4.grid(row=1, column=0, sticky=tk.W+tk.E)

btn5 = tk.Button(buttonFrame, text='Standard Diviation', font=('Arial', 13), bg='#97e7f1', command=standard_diviation)
btn5.grid(row=1, column=1, sticky=tk.W+tk.E)

btn6 = tk.Button(buttonFrame, text='Range', font=('Arial', 13), bg='#97e7f1', command=Range)
btn6.grid(row=1, column=2, sticky=tk.W+tk.E)

btn6 = tk.Button(buttonFrame, text='Mean Diviation', font=('Arial', 13), bg='#97e7f1', command=meandiv)
btn6.grid(row=2, column=0, sticky=tk.W+tk.E)

btn6 = tk.Button(buttonFrame, text='Quatile Diviation', font=('Arial', 13), bg='#97e7f1', command=quadiv)
btn6.grid(row=2, column=1, sticky=tk.W+tk.E)

btn6 = tk.Button(buttonFrame, text='Weighted Mean', font=('Arial', 13), bg='#97e7f1', command='')
btn6.grid(row=2, column=2, sticky=tk.W+tk.E)

btn6 = tk.Button(buttonFrame, text='Coefficient Variation', font=('Arial', 13), bg='#97e7f1', command=co_var)
btn6.grid(row=3, column=1, sticky=tk.W+tk.E)

clearbtn = tk.Button(buttonFrame, text='Clear Data', font=('Arial', 13), bg='#ce1313', command=clear)
clearbtn.grid(row=3, column=0, sticky=tk.W+tk.E)

clearbtn2 = tk.Button(buttonFrame, text='Clear Solution', font=('Arial', 13), bg='#ce1313', command=clearans)
clearbtn2.grid(row=3, column=2, sticky=tk.W+tk.E)


buttonFrame.pack(padx=10)


root.mainloop()

