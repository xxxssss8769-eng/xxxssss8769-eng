import tkinter as tk
from tkinter import messagebox
from test1 import WelcomeFrame
from test2 import DoctorFrame
from test3 import PatientsFrame
import saver

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('FaHtest')
        self.geometry('1100x600')
        self.resizable(False, False)

        container = tk.Frame(self)
        container.pack(fill='both', expand=True)

        self.frames = {}
        for name, F in (('welcome', WelcomeFrame), ('doctor', DoctorFrame), ('patients', PatientsFrame)):
            frame = F(container, self)
            self.frames[name] = frame
            frame.grid(row=0, column=0, sticky='nsew')

        self.doctor_info = None
        self.show_frame('welcome')

    def show_frame(self, name):
        frame = self.frames.get(name)
        if not frame:
            return
        frame.tkraise()

    def show_error(self, message: str):
        messagebox.showerror('Error', message)

    def on_doctor_info(self, info: dict):
        # save doctor info then navigate to patients
        self.doctor_info = info
        self.show_frame('patients')

    def on_finish(self, data: dict):
        # combine doctor info and patients data and ask to save
        payload = {'doctor': self.doctor_info or {}, 'patients': data.get('patients', []), 'pats': data.get('pats', []), 'day': data.get('day'), 'details': data.get('details', {})}
        saved = saver.save_summary(payload, as_json=False)
        if saved:
            messagebox.showinfo('Saved', 'Data saved successfully')
            self.quit()

if __name__ == '__main__':
    app = App()
    app.mainloop()

