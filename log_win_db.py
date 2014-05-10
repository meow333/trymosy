from Tkinter import *

from sqlite3 import dbapi2 as sqlite
login=sqlite.connect("dataholder.sqlite")
l=login.cursor()

t=("Consumer ID", "Password", "First name", "Middle name", "Last name", "Date of Birth", "Email", "Phone", "City", "Nation", "Address", "Credit card number", "Name on credit card", "Bank name", " ")

flag=0

def hb():
   global u, p, top, root, flag
   ug=int(u.get())
   pg=int(p.get())
   l.execute("select * from consumer")
   c=0
   for i in l:
       if ug == int(i[0]) and pg == int(i[1]):
          wc(i[0])
          c=c+1
   if c==0:
      root=Tk()
      cl(flag)
      flag=2
      Label(root, text ="wrong username or password!").grid(row=1, column=0)
      Button(root, text="back" ,command=st).grid(row=2, column=1)
      root.mainloop()
      
def st():
   global u, p, root, top, flag
   top = Tk()
   top.title("Login")
   cl(flag)
   flag=1
   Label(top, text ="Login today and Start bidding!", width=40,bg='Red', fg="white",).grid(row=0, column=0, columnspan=2)
   Label(top, text ="Username",width=20).grid(row=6, column=0)
   u=Entry(top)
   u.grid(row=6, column=1)
   Label(top, text ="Password",width=20).grid(row=7, column=0)
   p=Entry(top)
   p.grid(row=7, column=1)
   Button(top, text="SUBMIT" , width=40, command=hb,bg='blue', fg="white",).grid(row=8, column=0,columnspan=2)
   Button(top, text="New to AuctionWorld! Sart Here!" ,bg='yellow', width=40, command=newuserui).grid(row=9, column=0,columnspan=2)
   top.mainloop()

def cl(f):
   global flag
   if f==1:
      top.destroy()
   elif f==2:
      root.destroy()
   elif f==3:
      page.destroy()
   elif f==4:
       new.destroy()
       
def wc(c):
   global top, page, flag
   page=Tk()
   page.title("Consumer")
   cl(flag)
   flag=3
   l.execute("select * from consumer")
   for i in l:
      if c==i[0]:
         Label(page, text="Welcome back "+ i[2] + ' !',bg="white", width=30,).grid(row=0, column=0)
         Label(page, text=" ", width=30,).grid(row=1, column=0)
         Label(page, text="Your Details",bg='blue', fg="white", relief=RAISED, width=30,).grid(row=2, column=0)
         Label(page, text="Best Selling",bg='black', fg="white", relief=RAISED, width=30,).grid(row=20, column=0)
##         pbest() 
         Label(page, text="Most Bidded",bg='black', fg="white", relief=RAISED, width=30,).grid(row=20, column=1)
##         pmost()
         Label(page, text="Popular in " + str(i[8]),bg='black', fg="white", relief=RAISED, width=30,).grid(row=20, column=2)
##         ploc(i[0])
         Label(page, text="Popular among people like you",bg='black', fg="white", relief=RAISED, width=30,).grid(row=20, column=3)
##         page(i[0])
         Label(page, text="Products bidded by you ",bg='black', fg="white", relief=RAISED, width=90).grid(row=0, column=1,columnspan=3)
##         pyou(i[0])
         for j in range(14):
             Label(page, text=t[j]+": "+str(i[j]), width=30, bg='sky blue', anchor=W).grid(row=j+4, column=0)
   Button(page, text="Logout" , bg="orange" ,command=st, width=30).grid(row=1, column=0)
   page.mainloop()

##def ploc():
##
   
def newuserui():
   global new, flag, accept, t
   accept=['']*14
   new=Tk()
   new.title("New User")
   cl(flag)
   flag=4
   l.execute("select max(c_id) from consumer")
   for i in l:
       accept[0]=i[0]+1       
   Label(new, text="Register yourself with us", bg="Red", fg= "white", width=40).grid(row=0, column=0, columnspan=2)
   Label(new, text="Consumer ID", width=20, anchor=W).grid(row=1, column=0)
   Label(new, text=accept[0], width=20).grid(row=1, column=1)
   for i in range(1,14):
        Label(new,width=20,text=t[i], anchor=W).grid(row=i+2,column=0)
        accept[i]=Entry(new)
        accept[i].grid(row=i+2, column=1)
   Button(new, text="Submit" , bg="green" ,width=40, command=newsubmit).grid(row=20, column=0, columnspan=2)
   Button(new, text="Login to your account" , bg="orange" ,width=40, command=st).grid(row=21, column=0, columnspan=2)
   new.mainloop()

def newsubmit():
   global new, accept, t, l
   x=['']*14
   x[0]=accept[0]
   for i in range(1,14):
       x[i]=accept[i].get()
       print t[i], ":", x[i]
   sql="insert into consumer values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (x[0],x[1],x[2],x[3],x[4],x[5],x[6],x[7],x[8],x[9],x[10],x[11],x[12],x[13],)
   l.execute(sql)
   login.commit()
   showdb()
   Label(new, width=20, text='Success!').pack()

def showdb():
    global t, l
    l.execute("select * from consumer")
    for i in l:
        print "========================"
        for j in range(15):
            print t[j], ":", i[j]
        
showdb()
st()


