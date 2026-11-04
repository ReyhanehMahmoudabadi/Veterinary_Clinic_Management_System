from tkinter import *
from view import *


class MainView:

    def owner_click(self):
        owner_ui = OwnerView()

    def vet_click(self):
        vet_ui = VetView()

    def pet_click(self):
        pet_ui = PetView()

    def visit_click(self):
        visit_ui = VisitView()

    def __init__(self):
        self.win = Tk()
        self.win.title("Veterinary Clinic Management System")
        self.win.geometry("350x350")
        self.win.resizable(False, False)

        # Owners Button
        Button(
            self.win,
            text="Owners",
            width=20,
            height=2,
            command=self.owner_click
        ).place(x=95, y=35)

        # Pets Button
        Button(
            self.win,
            text="Pets",
            width=20,
            height=2,
            command=self.pet_click
        ).place(x=95, y=175)

        # Vets Button
        Button(
            self.win,
            text="Vets",
            width=20,
            height=2,
            command=self.vet_click
        ).place(x=95, y=105)

        # Visits Button
        Button(
            self.win,
            text="Visits",
            width=20,
            height=2,
            command=self.visit_click
        ).place(x=95, y=245)

        self.win.mainloop()