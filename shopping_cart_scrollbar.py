from tkinter import *
from tkinter import messagebox

dict1={'Jeans': 400, 'Shirt': 300, 'Pant': 200, 'Apples': 120, 'guava': 60, 'bananas': 40, 'oranges': 100, 'chiku': 140, 'track suit': 999, 'socks': 30}
dict2={'shoes': 700, 'comb': 20, 'gloves': 150, 'hat': 100, 'deodrant': 70, 'oil': 35, 'shampoo': 49, ' kajal': 49, 'T-shirt': 350, 'high neck': 248}
dict1.update(dict2)

def cart():
    a= lb1.get(ANCHOR)
    lb2.insert(END, a)

def clear():
    lb2.delete(0, END)

def delete():
    lb2.delete(ANCHOR)

def checkout():
    messagebox.showinfo("CHECKOUT", "Thanks For Shopping !!")

root=Tk()
root.title("SHOPPING CART")
root.geometry("600x500")

l1=Label(root, text="SHOPPING CART", fg="red", font="Cambria 28 bold underline")
l1.place(x=160, y=20)
l2=Label(root, text="Products", font="Cambria 18 bold")
l2.place(x=70, y=80)
l3=Label(root, text="Cart", font="Cambria 18 bold")
l3.place(x=440, y=80)

frame=Frame(root)
frame.pack(side="left")
frame2=Frame(root)
frame2.pack(side="right")

lb1=Listbox(frame, height=12, width=20, bg="pink", font=("Cambria", 12))
lb1.pack(side="left")
lb2=Listbox(frame2, height=12, width=20, bg="cyan", font=("Cambria", 12))
lb2.pack(side="right")

s=Scrollbar(frame, orient="vertical")
s.config(command=lb1.yview)
s.pack(side="right", fill="y")

lb1.config(yscrollcommand=s.set)

s1=Scrollbar(frame2, orient="vertical")
s1.config(command=lb2.yview)
s1.pack(side="right", fill="y")

lb2.config(yscrollcommand=s1.set)

for i in dict1:
    lb1.insert(END, i+" :        "+ '       {}'.format(dict1[i])+"/-")

b1=Button(root, text="Go to Cart", bg="orange", command=cart)
b1.place(x=270, y=240)
b2=Button(root, text="Checkout", bg="green", fg="white", command=checkout)
b2.place(x=100, y=420)
b3=Button(root, text="Delete", bg="black", fg="white", command=delete)
b3.place(x=240, y=420)
b4=Button(root, text="Clear All", bg="yellow", command=clear)
b4.place(x=350, y=420)
b5=Button(root, text="Exit", bg="red", fg="white", command=root.destroy)
b5.place(x=470, y=420)

root.mainloop()
