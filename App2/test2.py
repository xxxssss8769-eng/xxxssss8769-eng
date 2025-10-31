from tkinter import Frame, Label, Entry, Button, RAISED

class DoctorFrame(Frame):
    def __init__(self, parent, controller, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.controller = controller
        self.configure(width=1100, height=600)

        # left green panel
        Label(self, bg='green').place(x=0, y=0, width=300, height=600)

        Label(self, text='Please fill it with a doctor or secretary', font=('', 20), bg='green', fg='white', pady=5, padx=5).place(x=350, y=20)

        Label(self, text='Doctor name: ', font=('', 16)).place(x=150, y=150)
        self.entr1 = Entry(self, font=('Ink Free', 16), bg='white', fg='black')
        self.entr1.place(x=310, y=150)

        Label(self, text='The clinic     : ', font=('', 16)).place(x=150, y=200)
        self.entr2 = Entry(self, font=('Ink Free', 16), bg='white', fg='black')
        self.entr2.place(x=310, y=200)

        Label(self, text='The number  : ', font=('', 16)).place(x=150, y=250)
        self.entr3 = Entry(self, font=('Ink Free', 16), bg='white', fg='black')
        self.entr3.place(x=310, y=250)

        btn_next = Button(self, text='Next', relief=RAISED, bd=4, font=('', 16), command=self.on_next)
        btn_next.place(x=900, y=500)

        Label(self, text='special thank for fahd mahfouz', font=('Ink Free', 14), bg='green', fg='white').place(x=305, y=565)

    def on_next(self):
        doctor = self.entr1.get().strip()
        clinic = self.entr2.get().strip()
        number = self.entr3.get().strip()
        # basic validation
        if not doctor:
            # allow controller to show an error
            self.controller.show_error('Doctor name is required')
            return
        # pass info to controller
        self.controller.on_doctor_info({'doctor': doctor, 'clinic': clinic, 'number': number})
