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
    text.delete(1.0, END)

def delete():
    lb2.delete(ANCHOR)

def checkout():
    text.insert(END, lb2.get(ANCHOR)+"\n")

def exit1():
    messagebox.showinfo("Gratitude", "Thanks For Shopping !!")
    root.destroy()

root=Tk()
root.title("SHOPPING CART")
root.geometry("1000x500")

l1=Label(root, text="SHOPPING CART", fg="red", font="Cambria 28 bold underline")
l1.place(x=360, y=20)
l2=Label(root, text="Products", font="Cambria 18 bold")
l2.place(x=70, y=80)
l3=Label(root, text="Cart", font="Cambria 18 bold")
l3.place(x=440, y=80)
l4=Label(root, text="Bill", font="Cambria 18 bold")
l4.place(x=740, y=80)

lb1=Listbox(root, height=12, width=20, bg="pink", font=("Cambria", 12))
lb1.place(x=40, y=140)
lb2=Listbox(root, height=12, width=20, bg="cyan", font=("Cambria", 12))
lb2.place(x=330, y=140)

for i in dict1:
    lb1.insert(END, i+" :        "+ '       {}'.format(dict1[i])+"/-")

text=Text(root, bg="gold", width=40, height=20)
text.place(x=630, y=140)

b1=Button(root, text="Go to Cart", bg="orange", command=cart)
b1.place(x=240, y=240)
b2=Button(root, text="Add to Bill", bg="green", fg="white", command=checkout)
b2.place(x=540, y=240)
b3=Button(root, text="Delete", bg="black", fg="white", width=10, command=delete)
b3.place(x=150, y=420)
b4=Button(root, text="Clear All", bg="yellow", width=10, command=clear)
b4.place(x=300, y=420)
b5=Button(root, text="Exit", bg="red", fg="white", width=10, command=exit1)
b5.place(x=470, y=420)

root.mainloop()
