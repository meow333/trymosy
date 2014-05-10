from Tkinter import *
flag=0
def hb():
   global u, p, flag, top, root
   ug=u.get()
   pg=p.get()
   top.destroy()
   if ug=='u' and pg=='p':
      root=Tk()
      flag=1
      Label(root, text ="yes!").grid(row=1, column=0)
      Button(root, text="back" ,command=st).grid(row=2, column=1)
      root.mainloop()
   else:
      root=Tk()
      flag=1
      Label(root, text ="no!").grid(row=1, column=0)
      Button(root, text="back" ,command=st).grid(row=2, column=1)
      root.mainloop()
   

def st():
   global u, p, flag, root, top
   if flag==1:
      root.destroy()
   top = Tk()
   flag=0
   Label(top, text ="Username").grid(row=0, column=0)
   u=Entry(top)
   u.grid(row=0, column=1)
   Label(top, text ="Password").grid(row=1, column=0)
   p=Entry(top)
   p.grid(row=1, column=1)
   Button(top, text="submit" ,command=hb).grid(row=2, column=1)
   top.mainloop()
   

st()
