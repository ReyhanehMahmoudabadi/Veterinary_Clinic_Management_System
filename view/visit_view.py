from tkinter import *
from tkinter import ttk, messagebox
from controller.visit_controller import VisitController
from datetime import datetime


class VisitView:

    def __init__(self):
        self.controller = VisitController()

        self.window = Toplevel()
        self.window.geometry("1150x550")
        self.window.title("Visits")

        # Visit ID
        Label(self.window, text="Visit ID").place(x=30, y=30)
        self.visit_id = StringVar()
        Entry(self.window, textvariable=self.visit_id).place(x=140, y=30)

        # Visit Date
        Label(self.window, text="Visit Date").place(x=30, y=75)
        self.visit_date = StringVar()
        Entry(self.window, textvariable=self.visit_date).place(x=140, y=75)

        # Reason
        Label(self.window, text="Reason").place(x=30, y=120)
        self.reason = StringVar()
        Entry(self.window, textvariable=self.reason).place(x=140, y=120)

        # Status
        Label(self.window, text="Status").place(x=30, y=165)
        self.status = StringVar()
        Entry(self.window, textvariable=self.status).place(x=140, y=165)

        # Vet ID
        Label(self.window, text="Vet ID").place(x=30, y=210)
        self.vet_id = StringVar()
        Entry(self.window, textvariable=self.vet_id).place(x=140, y=210)

        # Pet ID
        Label(self.window, text="Pet ID").place(x=30, y=255)
        self.pet_id = StringVar()
        Entry(self.window, textvariable=self.pet_id).place(x=140, y=255)

        # Diagnosis
        Label(self.window, text="Diagnosis").place(x=30, y=300)
        self.diagnosis = StringVar()
        Entry(self.window, textvariable=self.diagnosis).place(x=140, y=300)

        # Treatment
        Label(self.window, text="Treatment").place(x=30, y=345)
        self.treatment = StringVar()
        Entry(self.window, textvariable=self.treatment).place(x=140, y=345)

        # Table
        self.table = ttk.Treeview(
            self.window,
            show="headings",
            columns=[1, 2, 3, 4, 5, 6, 7, 8]
        )
        self.table.place(x=380, y=20, width=740, height=470)

        self.table.column(1, width=90)
        self.table.column(2, width=110)
        self.table.column(3, width=90)
        self.table.column(4, width=85)
        self.table.column(5, width=70)
        self.table.column(6, width=70)
        self.table.column(7, width=110)
        self.table.column(8, width=115)

        self.table.heading(1, text="Visit ID")
        self.table.heading(2, text="Visit Date")
        self.table.heading(3, text="Reason")
        self.table.heading(4, text="Status")
        self.table.heading(5, text="Vet ID")
        self.table.heading(6, text="Pet ID")
        self.table.heading(7, text="Diagnosis")
        self.table.heading(8, text="Treatment")

        self.table.bind("<ButtonRelease>", self.table_click)

        # Save Button
        Button(
            self.window,
            text="Save",
            command=self.save_click
        ).place(x=80, y=480, width=80, height=35)
        self.reset_form()

    # Reset Form and Refresh Table
    def reset_form(self):
        self.visit_id.set("")
        self.visit_date.set("")
        self.reason.set("")
        self.status.set("")
        self.vet_id.set("")
        self.pet_id.set("")
        self.diagnosis.set("")
        self.treatment.set("")

        for item in self.table.get_children():
            self.table.delete(item)

        success, result = self.controller.find_all()

        if success:
            for visit in result:
                self.table.insert("", END, values=visit.to_tuple())
        else:
            messagebox.showerror("Error", result)

    # Save Button Click
    def save_click(self):
        try:
            success, message = self.controller.save(
                self.visit_id.get(),
                datetime.fromisoformat(self.visit_date.get()),
                self.reason.get(),
                self.status.get(),
                int(self.vet_id.get()),
                self.pet_id.get(),
                self.diagnosis.get() or None,
                self.treatment.get() or None
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
        selected_visit = self.table.item(selected_id)["values"]

        if selected_visit:
            self.visit_id.set(selected_visit[0])
            self.visit_date.set(selected_visit[1])
            self.reason.set(selected_visit[2])
            self.status.set(selected_visit[3])
            self.vet_id.set(selected_visit[4])
            self.pet_id.set(selected_visit[5])
            self.diagnosis.set(selected_visit[6])
            self.treatment.set(selected_visit[7])