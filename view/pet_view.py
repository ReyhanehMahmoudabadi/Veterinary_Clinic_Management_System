from tkinter import *
from tkinter import ttk, messagebox
from controller.pet_controller import PetController
from datetime import date


class PetView:

    def __init__(self):
        self.controller = PetController()

        self.win = Toplevel()
        self.win.geometry("1150x550")
        self.win.title("Pets")

        # Pet ID
        Label(self.win, text="Pet ID").place(x=30, y=30)
        self.pet_id = StringVar()
        Entry(self.win, textvariable=self.pet_id).place(x=140, y=30)

        # Pet Name
        Label(self.win, text="Pet Name").place(x=30, y=75)
        self.pet_name = StringVar()
        Entry(self.win, textvariable=self.pet_name).place(x=140, y=75)

        # Species
        Label(self.win, text="Species").place(x=30, y=120)
        self.species = StringVar()
        Entry(self.win, textvariable=self.species).place(x=140, y=120)

        # Breed
        Label(self.win, text="Breed").place(x=30, y=165)
        self.breed = StringVar()
        Entry(self.win, textvariable=self.breed).place(x=140, y=165)

        # Gender
        Label(self.win, text="Gender").place(x=30, y=210)
        self.gender = StringVar()
        Entry(self.win, textvariable=self.gender).place(x=140, y=210)

        # Birth Date
        Label(self.win, text="Birth Date").place(x=30, y=255)
        self.birth_date = StringVar()
        Entry(self.win, textvariable=self.birth_date).place(x=140, y=255)

        # Weight
        Label(self.win, text="Weight").place(x=30, y=300)
        self.weight = StringVar()
        Entry(self.win, textvariable=self.weight).place(x=140, y=300)

        # Owner ID
        Label(self.win, text="Owner ID").place(x=30, y=345)
        self.owner_id = StringVar()
        Entry(self.win, textvariable=self.owner_id).place(x=140, y=345)

        # Microchip Number
        Label(self.win, text="Microchip Number").place(x=30, y=390)
        self.microchip_number = StringVar()
        Entry(self.win, textvariable=self.microchip_number).place(x=140, y=390)

        # Table
        self.table = ttk.Treeview(
            self.win,
            show="headings",
            columns=[1, 2, 3, 4, 5, 6, 7, 8,9]
        )
        self.table.place(x=380, y=20, width=740, height=470)

        self.table.column(1, width=65)
        self.table.column(2, width=85)
        self.table.column(3, width=75)
        self.table.column(4, width=75)
        self.table.column(5, width=65)
        self.table.column(6, width=90)
        self.table.column(7, width=65)
        self.table.column(8, width=75)
        self.table.column(9, width=145)

        self.table.heading(1, text="Pet ID")
        self.table.heading(2, text="Pet Name")
        self.table.heading(3, text="Species")
        self.table.heading(4, text="Breed")
        self.table.heading(5, text="Gender")
        self.table.heading(6, text="Birth Date")
        self.table.heading(7, text="Weight")
        self.table.heading(8, text="Owner ID")
        self.table.heading(9, text="Microchip Number")

        self.table.bind("<ButtonRelease>", self.table_click)

        # Save Button
        Button(
            self.win,
            text="Save",
            command=self.save_click
        ).place(x=80, y=480, width=80, height=35)

        self.reset_form()

    # Reset Form and Refresh Table
    def reset_form(self):
        self.pet_id.set("")
        self.pet_name.set("")
        self.species.set("")
        self.breed.set("")
        self.gender.set("")
        self.birth_date.set("")
        self.weight.set("")
        self.owner_id.set("")
        self.microchip_number.set("")

        for item in self.table.get_children():
            self.table.delete(item)

        success, result = self.controller.find_all()

        if success:
            for pet in result:
                self.table.insert("", END, values=pet.to_tuple())
        else:
            messagebox.showerror("Error", result)

    # Save Button Click
    def save_click(self):
        try:
            success, message = self.controller.save(
                self.pet_id.get(),
                self.pet_name.get(),
                self.species.get(),
                self.breed.get(),
                self.gender.get(),
                date.fromisoformat(self.birth_date.get()),
                float(self.weight.get()),
                int(self.owner_id.get()),
                self.microchip_number.get() or None
            )

            if success:
                messagebox.showinfo("Success", message)
                self.reset_form()
            else:
                messagebox.showerror("Error", message)

        except (ValueError, TypeError) as e:
            messagebox.showerror("Error", str(e))

    # Table Click
    def table_click(self, event):
        selected_id = self.table.focus()
        selected_pet = self.table.item(selected_id)["values"]

        if selected_pet:
            self.pet_id.set(selected_pet[0])
            self.pet_name.set(selected_pet[1])
            self.species.set(selected_pet[2])
            self.breed.set(selected_pet[3])
            self.gender.set(selected_pet[4])
            self.birth_date.set(selected_pet[5])
            self.weight.set(selected_pet[6])
            self.owner_id.set(selected_pet[7])
            self.microchip_number.set(selected_pet[8])