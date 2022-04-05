#importing all required libraries
from tkinter import *
import pandas as pd
from tkinter.messagebox import showinfo
from tkinter import ttk
from datetime import datetime
from datetime import date as dt

main_list_path='/Users/krishshah/Desktop/Projects/booklist.csv'#replace with file path of book list when running on your system
issued_list_path='/Users/krishshah/Desktop/Projects/issued.csv'#replace with file path of issued book list when running on your system

#commands to retrive data from CSV files using pandas
df= pd.read_csv(main_list_path)#dataframe of all booklist
df.index+=1
df = df.fillna('-')
booklist=df['title'].tolist()
authorlist=df['author'].tolist()
idf= pd.read_csv(issued_list_path)#dataframe of issued book list
idf.index+=1
issuedbooklist=idf['title'].tolist()
issuedauthorlist=idf['author'].tolist()
issueddate=idf['issue date'].tolist()
issueprice=idf['ppd'].tolist()
curr=datetime.now()
today=str(curr.day)+'/'+str(curr.month)+'/'+str(curr.year)

#create gui window
win=Tk()
def writetofile(write_vals,check):#to rewrite the csv file after modifying values
	if (check ==1):#rewrite booklist with updated values after Add/Deleting book
		global df
		df=pd.DataFrame(write_vals)
		df.index=df.index+1
		df.to_csv('booklist.csv',header = True,index= False)
	if (check==2):
		global idf
		idf=pd.DataFrame(write_vals)
		idf.index=idf.index+1
		idf.to_csv('issued.csv',header=True,index=False)

def addbooks(bn,an):#to add books to the existing database
	bookname=bn
	authorname=an
	flag=0
	for i in range(0,len(booklist)):
		if(bookname.upper()==booklist[i].upper):
			showinfo(title="Add Book",message="Book already exists")
			flag=1
	if(not flag):
		booklist.append(bookname)
		authorlist.append(authorname)
		df_dict={"title": booklist, "author": authorlist}#create updated dictionary that is to be written to file
		writetofile(df_dict,1)
		showinfo(title="Add Book",message="Book has been added")

def add_books_gui():#to create GUI window when add book button is clicked
	global win
	win.destroy()
	win=Tk()
	win.title('Add Book')
	win.geometry("1200x720")
	win.resizable(False,False)
	tit=Label(win,text='Title : ')
	auth=Label(win,text='Author : ')
	bn=StringVar()#create a string type variable to get input from Entry widget and to use get() to get value
	an=StringVar()
	title=Entry(win,width=30,textvariable=bn)
	author=Entry(win,width=30,textvariable=an)
	b1=Button(win,height=2,width=30,text='Add Book',command=lambda:addbooks(bn.get(),an.get()))#lambda function used such that function is called only on button click
	b2=Button(win,height=2,width=30,text='Home',command=home)
	b3=Button(win, height=2,width=30,text=' Close ',command=win.destroy)
	tit.place(x=70,y=90)
	title.place(x=180,y=90)
	auth.place(x=70,y=130)
	author.place(x=180,y=130)
	b1.place(x=540,y=300)
	b2.place(x=540,y=350)
	b3.place(x=540,y=450)
	win.mainloop()

def issuebooks(bnum,bppd):#to issue books and change availability status
	booknumber=int(bnum)
	book_ppd=int(bppd)
	if(booklist[booknumber-1] in issuedbooklist):
		showinfo(title="Issued Book",message="Book has already been issued")
	elif(booknumber <= len(booklist)):
		booknumber=booknumber-1
		issuedbooklist.append(booklist[booknumber])
		issuedauthorlist.append(authorlist[booknumber])
		issueddate.append(today)
		issueprice.append(book_ppd)
		idf_dict={"title": issuedbooklist, "author": issuedauthorlist,"issue date":issueddate, "ppd":issueprice}#create updated dictionary of issued books that is to be written to file
		writetofile(idf_dict,2)
		showinfo(title="Issued Book",message="Book has been issued")
	else:
		showinfo(title="Issued Book",message="No Book with entered book number")
		
def issue_books_gui():#to create GUI window when issue new book button is clicked
	global win
	win.destroy()
	win=Tk()
	win.title('Issue Book')
	win.geometry("1200x720")
	win.resizable(False,False)
	bnum=StringVar()
	bppd=StringVar()
	num=Label(win,text='Enter Book Number to be issued : ')
	number=Entry(win,width=30,textvariable=bnum)
	price=Label(win,text='Enter price of renting book per day : ')
	pricepd=Entry(win,width=30,textvariable=bppd)
	b1=Button(win,height=2,width=30,text='Issue Book',command=lambda:issuebooks(bnum.get(),bppd.get()))
	b2=Button(win,height=2,width=30,text='Home',command=home)
	b3=Button(win, height=2,width=30,text=' Close ',command=win.destroy)
	num.place(x=70,y=90)
	number.place(x=300,y=90)
	price.place(x=70,y=130)
	pricepd.place(x=300,y=130)
	b1.place(x=540,y=300)
	b2.place(x=540,y=350)
	b3.place(x=540,y=450)
	win.mainloop()

def delbooks(bn):#to remove books from the existing database
	breakpoint()
	bookname=bn
	flag=0
	for i in range(1,(len(booklist)+1)):
		if(bookname.upper()==booklist[i-1].upper()):
			booklist.pop(i-1)
			authorlist.pop(i-1)
			df_dict={"title": booklist, "author": authorlist}
			writetofile(df_dict,1)
			flag=1
			showinfo(title="Delete Book",message="Book has been deleted")
			break
	if(not flag):
		showinfo(title="Delete Book",message="Book does not exist")

def delete_books_gui():#to create GUI window when delete book button is clicked
	global win
	win.destroy()
	win=Tk()
	win.title('Delete Book')
	win.geometry("1200x720")
	win.resizable(False,False)
	bn=StringVar()
	tit=Label(win,text='Title of book to be deleted : ')
	title=Entry(win,width=30,textvariable=bn)
	b1=Button(win,height=2,width=30,text='Remove Book',command=lambda:delbooks(bn.get()))#command to be added
	b2=Button(win,height=2,width=30,text='Home',command=home)
	b3=Button(win, height=2,width=30,text=' Close ',command=win.destroy)
	tit.place(x=70,y=90)
	title.place(x=300,y=90)
	b1.place(x=540,y=300)
	b2.place(x=540,y=350)
	b3.place(x=540,y=450)
	win.mainloop()

def payment(date1,p):#to calculate amount
	today=curr.date()
	d1,m1,y1=date1.split('/')
	d1,m1,y1=int(d1),int(m1),int(y1)
	issuedate=dt(y1,m1,d1)
	totaldays=(today-issuedate).days
	cost=int(totaldays)*p
	return(cost)

def returnbooks(bn):#to return books and check amount to be paid
	bookname=bn
	flag=0
	for i in range(1,(len(issuedbooklist)+1)):
		if(bookname.upper()==issuedbooklist[i-1].upper()):
			issuedbooklist.pop(i-1)
			issuedauthorlist.pop(i-1)
			d=issueddate.pop(i-1)
			price=issueprice.pop(i-1)
			string="amount to be paid is"+str(payment(d,price))
			showinfo(title="Return Book",message=string)
			idf_dict={"title": issuedbooklist, "author": issuedauthorlist,"issue date":issueddate, "ppd":issueprice}
			writetofile(idf_dict,2)
			flag=1
			showinfo(title="Return Book",message="Book has been returned")
			break
	if(not flag):
		showinfo(title="Return Book",message="Book has not been issued")

def return_books_gui():#to create GUI window when return book button is clicked
	global win
	win.destroy()
	win=Tk()
	win.title('Return Book')
	win.geometry("1200x720")
	win.resizable(False,False)
	bn=StringVar()
	tit=Label(win,text='Title of book being returned : ')
	title=Entry(win,width=30,textvariable=bn)
	b1=Button(win,height=2,width=30,text='Return Book',command=lambda:returnbooks(bn.get()))#command to be added
	b2=Button(win,height=2,width=30,text='Home',command=home)
	b3=Button(win, height=2,width=30,text=' Close ',command=win.destroy)
	tit.place(x=70,y=90)
	title.place(x=300,y=90)
	b1.place(x=540,y=300)
	b2.place(x=540,y=350)
	b3.place(x=540,y=450)
	win.mainloop()

def search_books_gui():#to create GUI window when search book button is clicked
	global win
	win.destroy()
	win=Tk()
	win.title('Search Book')
	win.geometry("1200x720")
	win.resizable(False,False)
	bn=StringVar()
	tit=Label(win,text='Enter title/part of book title you are looking for : ')
	title=Entry(win,width=30,textvariable=bn)
	b1=Button(win,height=2,width=30,text='Search Book',command=lambda:treeview(3,bn.get()))#command to be added
	b2=Button(win,height=2,width=30,text='Home',command=home)
	b3=Button(win, height=2,width=30,text=' Close ',command=win.destroy)
	tit.place(x=70,y=90)
	title.place(x=400,y=90)
	b1.place(x=540,y=300)
	b2.place(x=540,y=350)
	b3.place(x=540,y=450)
	win.mainloop()

def search_author_gui():#to create GUI window when search author button is clicked
	global win
	win.destroy()
	win=Tk()
	win.title('Search Book')
	win.geometry("1200x720")
	win.resizable(False,False)
	an=StringVar()
	aut=Label(win,text='Enter author you are looking for : ')
	author=Entry(win,width=30,textvariable=an)
	b1=Button(win,height=2,width=30,text='Search Book',command=lambda:treeview(4,an.get()))#command to be added
	b2=Button(win,height=2,width=30,text='Home',command=home)
	b3=Button(win, height=2,width=30,text=' Close ',command=win.destroy)
	aut.place(x=70,y=90)
	author.place(x=400,y=90)
	b1.place(x=540,y=300)
	b2.place(x=540,y=350)
	b3.place(x=540,y=450)
	win.mainloop()

def treeview(c,search="NA"):#to create GUI window when issued/view book button is clicked
	option =c
	global win
	win.destroy()
	win=Tk()
	win.title('View Books')
	win.geometry("1200x720")
	win.resizable(False,False)
	if(c==1):
		columns=('booknumber','title','author')
		tree = ttk.Treeview(win, columns=columns, show='headings',height=35)
		tree.column('booknumber', width=180)
		tree.column('title', width=500)
		tree.column('author', width=500)
		tree.heading('booknumber', text='Book Number')
		tree.heading('title', text='Title')
		tree.heading('author', text='Author')
		for i in range(1,len(booklist)+1):
			tree.insert('',END,values=(i,booklist[i-1],authorlist[i-1]))
		tree.grid(row=0, column=0, sticky='nsew')
		scrollbar = ttk.Scrollbar(win, orient=VERTICAL, command=tree.yview)
		tree.configure(yscroll=scrollbar.set)
		scrollbar.grid(row=0, column=1, sticky='ns')
	if(c==2):
		columns=('booknumber','title','author','date','price')
		tree = ttk.Treeview(win, columns=columns, show='headings',height=35)
		tree.column('booknumber', width=180)
		tree.column('title', width=250)
		tree.column('author', width=250)
		tree.column('date', width=250)
		tree.column('price', width=250)
		tree.heading('booknumber', text='Book Number')
		tree.heading('title', text='Title')
		tree.heading('author', text='Author')
		tree.heading('date', text='Issued Date')
		tree.heading('price', text='Price')
		for i in range(1,len(issueprice)+1):
			tree.insert('',END,values=(i,issuedbooklist[i-1],issuedauthorlist[i-1],issueddate[i-1],issueprice[i-1]))
		tree.grid(row=0, column=0, sticky='nsew')
		scrollbar = ttk.Scrollbar(win, orient=VERTICAL, command=tree.yview)
		tree.configure(yscroll=scrollbar.set)
		scrollbar.grid(row=0, column=1, sticky='ns')	
	if(c==3):
		columns=('booknumber','title','author')
		tree = ttk.Treeview(win, columns=columns, show='headings',height=35)
		tree.column('booknumber', width=180)
		tree.column('title', width=500)
		tree.column('author', width=500)
		tree.heading('booknumber', text='Book Number')
		tree.heading('title', text='Title')
		tree.heading('author', text='Author')
		bookname=search
		flag=0
		for i in range(1,len(booklist)+1):
			if bookname in booklist[i-1]:
				tree.insert('',END,values=(i,booklist[i-1],authorlist[i-1]))
				flag=1
		if(not flag):
			tree.insert('',END,values=('None Found','None Found','None Found'))
		tree.grid(row=0, column=0, sticky='nsew')
		scrollbar = ttk.Scrollbar(win, orient=VERTICAL, command=tree.yview)
		tree.configure(yscroll=scrollbar.set)
		scrollbar.grid(row=0, column=1, sticky='ns')	
	if(c==4):
		columns=('booknumber','title','author')
		tree = ttk.Treeview(win, columns=columns, show='headings',height=35)
		tree.column('booknumber', width=180)
		tree.column('title', width=500)
		tree.column('author', width=500)
		tree.heading('booknumber', text='Book Number')
		tree.heading('title', text='Title')
		tree.heading('author', text='Author')
		authorname=search
		flag=0
		for i in range(1,len(booklist)+1):
			if authorname in authorlist[i-1]:
				tree.insert('',END,values=(i,booklist[i-1],authorlist[i-1]))
				flag=1
		if(not flag):
			tree.insert('',END,values=('None Found','None Found','None Found'))
		tree.grid(row=0, column=0, sticky='nsew')
		scrollbar = ttk.Scrollbar(win, orient=VERTICAL, command=tree.yview)
		tree.configure(yscroll=scrollbar.set)
		scrollbar.grid(row=0, column=1, sticky='ns')	
	canv=Canvas(win,height=100,width=1200)
	b1=Button(canv,height=2,width=30,text='Home',command=home)
	b2=Button(canv, height=2,width=30,text=' Close ',command=win.destroy)
	b1.place(x=100,y=10)
	b2.place(x=600,y=10)
	canv.grid(row=1,column=0,sticky='ns')
	win.mainloop()

def home():#to create main GUI window when program is running
	global win
	win.destroy()
	win=Tk()
	win.title('Library')
	win.geometry("1200x720")
	win.resizable(False,False)
	b1=Button(win, height=2,width=30,text=' Add Book ',command=add_books_gui)
	b2=Button(win, height=2,width=30,text=' Issue New Book ',command=issue_books_gui)
	b3=Button(win, height=2,width=30,text=' Return Book ',command=return_books_gui)
	b4=Button(win, height=2,width=30,text=' View Book ',command=lambda:treeview(1))
	b5=Button(win, height=2,width=30,text=' Issued Book ',command=lambda:treeview(2))
	b6=Button(win, height=2,width=30,text=' Delete Book ',command=delete_books_gui)
	b7=Button(win, height=2,width=30,text=' Search Books',command=search_books_gui)
	b8=Button(win, height=2,width=30,text=' Search Author',command=search_author_gui)
	b9=Button(win, height=2,width=30,text=' Close ',command=win.destroy)
	b1.place(x=540,y=30)
	b2.place(x=540,y=80)
	b3.place(x=540,y=130)
	b4.place(x=540,y=180)
	b5.place(x=540,y=230)
	b6.place(x=540,y=280)
	b7.place(x=540,y=330)
	b8.place(x=540,y=380)
	b9.place(x=540,y=430)
	win.mainloop()

home()
win.mainloop()