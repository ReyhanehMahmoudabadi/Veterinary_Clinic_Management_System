
from tkinter import *
from tkinter import ttk, messagebox
from controller.owner_controller import OwnerController


class OwnerView:

    def __init__(self):
        self.controller = OwnerController()

        self.win = Toplevel()
        self.win.geometry("1150x550")
        self.win.title("Owners")

        # Owner ID
        Label(self.win, text="Owner ID").place(x=30, y=30)
        self.owner_id = StringVar()
        Entry(self.win, textvariable=self.owner_id).place(x=140, y=30)

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

        # Email
        Label(self.win, text="Email").place(x=30, y=255)
        self.email = StringVar()
        Entry(self.win, textvariable=self.email).place(x=140, y=255)

        # Address
        Label(self.win, text="Address").place(x=30, y=300)
        self.address = StringVar()
        Entry(self.win, textvariable=self.address).place(x=140, y=300)

        # Table
        self.table = ttk.Treeview(
            self.win,
            show="headings",
            columns=[1, 2, 3, 4, 5, 6, 7]
        )
        self.table.place(x=380, y=20,width=740,height=470)

        self.table.column(1, width=90)
        self.table.column(2, width=90)
        self.table.column(3, width=100)
        self.table.column(4, width=100)
        self.table.column(5, width=120)
        self.table.column(6, width=90)
        self.table.column(7, width=150)

        self.table.heading(1, text="Name")
        self.table.heading(2, text="Family")
        self.table.heading(3, text="National ID")
        self.table.heading(4, text="Phone")
        self.table.heading(5, text="Email")
        self.table.heading(6, text="Owner ID")
        self.table.heading(7, text="Address")

        self.table.bind("<ButtonRelease>", self.table_click)

        Button(
            self.win,
            text="Save",
            command=self.save_click
        ).place(x=80, y=480,width=80,height=35)

        self.reset_form()

    # Reset Form and Refresh Table
    def reset_form(self):
        self.owner_id.set("")
        self.name.set("")
        self.family.set("")
        self.national_id.set("")
        self.phone.set("")
        self.email.set("")
        self.address.set("")

        # Clear Table
        for item in self.table.get_children():
            self.table.delete(item)

        # Set All Owners On Table
        success, owner_list = self.controller.find_all()

        if success:
            for owner in owner_list:
                self.table.insert("", END, values=owner.to_tuple())

    # Save Button Click
    def save_click(self):
        try:
            success, message = self.controller.save(
                self.name.get(),
                self.family.get(),
                self.national_id.get(),
                self.phone.get(),
                int(self.owner_id.get()),
                self.address.get(),
                self.email.get() or None
            )

            if success:
                messagebox.showinfo("Success", message)
                self.reset_form()
            else:
                messagebox.showerror("Error", message)

        except ValueError as e:
            messagebox.showerror("Error", str(e))

    # Table Click
    def table_click(self, event):
        selected_owner_id = self.table.focus()
        selected_owner = self.table.item(selected_owner_id)["values"]

        if selected_owner:
            self.name.set(selected_owner[0])
            self.family.set(selected_owner[1])
            self.national_id.set(selected_owner[2])
            self.phone.set(selected_owner[3])
            self.email.set(selected_owner[4])
            self.owner_id.set(selected_owner[5])
            self.address.set(selected_owner[6])
