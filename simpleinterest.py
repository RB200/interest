from tkinter import *


def calculate_interest():
    p = float(principal_input.get())
    r = float(rate_input.get())
    t = float(time_input.get())

    i = (p * r * t) / 100
    interest = round(i,2)

    result_label.destroy()

    message = f'The interest will be {i} over {t} at a rate of {r}.'

    output = Label(result_frame, text=message, bg='lightblue', font=('Calibri',12), width=100, bd=1)
    output.place(x=300,y=300)
    output.pack()
window = Tk()

window.title('Interest Calculator')
window.geometry('800x800')
window.config(bg='lightblue')

heading_label = Label(window,text='Simple Interest Calculator', font=('Calibri', 12), bg='red', width=25, bd=1)
heading_label.place(x=25,y=25)

principal = Label(window,text='Principal', font=('Calibri',12), width=25, bd=1)
principal.place(x=25,y=75)

principal_input = Entry(window,text='', font=('Calibri',12), width=25, fg='black', bg='green', bd=1)
principal_input.place(x=25, y=100)

rate = Label(window,text='Rate', font=('Calibri',12), width=25, bg='green', bd=1)
rate.place(x=225, y=75)

rate_input = Entry(window,text='', font=('Calibri',12), width=25, fg='black',bg='lightblue', bd=1)
rate_input.place(x=225,y=100)

time = Label(window,text='Time', font=('Calibri', 12), width=25, bd=1)
time.place(x=425, y=75 )

time_input = Entry(window,text='', font=('Calibri',12), fg='black',bg='lightblue',width=25, bd=1)
time_input.place(x= 425,y=100)

submit = Button(window, text='Calculate', fg='black',bg='lightblue', bd=4, width=50, command=calculate_interest)
submit.place(x=75,y=200)

result_frame = LabelFrame(window, text='Result:', bg='lightblue',font=('Calibri',12), bd=1)
result_frame.pack(padx=20, pady=20) 
result_frame.place(x=20,y=300)

result_label = Label(result_frame, text=' ', bg='lightblue',font=('Calibri',12), width=45, bd=1)
result_label.place(x=20,y=20)
result_label.pack()

window.mainloop()