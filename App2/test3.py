import datetime
from tkinter import Frame, Label, Entry, Button, Listbox, END, Toplevel, messagebox

class PatientsFrame(Frame):
    def __init__(self, parent, controller, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.controller = controller

        self.configure(width=1100, height=600)
        self.deg = {}   # map name -> age
        self.deg2 = {}  # map name -> notes

        Label(self, text='patient name : ', font=('', 14), bg='green', fg='white').place(relx=0, rely=0.1)
        Label(self, text='patient old    : ', font=('', 14), bg='green', fg='white').place(relx=0, rely=0.2)
        Label(self, text='notes            : ', font=('', 14), bg='green', fg='white').place(relx=0, rely=0.3)

        self.entr1 = Entry(self, font=('', 10,), fg='green')
        self.entr1.place(relx=0.12, rely=0.1)
        self.entr2 = Entry(self, font=('', 10,), fg='green')
        self.entr2.place(relx=0.12, rely=0.2)
        self.entr3 = Entry(self, font=('', 10,), fg='green')
        self.entr3.place(relx=0.12, rely=0.3)

        btn_next = Button(self, text='next patient', bg='green', relief='raised', pady=5, padx=5, fg='white', command=self.add_patient)
        btn_next.place(relx=0.18, rely=0.4)

        self.patientlist = Listbox(self, height=20)
        self.patientlist.place(relx=0.84, rely=0.05)

        self.patlist = Listbox(self, height=10)
        self.patlist.place(relx=0.5, rely=0.05)

        Button(self, text='More info', bg='green', fg='white', command=self.moreinfo).place(relx=0.75, rely=0.1)
        Button(self, text='finish the day', command=self.finish, bg='red', fg='white').place(relx=0.91, rely=0.93)

        self.day = datetime.date.today()
        Label(self, text=('The Date: ' + str(self.day)), font=('', 14), bg='green', fg='white').place(relx=0, rely=0.9)

    def add_patient(self):
        name = self.entr1.get().strip()
        age = self.entr2.get().strip()
        notes = self.entr3.get().strip()
        if not name:
            self.controller.show_error('Patient name is required')
            return
        summary = f'The Name: {name} | The Old: {age} | Notes: {notes}|______________|'
        self.patientlist.insert(END, name)
        self.patlist.insert(END, summary)
        self.entr1.delete(0, END)
        self.entr2.delete(0, END)
        self.entr3.delete(0, END)
        self.deg[name] = age
        self.deg2[name] = notes

    def finish(self):
        if messagebox.askokcancel(title='info', message='Do you want finish the day ?'):
            patients = self.patientlist.get(0, END)
            pats = self.patlist.get(0, END)
            # hand off to controller to save
            self.controller.on_finish({'patients': list(patients), 'pats': list(pats), 'day': self.day, 'details': {'age': self.deg, 'notes': self.deg2}})

    def moreinfo(self):
        # simple input dialog using a Toplevel (do not create a second Tk root)
        top = Toplevel(self)
        top.geometry('300x120')
        top.resizable(False, False)
        Label(top, text='Enter The Name:').place(relx=0.05, rely=0.15)
        entr4 = Entry(top)
        entr4.place(relx=0.5, rely=0.15)
        def inf():
            ga = entr4.get().strip()
            messagebox.showinfo(title=ga or 'Info', message='Old: ' + str(self.deg.get(ga)) + '\nNotes: ' + str(self.deg2.get(ga)))
            top.destroy()
        Button(top, text='check', command=inf).place(relx=0.4, rely=0.6)

    # helpers for controller
    def get_summary(self):
        return {'patients': list(self.patientlist.get(0, END)), 'pats': list(self.patlist.get(0, END)), 'day': self.day, 'details': {'age': self.deg, 'notes': self.deg2}}
