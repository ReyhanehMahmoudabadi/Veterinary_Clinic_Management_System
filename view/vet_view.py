from tkinter import *
from tkinter import ttk, messagebox

from controller.vet_controller import VetController


class VetView:

    def __init__(self):
        self.controller = VetController()
        self.win = Toplevel()
        self.win.geometry("1150x550")
        self.win.title("Vets")

        # Vet ID
        Label(self.win, text="Vet ID").place(x=30, y=30)
        self.vet_id = StringVar()
        Entry(self.win, textvariable=self.vet_id).place(x=140, y=30)

        # Name
        Label(self.win, text="Name").place(x=30, y=75)
        self.name = StringVar()
        Entry(self.win, textvariable=self.name).place(x=140, y=75)

        # Family
        Label(self.win, text="Family").place(x=30, y=120)
        self.family = StringVar()
        Entry(self.win, textvariable=self.family).place(x=140, y=120)

        # National ID
        Label(self.win, text="National ID").place(x=30, y=165)
        self.national_id = StringVar()
        Entry(self.win, textvariable=self.national_id).place(x=140, y=165)

        # Phone
        Label(self.win, text="Phone").place(x=30, y=210)
        self.phone = StringVar()
        Entry(self.win, textvariable=self.phone).place(x=140, y=210)

        # Specialization
        Label(self.win, text="Specialization").place(x=30, y=255)
        self.specialization = StringVar()
        Entry(self.win, textvariable=self.specialization).place(x=140, y=255)

        # License Number
        Label(self.win, text="License Number").place(x=30, y=300)
        self.license_number = StringVar()
        Entry(self.win, textvariable=self.license_number).place(x=140, y=300)

        # Email
        Label(self.win, text="Email").place(x=30, y=345)
        self.email = StringVar()
        Entry(self.win, textvariable=self.email).place(x=140, y=345)

        # Table
        self.table = ttk.Treeview(
            self.win,
            show="headings",
            columns=[1, 2, 3, 4, 5, 6, 7, 8]
        )
        self.table.place(x=380, y=20,width=740,height=470)

        self.table.column(1, width=75)
        self.table.column(2, width=75)
        self.table.column(3, width=90)
        self.table.column(4, width=90)
        self.table.column(5, width=100)
        self.table.column(6, width=70)
        self.table.column(7, width=110)
        self.table.column(8, width=130)

        self.table.heading(1, text="Name")
        self.table.heading(2, text="Family")
        self.table.heading(3, text="National ID")
        self.table.heading(4, text="Phone")
        self.table.heading(5, text="Email")
        self.table.heading(6, text="Vet ID")
        self.table.heading(7, text="Specialization")
        self.table.heading(8, text="License Number")

        self.table.bind("<ButtonRelease>", self.table_click)

        Button(
            self.win,
            text="Save",
            command=self.save_click
        ).place(x=80, y=480,width=80,height=35)

        self.reset_form()
        self.win.mainloop()

    # Reset Form and Refresh Table
    def reset_form(self):
        self.vet_id.set("")
        self.name.set("")
        self.family.set("")
        self.national_id.set("")
        self.phone.set("")
        self.specialization.set("")
        self.license_number.set("")
        self.email.set("")

        # Clear Table
        for item in self.table.get_children():
            self.table.delete(item)

        # Set All Vets On Table
        for vet in self.controller.find_all()[1]:
            self.table.insert("", END, values=vet.to_tuple())

    # Save Button Click
    def save_click(self):
        success, message = self.controller.save(
            self.name.get(),
            self.family.get(),
            self.national_id.get(),
            self.phone.get(),
            self.specialization.get(),
            self.license_number.get(),
            int(self.vet_id.get()),
            self.email.get() or None
        )

        if success:
            messagebox.showinfo("Success", message)
            self.reset_form()
        else:
            messagebox.showerror("Error", message)

    # Table Click
    def table_click(self, event):
        selected_vet_id = self.table.focus()
        selected_vet = self.table.item(selected_vet_id)["values"]

        if selected_vet:
            self.name.set(selected_vet[0])
            self.family.set(selected_vet[1])
            self.national_id.set(selected_vet[2])
            self.phone.set(selected_vet[3])
            self.email.set(selected_vet[4])
            self.vet_id.set(selected_vet[5])
            self.specialization.set(selected_vet[6])
            self.license_number.set(selected_vet[7])

