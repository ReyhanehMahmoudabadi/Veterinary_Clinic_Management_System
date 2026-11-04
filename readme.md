# 🐾 Veterinary Clinic Management System

<p align="center">
  A Python-based desktop application for managing veterinary clinic operations.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/GUI-Tkinter-2C8EBB?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Paradigm-OOP-6A5ACD?style=for-the-badge" />
</p>

---

## 📌 About The Project

**Veterinary Clinic Management System** is a desktop application developed in Python to organize and manage essential veterinary clinic information.

The application provides a graphical user interface for managing pet owners, pets, veterinarians, and visits. It is designed using Object-Oriented Programming (OOP) principles and a layered architecture to keep the code organized and maintainable.

## ✨ Features

- **Owner Management** – Register and manage pet owner information.
- **Pet Management** – Add and manage pets and their owner relationships.
- **Veterinarian Management** – Store veterinarian information and specializations.
- **Visit Management** – Record appointments, visit details, diagnoses, and treatments.
- **Data Validation** – Validate user inputs and prevent duplicate IDs.
- **Relationship Validation** – Verify related pet and veterinarian records before saving visits.
- **Graphical User Interface** – Manage records through Tkinter windows.

## 🛠️ Technologies

- Python 3
- Object-Oriented Programming (OOP)
- Tkinter
- File Handling
- Exception Handling

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
│   ├── owner_test.py
│   ├── pet_test.py
│   ├── vet_test.py
│   └── visit_test.py
│
├── tools/
│   └── validation.py
│
├── view/
│   ├── owner_view.py
│   ├── pet_view.py
│   ├── vet_view.py
│   ├── visit_view.py
│   └── panel_view.py
│
├── main.py
└── README.md
```

## 🚀 Getting Started

### Prerequisites

- Python 3.x
- PyCharm or another Python IDE

### Installation

1. Clone the repository:

```bash
git clone https://github.com/ReyhanehMahmoudabadi/Veterinary_Clinic_Management_System.git
```

2. Navigate to the project directory:

```bash
cd Veterinary_Clinic_Management_System
```

3. Run the application:

```bash
python main.py
```

## 🏗️ Application Architecture

The project follows a layered architecture, separating different responsibilities:

| Layer | Responsibility |
|---|---|
| Model | Defines application entities |
| Data Access | Handles data storage and retrieval |
| Business Logic | Implements business rules and validations |
| Controller | Connects views with business logic |
| View | Provides the graphical user interface |
| Tools | Contains reusable utility functions |
| Test | Contains testing modules |

## 🎯 Project Purpose

This project was developed as a practical exercise in Python programming, Object-Oriented Design, layered architecture, data management, input validation, and GUI development.

---

<p align="center">
  Made with ❤️ by <a href="https://github.com/ReyhanehMahmoudabadi">Reyhaneh Mahmoudabadi</a>
</p>