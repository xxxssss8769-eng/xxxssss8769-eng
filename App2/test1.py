from tkinter import Frame, Canvas, Label, Button, RAISED

class WelcomeFrame(Frame):
    def __init__(self, parent, controller, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.controller = controller
        self.configure(width=1100, height=600)

        # background art (kept simple)
        art = Canvas(self, width=1100, height=600)
        art.create_rectangle(0, 0, 300, 600, fill='green')
        art.pack(fill='both', expand=True)

        # welcome text
        lbl_title = Label(self, text='Welcome', font=('', 24), bg='green', fg='white')
        lbl_title.place(x=120, y=80)

        lbl_info1 = Label(self, text='Hi, this program is designed for doctors or secretary', font=('', 14), bg='green', fg='white')
        lbl_info1.place(x=350, y=60)

        lbl_info2 = Label(self, text='to keep patients records in a modern, and secure way', font=('', 14), bg='green', fg='white')
        lbl_info2.place(x=350, y=90)

        lbl_info3 = Label(self, text='If you are ready to go ahead, please click Next', font=('', 14), bg='green', fg='white')
        lbl_info3.place(x=350, y=400)

        btn_next = Button(self, text='Next', relief=RAISED, bd=4, font=('', 14), command=lambda: controller.show_frame('doctor'))
        btn_next.place(x=900, y=500)

