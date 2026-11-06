<div align="center">

# 🐾 Veterinary Clinic Management System

**A desktop application for managing veterinary clinic records**

Built with Python, Tkinter, and Object-Oriented Programming (OOP).

</div>

---

## ⚠️ Important Notes

> **Please read these notes before running the application.**

- **Keep the project structure unchanged.** Do not rename, move, or remove the project folders or Python files. The application depends on the existing package names and file paths.
- **Run the application from the project root directory** — the folder containing `main.py` — so that the local data paths work correctly.
- **Follow the required data-entry order:** register an **Owner** before registering their **Pet**. Register **Vets** before creating **Visits**. Each visit must reference an existing Pet ID and Vet ID.
- The application stores records locally in `.dat` files using Python's `pickle` module. Do not manually edit these files. Back up the `data_access/data/` folder before making changes if you need to preserve your records.

---

---

## 📖 Overview

The Veterinary Clinic Management System is a Python desktop application designed to organize essential veterinary clinic information through a graphical user interface. It provides separate sections for managing pet owners, pets, veterinarians, and veterinary visits.

The project applies Object-Oriented Programming principles and a layered architecture to separate the user interface, application logic, data handling, and core entities.

---

## ✨ Features

- Manage pet owner information.
- Register pets and associate them with their owners.
- Manage veterinarian information.
- Create and manage veterinary visit records.
- Use a graphical interface built with Tkinter.
- Validate user input before processing records.
- Store application data locally between runs.

---

## 🛠️ Technologies

- **Language:** Python
- **GUI:** Tkinter and `tkinter.ttk`
- **Programming Concepts:** Object-Oriented Programming (OOP)
- **Data Persistence:** Python `pickle` module (`.dat` files)
- **Validation:** Python `re` and `datetime` modules

---

## 🏗️ Architecture Overview

The application follows a layered architecture in which each layer has a dedicated responsibility:

- **Model:** Defines the main application entities, including `Person`, `Owner`, `Vet`, `Pet`, and `Visit`.
- **View:** Contains the Tkinter windows and interface components used to interact with the application.
- **Controller:** Connects the views to the application logic and coordinates user actions.
- **Business Logic:** Implements the rules and operations for managing owners, pets, veterinarians, and visits.
- **Data Access:** Handles saving and retrieving records from local `.dat` files.
- **Tools:** Provides shared utilities, including input-validation functions.
- **Test:** Contains files used for manually testing application components and operations.

This separation makes the code easier to understand, maintain, and extend.

---

## 📂 Project Structure

```text
Veterinary_Clinic_Management_System/
│
├── business_logic/
│   ├── owner_bl.py
│   ├── pet_bl.py
│   ├── vet_bl.py
│   └── visit_bl.py
│
├── controller/
│   ├── owner_controller.py
│   ├── pet_controller.py
│   ├── vet_controller.py
│   └── visit_controller.py
│
├── data_access/
│   ├── data/
│   │   ├── owner.dat
│   │   ├── pet.dat
│   │   ├── vet.dat
│   │   └── visit.dat
│   ├── owner_da.py
│   ├── pet_da.py
│   ├── vet_da.py
│   └── visit_da.py
│
├── model/
│   ├── person.py
│   ├── owner.py
│   ├── pet.py
│   ├── vet.py
│   └── visit.py
│
├── test/
│   ├── person_test.py
│   ├── owner_test.py
│   ├── pet_test.py
│   ├── vet_test.py
│   └── visit_test.py
│
├── tools/
│   └── validation.py
│
├── view/
│   ├── panel_view.py
│   ├── owner_view.py
│   ├── pet_view.py
│   ├── vet_view.py
│   └── visit_view.py
│
└── main.py
```

---

## 📋 Requirements

- **Python 3:** The application is written in Python 3.
- **Tkinter:** Used to build the graphical user interface. It is included with many standard Python installations. On some Linux distributions, it may need to be installed separately.
- **Standard-library modules:** The project uses modules such as `datetime`, `os`, `pickle`, and `re`. These are included with Python.

**No third-party Python packages are required** for the application's current functionality. A separate `requirements.txt` file is therefore not necessary.

---

## ⚙️ Installation & Setup

### 1. Get the project

Clone the repository:

```bash
git clone https://github.com/ReyhanehMahmoudabadi/Veterinary_Clinic_Management_System.git
```

Alternatively, download the repository as a ZIP file and extract it.

### 2. Open the project directory

Open the `Veterinary_Clinic_Management_System` folder in your IDE or terminal. Make sure the terminal's current working directory is the project root — the directory containing `main.py`.

### 3. Check Tkinter availability

You can check whether Tkinter is available by running:

```bash
python -m tkinter
```

If a small Tkinter window appears, it is available.

---

## ▶️ Usage

Run the application from the project root directory:

```bash
python main.py
```

The main window provides access to the Owners, Pets, Vets, and Visits sections. Follow the data-entry requirements described in [Important Notes](#-important-notes) when creating records.

---

## 💾 Data Storage

The application stores records locally in `.dat` files inside `data_access/data/`. The Python `pickle` module is used to serialize and retrieve the records.

Keep the `data_access/data/` directory in its original location. To protect existing records, make a backup of this directory before modifying or replacing the project files.

---

## 🧪 Tests

The `test/` directory contains Python files with manual test examples for the project's models, controllers, business logic, and data-access components. These files are not configured as an automated `unittest` test suite.

---

## 👩‍💻 Author

**Reyhaneh Mahmoudabadi**

---

<div align="center">

*Developed as an Object-Oriented Programming project.*

❤️

</div>
